from flask import Flask
from flask_cors import CORS
from categories.controller import module as categories_blueprint
from orders.controller import module as orders_blueprint
from products.controller import module as products_blueprint

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(categories_blueprint)
app.register_blueprint(orders_blueprint)
app.register_blueprint(products_blueprint)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
