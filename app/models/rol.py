class Role
    def __init__(self, user_id, role_name):
        self.id = user_id
        self.role_name = role_name

    def __str__(self):
        return f'User ID: {self.id}, Role Name: {self.role_name}'
