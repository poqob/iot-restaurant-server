# dht11.py

from typing import Dict


class DHT11:
    def __init__(self, temperature=0, humidity=0):
        self.temperature = temperature
        self.humidity = humidity

    @staticmethod
    def parse(dht_dict: Dict[str, int]) -> "DHT11":
        temperature = dht_dict.get("temperature", 0)
        humidity = dht_dict.get("humidity", 0)
        return DHT11(temperature, humidity)

    def serialize(self) -> Dict[str, int]:
        return {"temperature": self.temperature, "humidity": self.humidity}

    def serialize_for_parse(self) -> Dict[str, int]:
        return {"temperature": self.temperature, "humidity": self.humidity}

    def __str__(self) -> str:
        return f"Temperature: {self.temperature}°C, Humidity: {self.humidity}%"


if __name__ == "__main__":
    # Example usage:
    dht_dict = {"temperature": 25, "humidity": 60}
    dht_instance = DHT11.parse(dht_dict)
    print(dht_instance.serialize())
