# led.py: model for RGB LED
class RGBLED:
    def __init__(self, status=0, red=0, green=0, blue=0):
        self.status = status
        self.red = red
        self.green = green
        self.blue = blue

    @staticmethod
    def parse(led_dict):
        status = led_dict.get("status", 0)
        red = led_dict.get("red", 0)
        green = led_dict.get("green", 0)
        blue = led_dict.get("blue", 0)
        return RGBLED(status, red, green, blue)


    def serialize(self):
        return {
            "status": self.status,
            "red": self.red,
            "green": self.green,
            "blue": self.blue,
        }


# Example usage:
if __name__ == "__main__":
    led_dict = {"status": 1, "red": 255, "green": 0, "blue": 0}
    led_instance = RGBLED.parse(led_dict)
    print(led_instance.serialize())
