from flask import Flask, render_template
import sqlite3



app = Flask(__name__)


def get_db_connection():
    connection = sqlite3.connect('blog.db')
    connection.row_factory = sqlite3.Row
    return connection


@app.route("/")
def index():
    c = get_db_connection()
    posts = c.execute('SELECT * FROM posts').fetchall()
    c.close()
    return render_template('index.html', posts_html=posts)


@app.route("/wow")
def wow():
    return "<h1>nöhö</h1>"