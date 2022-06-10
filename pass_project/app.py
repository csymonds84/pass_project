import sqlite3
from optparse import Values
from flask import Flask, render_template, send_file, make_response, url_for, Response, request, flash, redirect
from flask_bootstrap import Bootstrap
import pandas as pd
import db_functions


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', PageTitle="Home")

@app.route('/signup', methods=("POST", "GET"))
def sign_up():
    return render_template('sign_up_form.html', PageTitle="Sign Up")

@app.route('/login', methods=("POST", "GET"))
def login():
    return render_template('login.html', PageTitle="Log in")

@app.route('/about')
def about():
    return render_template('about.html', PageTitle="About Us")

@app.route('/usersTable', methods=("POST", "GET"))
def user_tables():
    userTable = db_functions.get_user_data()
    return render_template('usersTable.html', PageTitle="Users Table", table=[userTable.to_html(classes='data', index='flase')], titles=userTable.columns.values)

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn




if __name__ == "__main__":
    app.run(debug=True)