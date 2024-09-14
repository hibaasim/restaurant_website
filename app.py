#!/usr/bin/python3
'''Flask app for endpoints and templates'''

from flask install Flask,z render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/reserve')
def reserve():
    return render_template('book.html')


if __name__=='__main__':
    app.run()