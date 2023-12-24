from flask import Flask, render_template, request, g
import sqlite3
from models.desk import Desk
from models.mDesk import Mdesk
from models.led import RGBLED

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


@app.route("/")
def index():
    return render_template("welcome.html")


# dedect desk object is valid and return desk page up to its role. (admin, user, guest...)
@app.route("/desk/<string:desk_rfid>")
def desk_access(desk_rfid):
    # db connection
    connection = get_db()
    cursor = connection.cursor()

    try:
        # query
        cursor.execute("select * from desk where desk_rfid = ?", (desk_rfid,))
        data = cursor.fetchone()
    except sqlite3.Error as e:
        print(e)
        return render_template("InvalidDesk.html")

    # parse query result
    id = data[0]
    _desk_rfid = data[1]
    desk_role_id = data[2]
    status = data[3]
    rgb = data[4]

    # create desk object
    desk = Desk(id, _desk_rfid, desk_role_id, status, rgb)

    if desk:
        desk.status = 1
        cursor.execute("update desk set status = 1 where id = ?", (id,))
        return get_desk_page(
            desk=desk
        )  # create a user page that takes data as parameter.
    else:
        return render_template(
            "InvalidDesk.html"
        )  # create and return invalid desk html error page.


def get_desk_page(desk):
    if desk.desk_role_id == 1:
        return render_template("admin_desk.html", mdesk=Mdesk(desk).serialize())
    elif desk.desk_role_id == 2:
        return render_template("user_desk.html", mdesk=Mdesk(desk).serialize())
    else:
        return render_template("guest_desk.html", mdesk=Mdesk(desk).serialize())


@app.route("/pay")
def pay():
    if request.method == "POST":
        data = request.get_json()
        try:
            return {"desk_rfid":data, "call_waiter":True}
        except sqlite3.Error as e:
            print(e)
            return {"desk_rfid":data, "call_waiter":False}


@app.route("/call_waiter")
def call_waiter():
    if request.method == "POST":
        data = request.get_json()
        try:
            # TODO: call esp waiter.
            return {"desk_rfid": data, "call_waiter": True}
        except sqlite3.Error as e:
            print(e)
            return {"desk_rfid": data, "call_waiter": False}


@app.route("/color_change", methods=["POST"])
def color_change():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        _led = RGBLED.parse(data)
        return _led.serialize()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
