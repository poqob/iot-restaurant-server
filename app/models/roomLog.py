from dht11 import DHT11
from led import RGBLED

class RoomLog:
    def __init__(self, room_id, dht_dict, led_dict):
        self.room_id = room_id
        self.dht = DHT11.parse(dht_dict)
        self.rgbled = RGBLED.parse(led_dict)

    def serialize(self):
        return {'room_id': self.room_id, 'dht11': self.dht.serialize(), 'led': self.rgbled.serialize()}

    @staticmethod
    def parse(room_log_dict):
        room_id = room_log_dict.get('room_id', 0)
        dht_dict = DHT11.parse(room_log_dict.get('dht11', {}))
        led_dict = RGBLED.parse(room_log_dict.get('led', {}))
        return RoomLog(room_id, dht_dict, led_dict)

if __name__ == "__main__":
    # Code within this block will only run if the script is executed directly
    room_log_instance = RoomLog(room_id=1, dht_dict={'temperature': 25, 'humidity': 60}, led_dict={'status': True, 'red': 255, 'green': 0, 'blue': 0})

    # Serialize RoomLog object to dictionary
    serialized_room_log = room_log_instance.serialize()
    print(serialized_room_log)

    # Parse the dictionary back to a RoomLog object
    parsed_room_log = RoomLog.parse(serialized_room_log)
    print(parsed_room_log.serialize())

