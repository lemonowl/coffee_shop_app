from datetime import datetime
from pymongo.collection import Collection, ObjectId
from pymongo.cursor import Cursor
from pymongo.command_cursor import CommandCursor
from database import DatabaseModel

__all__ = ['orders_model', 'STATUSES']

STATUSES = {
    'Pending': 'A',  # active
    'Completed': 'F',  # finished
    'Cancelled': 'C',  # cancelled
}


class OrdersItemsModel(DatabaseModel):

    @property
    def collection(self) -> Collection:
        return self.db.order_items

    def create_items(self, items: list[dict]) -> None:
        self.collection.insert_many(items)

    def update_items(self, items: list[dict]) -> None:
        for item in items:
            self.collection.update_one({'_id': ObjectId(item.pop('id'))}, {'$set': item})

    def delete_items(self, items: list[str]) -> None:
        ids = [ObjectId(i) for i in items]
        self.collection.delete_many({'_id': {'$in': ids}})

    def get_items(self, *args, **kwargs) -> Cursor:
        return self.collection.find(*args, **kwargs)


class OrdersModel(DatabaseModel):

    def __init__(self):
        super().__init__()
        self.__items_model = OrdersItemsModel()

    @property
    def collection(self) -> Collection:
        return self.db.orders

    def get_list(self) -> CommandCursor:
        return self._get_aggregation()

    def get_order_by_id(self, order_id: str) -> dict:
        result = self._get_aggregation(order_id)
        try:
            return result.next()
        except StopIteration:
            return {}

    def save_order(self, order: dict) -> bool:
        try:
            if 'id' in order.keys():
                self.update_order(order)
            else:
                self.create_order(order)
            return True
        except Exception as e:
            print(e)
            return False

    def create_order(self, order: dict) -> None:
        order['status'] = STATUSES['Pending']
        order['created'] = datetime.now()
        order_id = self.collection.insert_one(order).inserted_id

        items_list = []
        for item in order['items']:
            item_data = {
                'product_id': ObjectId(item['product_id']),
                'order_id': order_id,
                'count': int(item.get('count', 1)),
                'comment': str(item.get('comment', '')),
            }
            items_list.append(item_data)
        self.__items_model.create_items(items_list)

    def update_order(self, order: dict) -> None:
        db_order = self.get_order_by_id(order['id'])

        order_id = ObjectId(order.pop('id'))
        order_items = order.pop('items')
        order['status'] = STATUSES[order['status']]

        update_fields = {key: val for key, val in order.items() if val != db_order[key]}
        if update_fields:
            self.collection.update_one({'_id': order_id}, {'$set': update_fields})

        # удаляем помеченные на удаление товары
        deleted_items = []
        for item in [i for i in order_items if i.get('deleted')]:
            deleted_items.append(item['id'])
            order_items.remove(item)
        self.__items_model.delete_items(deleted_items)

        # собираем новые товары, если они есть в заказе
        new_items = []
        for item in order_items.copy():
            if 'id' not in item.keys():
                item_data = {
                    'product_id': ObjectId(item['product_id']),
                    'order_id': order_id,
                    'count': int(item.get('count', 1)),
                    'comment': str(item.get('comment', '')),
                }
                new_items.append(item_data)
                order_items.remove(item)

        # обновляем изменившиеся поля у оставшихся товаров
        db_items = list(self.__items_model.get_items({'order_id': order_id}, {'count': 1, 'comment': 1}))
        updated_items = []
        for index, item in enumerate(order_items):
            db_rec = [i for i in db_items if str(i['_id']) == item['id']][0]
            upd_item = {key: item[key] for key in ['count', 'comment'] if item[key] != db_rec[key]}
            if upd_item:
                upd_item['id'] = item['id']
                updated_items.append(upd_item)
            db_items.remove(db_rec)
        self.__items_model.update_items(updated_items)

        # сохраняем новые товары
        if new_items:
            self.__items_model.create_items(new_items)

    def change_status(self, order_id: str, status: str) -> bool:
        if status not in STATUSES.keys():
            raise ValueError("Processing of this type of status has not yet been implemented")

        try:
            self.collection.update_one({'_id': ObjectId(order_id)}, {'$set': {'status': STATUSES[status]}})
            return True
        except Exception as e:
            print(e)
            return False

    def _get_aggregation(self, order_id: str = None) -> CommandCursor:
        _filter = {'status': STATUSES['Pending']}
        if order_id:
            _filter['_id'] = ObjectId(order_id)

        cursor = self.collection.aggregate([
            {'$match': _filter},
            {'$lookup': {
                'from': 'order_items', 'localField': '_id', 'foreignField': 'order_id', 'as': 'items'}},
            {'$unwind': '$items'},
            {'$lookup': {'from': 'products', 'localField': 'items.product_id', 'foreignField': '_id', 'as': 'props'}},
            {'$unwind': '$props'},
            {'$group': {
                '_id': '$_id',
                'number': {'$first': '$number'},
                'total': {'$first': '$total'},
                'status': {'$first': '$status'},
                'comment': {'$first': '$comment'},
                'created': {'$first': '$created'},
                'items': {
                    '$push': {
                        'id': '$items._id',
                        'product_id': '$items.product_id',
                        'name': '$props.name',
                        'price': '$props.price',
                        'count': '$items.count',
                        'comment': '$items.comment'
                    }
                },
            }},
            {'$sort': {'created': 1}}, {'$project': {'created': 0}}
        ])
        return cursor


orders_model = OrdersModel()
