#!/usr/bin/python3
'''Flask app for endpoints and templates'''

from flask import Flask, render_template, jsonify, request, url_for, redirect

app = Flask(__name__)

#sample data
menu_items = []

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


@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(menu_items)

# API endpoint to create a reservation
@app.route('/reservation', methods=['POST', 'GET'])
def create_reservation():
    if request.method == "POST":
        #take data and make a new page to display them on
        data = request.get_json()
        new_res = {
            "name": data.get("name"),
            "date": data.get("date"),
            "time": data.get("time"),
            "guests": data.get("guests")
        }
        reservations.append(data)
        return jsonify({"message": "Reservation created!", "data": data}), 201
    else:
        return render_template("book.html")  

if __name__=='__main__':
    app.run(debug=True)