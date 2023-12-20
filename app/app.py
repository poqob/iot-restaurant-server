from flask import Flask, render_template, request, g
import sqlite3

app = Flask(__name__)
app.config['DATABASE'] = './db/main.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    cur = get_db().cursor()
    cur.execute('SELECT * FROM role')
    data = cur.fetchall()
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
