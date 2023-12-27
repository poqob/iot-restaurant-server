from models.log import Log
from models.dht11 import DHT11

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

# log.serialize=> {'dht': {'temperature': 25, 'humidity': 60}, 'attic': False, 'rain': False}
# log.parse({'dht': {'temperature': 25, 'humidity': 60}, 'attic': False, 'rain': False}) -> Log
