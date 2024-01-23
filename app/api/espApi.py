# espApi.py is used to communicate with the esp8266 server.
from models.led import RGBLED
import requests


class EspApi:
    def color_change(self, led: RGBLED):
        url = "http://192.168.73.100:5951/color_change"
        res = str(led.serialize()).replace("'", '"')
        data = {"color": res}
        response = requests.post(url, data=data)
        return response.text

    def call_waiter(self, desk_id):
        url = "http://192.168.73.100:5951/call_waiter"
        data_waiter = {"desk_id": desk_id}
        response = requests.post(url, data=data_waiter)
        return response.text

    # data includes attic: 0-1, desk_rfid: string
    def attic(self, data):
        url = "http://192.168.73.100:5951/attic"
        response = requests.post(url, data=data)
        return response.text

    # data includes attic: 0-1, desk_rfid: string
    def automatic_attic(self, data):
        url = "http://192.168.73.100:5951/automatic_attic"
        response = requests.post(url, data=data)
        return response.text

    def log(self):
        url = "http://192.168.73.100:5951/log"
        response = requests.get(url)
        print(response.text)
        return response.text
