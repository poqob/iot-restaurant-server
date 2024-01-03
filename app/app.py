from flask import Flask, render_template, request, g
import sqlite3
from models.desk import Desk
from models.mDesk import Mdesk
from models.led import RGBLED
from models.log import Log
from datetime import datetime
from api.espApi import EspApi
import json

app = Flask(__name__)
app.config["DATABASE"] = "./db/main.db"
api_esp = EspApi()


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
        connection.commit()
        cursor.close()
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


@app.route("/pay", methods=["POST"])
def pay():
    if request.method == "POST":
        data = request.get_json()
        desk_rfid = data["desk_rfid"]
        connection = get_db()
        cursor = connection.cursor()
        try:
            query = 'update desk set status = 0 where desk_rfid = "' + desk_rfid + '";'
            cursor.execute(query)
            connection.commit()
            return render_template("thank_you.html")
        except sqlite3.Error as e:
            print(e)
            return {"log_status": False}
        finally:
            cursor.close()


@app.route("/call_waiter", methods=["POST"])
def call_waiter():
    if request.method == "POST":
        data = request.get_json()
        try:
            api_esp.call_waiter(data["desk_rfid"])
            return {"desk_rfid": data, "call_waiter": True}
        except sqlite3.Error as e:
            print(e)
            return {"desk_rfid": data, "call_waiter": False}


# post request to change color of led.
@app.route("/color_change", methods=["POST"])
def color_change():
    connection = get_db()
    cursor = connection.cursor()
    if request.method == "POST":
        data = request.get_json()
        led_ = data["rgb"]
        desk_rfid = data["desk_rfid"]
        _led = RGBLED.parse(led_)
        if _led:
            api_esp.color_change(_led)  # send request to esp
            rgb_field = json.dumps(_led.serialize()).replace('"', '""')
            query = (
                'update desk set rgb = "'
                + rgb_field
                + '" where desk_rfid = "'
                + desk_rfid
                + '";'
            )
            cursor.execute(query)
            connection.commit()
            cursor.execute("select * from desk;")
            record = cursor.fetchall()
            cursor.close()
            print(record)
            return _led.serialize()
        return {"log_status": False}


# admin routes


# TODO: change this, flask will call esp/log and receive log data from esp.
@app.route("/log", methods=["POST"])
def log():
    if request.method == "POST":
        data = request.get_json()
        connection = get_db()
        cursor = connection.cursor()
        try:
            log = Log.parse(data)
            timestamp = datetime.now()
            time_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            if log:
                serialized = json.dumps(data).replace('"', '""')

                query = (
                    'insert into log (log,timestamp) values ("'
                    + serialized
                    + '","'
                    + time_str
                    + '");'
                )

                cursor.execute(query)
                connection.commit()
                return log.serialize()
        except sqlite3.Error as e:
            print(e)
            return "{error}"


# incoming data is json object with desk_rfid(string) and attic status(0-1) fields.
@app.route("/attic", methods=["POST"])
def attic():
    if request.method == "POST":
        data = request.get_json()
        connection = get_db()
        cursor = connection.cursor()
        try:
            _attic = data["attic"]
            _desk_rfid = data["desk_rfid"]
            _post = api_esp.attic(data)

            return {"attic": _attic, "desk_rfid": _desk_rfid}

        except sqlite3.Error as e:
            print(e)
            return "{error}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
