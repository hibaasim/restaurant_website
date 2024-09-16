#!/usr/bin/python3
'''Flask app for endpoints and templates'''

from flask import Flask, render_template

app = Flask(__name__)

#sample data
menu_items = [
    {"id": 1, "name": "Dish 1", "price": 10.99},
    {"id": 2, "name": "Dish 2", "price": 12.99},
    {"id": 3, "name": "Dish 3", "price": 8.99},
]

reservations = []


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/about')
def about(): 
    return render_template('about.html', title='About')

  
@app.route('/menu')
def menu():
    return render_template('menu.html', menu=menu_items, title='Menu')


@app.route('/reservation')
def reserve():
    return render_template('book.html', title='Reservation')


# API endpoint to get menu items (move to api folder for better amangement one file 
# for menu items and the other for reservations)
@app.route('/api/menu', methods=['GET'])
def get_menu():
    return jsonify(menu_items)

# API endpoint to create a reservation
@app.route('/api/reservation', methods=['POST'])
def create_reservation():
    data = request.get_json()
    reservations.append(data)
    return jsonify({"message": "Reservation created!", "data": data}), 201

#Add api to get reservation from file storage  

if __name__=='__main__':
    app.run(debug=True)