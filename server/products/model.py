from pymongo.collection import Collection, ObjectId
from pymongo.cursor import Cursor
from database import DatabaseModel

__all__ = ['products_model']

STATUSES = {'active': 'A', 'nonactive': 'N'}


class ProductsModel(DatabaseModel):

    @property
    def collection(self) -> Collection:
        return self.db.products

    def get_products_for_showcase(self) -> Cursor:
        return self.collection.find(
            {'status': STATUSES['active']},
            {'_id': 0, 'comment': 0, 'status': 0},
        )

    def get_products_for_order(self) -> Cursor:
        return self.collection.find(
            {'status': STATUSES['active']},
            {'_id': 1, 'name': 1, 'category': 1},
        )

    def get_product_by_id(self, product_id: str) -> Cursor:
        return self.collection.find_one(
            {'_id': ObjectId(product_id)},
            {'_id': 1, 'name': 1, 'price': 1}
        )

    def get_total_price_by_ids(self, items: list[dict]) -> int | float:
        products_ids = set(ObjectId(i['product_id']) for i in items)
        prices = {
            str(i['_id']): i['price'] for i in
            self.collection.find({'_id': {'$in': list(products_ids)}}, {'price': 1})
        }
        return sum(int(i['count'])*prices[i['product_id']] for i in items)


products_model = ProductsModel()
