from roles import User

""" A module for special users """


class Admin(User):

    def __init__(self, first_name, last_name, username, school, age):
        """Initialize attributes of User Class"""

        super().__init__(first_name, last_name, username, school, age)

        self.privileges = Privileges(
            ["can add post", "can delete post", "can ban user"]
        )


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("---- Admin Privileges ----")
        for privilege in self.privileges:
            print(f"    {privilege}")
