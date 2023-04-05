#!/usr/bin/env python3

from flask import Flask, render_template
from flask_migrate import Migrate

from models import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///meow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = "False"

migrate = Migrate(app, db)
 
db.init_app(app)

@app.route('/')
def home():
    return('<h1>Python Operations with Flask Routing and Views</h1>')

@app.route('/print/<param>')
def print_page(param):
    print(f'{param}')
    for _ in range(5):
        return param

@app.route('/count/<int:param>')
def count(param):
    string = ''
    if param == 0:
        print(0)
    for i in range(0, param):
        print(f'{i}')
        string = string + (f'{i}\n')
    return string

@app.route('/math/<params>')
def math(params):
    print("math")
    print(params)
    total = 0
    if not params.find('div') == -1:
        new = params.split('div')
        for i in range(len(new)):
            if i == 0:
                total = int(new[i])
            else:
                total /= int(new[i]) 
    if not params.find('*') == -1:
        new = params.split('*')
        for i in range(len(new)):
            if i == 0:
                total = int(new[i])
            else:
                total *= int(new[i])
    if not params.find('+') == -1:
        print("adding")
        new = params.split('+')
        total = 0
        for i in range(len(new)):
            total += int(new[i])
    if not params.find('-') == -1:
        print("subtracting")
        total = 0
        new = params.split('-')
        for i in range(len(new)):
            if i == 0:
                total = int(new[i])
                print(f'assigned to total: {total}')
            else:
                print(f'subtracting from total: {new[i]}')
                total -= int(new[i])
    print("total")
    print (total)
    return str(total)


if __name__ == '__main__':
    app.run(port=5555, debug=True)