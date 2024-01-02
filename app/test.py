from models.log import Log
from models.dht11 import DHT11
from api.espApi import EspApi
from models.led import RGBLED

# Code within this block will only run if the script is executed directly
instance = Log(
    dht_dict={"temperature": 25, "humidity": 60},
    attic=False,
    rain=False,
)

json = instance.serialize()
print(json)
instance2 = Log.parse(json)
print(instance2.serialize())

api = EspApi()
ledd = RGBLED(status=1, red=255, green=0, blue=0)
api.color_change(ledd)
api.attic(1)
api.call_waiter("rfid")
api.log()

# log.serialize=> {'dht': {'temperature': 25, 'humidity': 60}, 'attic': False, 'rain': False}
# log.parse({'dht': {'temperature': 25, 'humidity': 60}, 'attic': False, 'rain': False}) -> Log
