class RGBLED:
    def __init__(self, status=False, red=0, green=0, blue=0):
        self.status = status
        self.red = red
        self.green = green
        self.blue = blue

    @staticmethod
    def parse(led_dict):
        status = led_dict.get("status", False)
        red = led_dict.get("red", 0)
        green = led_dict.get("green", 0)
        blue = led_dict.get("blue", 0)
        return RGBLED(status, red, green, blue)

    def __str__(self):
        return f'Status: {"On" if self.status else "Off"}, RGB: ({self.red}, {self.green}, {self.blue})'

    def serialize(self):
        return {
            "status": int(self.status),
            "red": self.red,
            "green": self.green,
            "blue": self.blue,
        }


# Example usage:
if __name__ == "__main__":
    led_dict = {"status": True, "red": 255, "green": 0, "blue": 0}
    led_instance = RGBLED.parse(led_dict)
    print(led_instance.serialize())
