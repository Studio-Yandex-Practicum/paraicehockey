from flask import Flask, render_template

from src.core.settings import Config

from .models import Product

app = Flask(__name__)
app.config.from_object(Config)


products = [
    [1, 'Мягкая игрушка', 'Талисман Федерации - енот Фырк.',
     'img/fyrk.jpg', 1700],
    [2, 'Сумка поясная-наплечная',
     'Ткань Oxford на подкладе. Вышивка, 2 отделения на молнии',
     'img/bag.jpg', 1700]
]


def add_products(products):
    for product in products:
        Product(*product)
    return Product.all_products


add_products(products)


@app.route('/')
def index_view():
    if products is not None:
        return render_template('index.html', items=Product.all_products)
    return 404


@app.route('/product/<int:id>')
def product_view(id_code):
    product = [item for item in Product.all_products if item.id == id_code]
    if product is not None:
        return render_template('product_card.html', item=product[0])
    return 404
