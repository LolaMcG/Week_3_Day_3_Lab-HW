from flask import render_template
from app import app
from models.order_list import *



@app.route('/orders')
def index():
    return render_template('index.html', title="Instrument Shop", orders = orders, order_1=order_1)

@app.route('/orders/<index>')
def order(index):
    order = orders[int(index)]
    return render_template('order.html', title="sinlge order",order = order)
    
