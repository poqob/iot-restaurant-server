from models.desk import Desk
import json
class Mdesk:
    def __init__(self, desk):
        self.id = desk.id  # 1-2...
        self.desk_rfid = desk.desk_rfid  # BA:65:D3:A1
        self.desk_role_id = desk.desk_role_id  # 1 admin 2 user
        self.status = desk.status  # 0 or 1
        self.rgb = json.loads(desk.rgb)  # '0 255 255 200' led status, red, green, blue
        # print(self.rgb)
        self.led_status= self.rgb["status"]
        self.red = self.rgb["red"]
        self.green = self.rgb["green"]
        self.blue = self.rgb["blue"]

    def __str__(self):
        return f"Desk ID: {self.id}, RFID: {self.desk_rfid}, Role ID: {self.desk_role_id}, Status: {self.status}, RGB: {self.rgb}"

    def serialize(self):
        return {
            "id": self.id,
            "desk_rfid": self.desk_rfid,
            "desk_role_id": self.desk_role_id,
            "status": self.status,
            "led_status": self.led_status,
            "red": self.red,
            "green": self.green,
            "blue": self.blue,
        }


if __name__ == "__main__":
    desk = Desk(
        1, "BA:65:D3:A1", 1, 1, {"status": True, "red": 255, "green": 0, "blue": 0}
    )
    mdesk = Mdesk(desk)
    print(mdesk.serialize())
