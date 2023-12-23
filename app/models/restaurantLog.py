class RestaurantLog:
    def __init__(self, attic):
        self.attic = attic

    def serialize(self):
        return {"attic": self.attic}

    @staticmethod
    def parse(restaurant_log_dict):
        attic = restaurant_log_dict.get("attic", 0)
        return RestaurantLog(attic)
