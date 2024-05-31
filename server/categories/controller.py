from flask import Blueprint, jsonify, Response
from categories.model import categories_model

module = Blueprint('categories', __name__, url_prefix='/api/categories')


@module.route('get_list', methods=['POST'])
def get_categories() -> Response:
    """Возвращает список категорий товаров
    """
    categories = list(categories_model.get_all())
    return jsonify(categories)
