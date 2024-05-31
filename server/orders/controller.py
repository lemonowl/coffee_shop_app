from flask import Blueprint, jsonify, request, Response
from helper import format_request
from orders.model import orders_model, STATUSES as model_statuses
from products.model import products_model

module = Blueprint('orders', __name__, url_prefix='/api/orders')
STATUSES = {value: key for key, value in model_statuses.items()}


@module.route('get_list', methods=['POST'])
def get_orders() -> Response:
    """Возвращает список активных заказов
    """
    orders = []
    for order in orders_model.get_list():
        _format_order(order)
        orders.append(order)
    return jsonify(orders)


@module.route('get/<order_id>', methods=['POST'])
def get_order_by_id(order_id: str) -> Response:
    """Возвращает заказ по его ID
    """
    order = orders_model.get_order_by_id(order_id)
    if not order:
        return jsonify(
            result=False,
            error='Could not find the order in the database',
        )
    _format_order(order)
    return jsonify(order)


@module.route('save', methods=['POST'])
def save_order() -> Response:
    """Создает либо обновляет заказ
    """
    order = format_request(request)
    if not all(k in order.keys() for k in ['number', 'status']):
        return jsonify(
            result=False,
            error="Required parameters: number, status",
        )
    if 'items' not in order.keys():
        return jsonify(
            result=False,
            error="Items is required, choose at least one",
        )

    if not all(['product_id' in item.keys() for item in order['items'] if not item.get('deleted')]):
        return jsonify(
            result=False,
            error="Required parameters for items list: product_id",
        )

    order['number'] = str(order['number'])
    order['comment'] = str(order.get('comment', ''))
    order['total'] = products_model.get_total_price_by_ids([i for i in order['items'] if not i.get('deleted')])
    result = orders_model.save_order(order)

    if not result:
        return jsonify(
            result=result,
            error='Could not save the order to the database',
        )
    return jsonify(result=result)


@module.route('complete/<order_id>', methods=['POST'])
def complete_order(order_id: str) -> Response:
    """Меняет статус заказа на Completed
    """
    result = orders_model.change_status(order_id, 'Completed')
    if not result:
        return jsonify(
            result=result,
            error='Could not save the status to the database',
        )
    return jsonify(result=True)


def _format_order(order: dict) -> None:
    order['id'] = str(order.pop('_id'))
    order['status'] = STATUSES[order['status']]
    for item in order['items']:
        item['id'] = str(item['id'])
        item['product_id'] = str(item['product_id'])
