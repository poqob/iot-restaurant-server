from models.led import RGBLED
import requests


class EspApi:
    def color_change(self, led: RGBLED):
        url = "http://192.168.73.100:5951/color_change"
        res = str(led.serialize()).replace("'", '"')
        data = {"color": res}
        response = requests.post(url, data=data)
        print(response.text)

    def call_waiter(self, desk_id):
        url = "http://192.168.73.100:5951/call_waiter"
        data_waiter = {"desk_id": desk_id}
        response = requests.post(url, data=data_waiter)
        print(response.text)

    # attic = 0 or 1
    def attic(self, attic):
        url = "http://192.168.73.100:5951/attic"
        attic = {"attic": attic}
        response = requests.post(url, data=attic)
        print(response.text)
        return response.text

    def log(self):
        url = "http://192.168.73.100:5951/log"
        response = requests.get(url)
        print(response.text)
