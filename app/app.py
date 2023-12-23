from flask import Flask, render_template, request, g
import sqlite3
from models.desk import Desk

app = Flask(__name__)
app.config["DATABASE"] = "./db/main.db"


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(app.config["DATABASE"])
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


# TODO welcome page.
@app.route("/")
def index():
    return render_template("welcome.html")


@app.route("/desk/<string:desk_rfid>")
def desk_access(desk_rfid):
    connection = get_db()
    cursor = connection.cursor()

    cursor.execute("select * from desk where desk_rfid = ?", (desk_rfid,))
    data = cursor.fetchone()

    id = data[0]
    _desk_rfid = data[1]
    desk_role_id = data[2]
    status = data[3]
    rgb = data[4]
    desk = Desk(id, _desk_rfid, desk_role_id, status, rgb)

    if data:
        return desk.serialize()  # create a user page that takes data as parameter.
    else:
        return "Invalid Desk"  # create and return invalid desk html error page.


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
