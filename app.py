from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
from werkzeug.exceptions import abort


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


def get_db_connection():
    connection = sqlite3.connect('blog.db')
    connection.row_factory = sqlite3.Row
    return connection


def get_post(post_id):
    c = get_db_connection()
    post = c.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    c.close()

    if post is None:
        abort(404)

    return post


@app.route("/")
def index():
    c = get_db_connection()
    posts = c.execute('SELECT * FROM posts ORDER BY "created" DESC').fetchall()
    c.close()
    return render_template('index.html', posts_html=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post_html=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            c = get_db_connection()
            c.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            c.commit()
            c.close()
            return redirect(url_for('index'))

    return render_template('create.html'h