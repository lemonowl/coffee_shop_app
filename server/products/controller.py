from flask import Blueprint, jsonify, Response
from products.model import products_model

module = Blueprint('products', __name__, url_prefix='/api/products')


@module.route('get_list', methods=['POST'])
def get_products() -> Response:
    """Возвращает список доступных товаров
    """
    return jsonify(list(products_model.get_products_for_showcase()))


@module.route('get_shortlist', methods=['POST'])
def get_products_shortlist() -> Response:
    """Возвращает список товаров для отображения в списке
    """
    products = [{'id': str(item.pop('_id')), **item} for item in products_model.get_products_for_order()]
    products.sort(key=lambda k: k['category'])
    return jsonify(products)


@module.route('get/<product_id>', methods=['POST'])
def get_product_by_id(product_id) -> Response:
    """Возвращает товар по его ID
    """
    product = dict(products_model.get_product_by_id(product_id))
    product['product_id'] = str(product.pop('_id'))
    product['count'] = 1
    return jsonify(product)
