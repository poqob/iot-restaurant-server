# role.py: model for role
class Role:
    def __init__(self, user_id, role_name):
        self.id = user_id
        self.role_name = role_name

    def __str__(self):
        return f"User ID: {self.id}, Role Name: {self.role_name}"

    @classmethod
    def parse(cls, role_dict):
        return cls(role_dict["id"], role_dict["role_name"])

    def serialize(self):
        return {"id": self.id, "role_name": self.role_name}


if __name__ == "__main__":
    role_dict = {"id": 1, "role_name": "admin"}
    role_instance = Role.parse(role_dict)
    print(role_instance.serialize())
