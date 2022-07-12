import sqlite3

from flask import Flask, render_template, request, url_for, flash, redirect

from werkzeug.exceptions import abort

def get_db_connection(): #Esta funcion sirve para abrir un coneccion de base de datos y ejecucion de la consulta SQL

    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id): #Determinara la entrada de blog a recuperar
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id) # utiliza la función get_post() para
     #obtener la entrada de blog asociada con el ID especificado y almacenar el resultado en la variable post
    return render_template('post.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    return render_template('create.html')