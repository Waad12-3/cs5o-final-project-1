import os
import sqlite3
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

#from helpers import apology, login_required, lookup, usd

app = Flask(__name__)

db = SQL("sqlite:///space.db")

@app.route('/search')
def search():
    query = request.args.get('query').lower()

    if query == "earth":
        return redirect('/earth.html')
    elif query == "stars":
        return redirect('/stars.html')
    elif query == "galaxies":
        return redirect('/galaxies.html')
    elif query == "black holes":
        return redirect('/blackhole.html')
    elif query == "planets":
        return redirect('/planets.html')

    return render_template('index.html', query=query)

@app.route("/")
def index():
    conn = sqlite3.connect('space.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT solar_system.id, solar_system.title, solar_system.description, solar_system.url, photos.photo_name, photos.photo_link FROM solar_system LEFT JOIN photos ON solar_system.id = photos.id''')
    space_data = cursor.fetchall()
    cursor.execute('''SELECT id, title, description, url FROM books''')
    missions_data = cursor.fetchall()
    cursor.execute('''SELECT id, mission_name, mission_description, mission_link FROM missions''')
    books_data = cursor.fetchall()
    cursor.execute('''SELECT id, nasa_name, nasa_description, nasa_link FROM nasa''')
    nasa_data = cursor.fetchall()
    conn.close()

    print(space_data)

    return render_template("index.html", space_data=space_data, books_data=books_data, missions_data=missions_data, nasa_data=nasa_data)

@app.route('/earth.html')
def earth():
    return render_template('earth.html')

@app.route('/stars.html')
def stars():
    return render_template('stars.html')

@app.route('/galaxies.html')
def galaxies():
    return render_template('galaxies.html')

@app.route('/blackhole.html')
def blackhole():
    return render_template('blackhole.html')

def get_db_connection():
    conn = sqlite3.connect('space.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/planets.html')
def planets():
    conn = get_db_connection()
    planets = conn.execute('SELECT * FROM planets').fetchall()
    conn.close()
    return render_template('planets.html', planets=planets)

if __name__== "__main__":
    app.run()

