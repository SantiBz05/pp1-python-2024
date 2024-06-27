from flask import (Flask, render_template, redirect, request)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/productos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Marca, Tipo, Producto

listado_productos = [
    dict(
        name = "Yogurt",
        price = "3000",
        code = "0000000001"
    ),
    dict(
        name = "Rollisec",
        price = "5500",
        code = "0000000002"
    ),
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def productos():
    listado = listado_productos
    return render_template('productos.html', listado=listado)

@app.route('/add_productos', methods=['POST', 'GET'])
def agregar_productos():
    if request.method == 'POST':
        nombre = request.form['name']
        precio = request.form['price']
        codigo = request.form['code']

        producto = dict(
            name = nombre,
            price = precio,
            code = codigo,
        ), #tilingo
        listado_productos.append(producto[0])
        print(nombre, precio, codigo)
    return render_template('add_productos.html')