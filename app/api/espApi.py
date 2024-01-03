from models.led import RGBLED
import aiohttp
import asyncio


class EspApi:
    async def color_change(self, led: RGBLED):
        url = "http://192.168.73.100:5951/color_change"
        res = str(led.serialize()).replace("'", '"')
        data = {"color": res}

        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as response:
                print(await response.text())

    async def call_waiter(self, desk_id):
        url = "http://192.168.73.100:5951/call_waiter"
        data_waiter = {"desk_id": desk_id}

        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data_waiter) as response:
                print(await response.text())

    # attic = 0 or 1
    async def attic(self, attic):
        url = "http://192.168.73.100:5951/attic"
        data_attic = {"attic": attic}

        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data_attic) as response:
                print(await response.text())
                return await response.text()

    async def log(self):
        url = "http://192.168.73.100:5951/log"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                print(await response.text())


# Example of using the asynchronous EspApi class
async def example_usage():
    esp_api = EspApi()
    await esp_api.attic(1)
    await esp_api.color_change(RGBLED(255, 0, 0))
    await esp_api.call_waiter("desk123")
    await esp_api.log()


# Run the example
asyncio.run(example_usage())
