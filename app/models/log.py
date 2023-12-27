from models.dht11 import DHT11


class Log:
    def __init__(self, dht_dict, attic, rain):
        self.dht = DHT11.parse(dht_dict)
        self.attic = attic
        self.rain = rain

    def serialize(self):
        return {
            "dht": self.dht.serialize(),
            "attic": self.attic,
            "rain": self.rain,
        }

    @staticmethod
    def parse(log_dict) -> "Log":
        dht_dict = log_dict.get("dht", {})
        attic = log_dict.get("attic", False)
        rain = log_dict.get("rain", False)
        return Log(dht_dict=dht_dict, attic=attic, rain=rain)


if __name__ == "__main__":
    # Code within this block will only run if the script is executed directly
    instance = Log(
        dht_dict={"temperature": 25, "humidity": 60},
        attic=False,
        rain=False,
    )

    json = instance.serialize()

    instance2 = Log.parse(json)

    print(instance2.serialize())
