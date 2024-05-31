from categories.model import categories_model
from products.model import products_model


def create_categories():
    categories = [
        {'key': "coffee", 'name': "Coffee"},
        {'key': "tea", 'name': "Tea"},
        {'key': "lemonades", 'name': "Lemonades"},
        {'key': "desserts", 'name': "Desserts"},
        {'key': "snacks", 'name': "Snacks"},
    ]
    categories_model.collection.insert_many(categories)


def create_products():
    products = [
        {
            'name': "Espresso", 'category': "coffee", 'description': "Rich and creamy espresso",
            'img_path': "/img/coffee/Espresso.png", 'price': 2.5, 'portion': "100 ml", 'status': "A", 'comment': None
        },
        {
            'name': "Latte", 'category': "coffee", 'description': "Smooth and mild latte",
            'img_path': "/img/coffee/Latte.png", 'price': 4, 'portion': "300 ml", 'status': "A", 'comment': None
        },
        {
            'name': "Cappuccino", 'category': "coffee", 'description': "Classic cappuccino",
            'img_path': "/img/coffee/Cappuccino.png", 'price': 3.5, 'portion': "300 ml", 'status': "A", 'comment': None
        },
        {
            'name': "Green Tea", 'category': "tea", 'description': "Tonic green tea",
            'img_path': "/img/tea/GreenTea.png", 'price': 2, 'portion': "200 ml", 'status': "A", 'comment': None
        },
        {
            'name': "Black Tea", 'category': "tea", 'description': "Strong black tea",
            'img_path': "/img/tea/BlackTea.png", 'price': 2, 'portion': "200 ml", 'status': "A", 'comment': None
        },
        {
            'name': "Herbal Tea", 'category': "tea", 'description': "Blend of various herbs",
            'img_path': "/img/tea/HerbalTea.png", 'price': 2.5, 'portion': "200 ml", 'status': "A", 'comment': None
        },
        {
            'name': "Lemonade", 'category': "lemonades", 'description': "Refreshing lemonade",
            'img_path': "/img/lemonades/Lemonade.png", 'price': 2.5, 'portion': "250 ml", 'status': "A", 'comment': None
        },
        {
            'name': "Pink Lemonade", 'category': "lemonades", 'description': "Lemonade with a hint of strawberry",
            'img_path': "/img/lemonades/PinkLemonade.png", 'price': 3, 'portion': "250 ml", 'status': "A", 'comment': None
        },
        {
            'name': "Earl Grey", 'category': "tea", 'description': "Black tea with bergamot",
            'img_path': "/img/tea/EarlGrey.png", 'price': 2.5, 'portion': "200 ml", 'status': "A", 'comment': None
        },
        {
            'name': "Croissant", 'category': "snacks", 'description': "Buttery croissant",
            'img_path': "/img/snacks/Croissant.png", 'price': 1.5, 'portion': "150 gr", 'status': "N", 'comment': None
        },
        {
            'name': "Muffin", 'category': "snacks", 'description': "Buttery croissant",
            'img_path': "/img/snacks/Muffin.png", 'price': 2, 'portion': "150 gr", 'status': "N", 'comment': None
        },
        {
            'name': "Brownie", 'category': "desserts", 'description': "Chocolate brownie",
            'img_path': "/img/desserts/Brownie.png", 'price': 2.5, 'portion': "100 gr", 'status': "A", 'comment': None
        },
        {
            'name': "Cheesecake", 'category': "desserts", 'description': "Creamy and smooth cheesecake",
            'img_path': "/img/desserts/Cheesecake.png", 'price': 3, 'portion': "100 gr", 'status': "A", 'comment': None
        },
        {
            'name': "Tiramisu", 'category': "desserts", 'description': "Dessert with coffee and mascarpone cheese",
            'img_path': "/img/desserts/Tiramisu.png", 'price': 3.5, 'portion': "100 gr", 'status': "A", 'comment': None
        },
        {
            'name': "Lemon Tart", 'category': "desserts", 'description': "Tart and sweet lemon dessert",
            'img_path': "/img/desserts/LemonTart.png", 'price': 3, 'portion': "100 gr", 'status': "N", 'comment': None
        },
        {
            'name': "Macchiato", 'category': "coffee", 'description': "Espresso with a small amount of milk",
            'img_path': "/img/coffee/Macchiato.png", 'price': 3, 'portion': "150 ml", 'status': "A", 'comment': None
        },
        {
            'name': "Frappuccino", 'category': "coffee", 'description': "Blended coffee drink",
            'img_path': "/img/coffee/Frappuccino.png", 'price': 3.5, 'portion': "300 ml", 'status': "A", 'comment': None
        },
        {
            'name': "Macarons", 'category': "desserts", 'description': "Colorful and delicate French cookies",
            'img_path': "/img/desserts/Macarons.png", 'price': 4, 'portion': "100 gr", 'status': "A", 'comment': None
        },
    ]
    products_model.collection.insert_many(products)


def create_order():
    pass


if __name__ == '__main__':
    create_categories()
    create_products()
