class Desk:
    def __init__(self, desk_id, desk_rfid, desk_role_id, status, rgb):
        self.id = desk_id  # 1-2...
        self.desk_rfid = desk_rfid  # BA:65:D3:A1
        self.desk_role_id = desk_role_id  # 1 admin 2 user
        self.status = status  # 0 or 1
        self.rgb = rgb  # '0 255 255 200' led status, red, green, blue

    def __str__(self):
        return f"Desk ID: {self.id}, RFID: {self.desk_rfid}, Role ID: {self.desk_role_id}, Status: {self.status}, RGB: {self.rgb}"

    @classmethod
    def parse(cls, desk_dict):
        return cls(
            desk_dict["id"],
            desk_dict["desk_rfid"],
            desk_dict["desk_role_id"],
            desk_dict["status"],
            desk_dict["rgb"],
        )

    def serialize(self):
        return {
            "id": self.id,
            "desk_rfid": self.desk_rfid,
            "desk_role_id": self.desk_role_id,
            "status": self.status,
            "rgb": self.rgb,
        }
