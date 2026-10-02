"""A base module for any type of user"""


class User:
    def __init__(self, first_name, last_name, username, school, age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.school = school
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Username: {self.username}")
        print(f"School: {self.school}")
        print(f"Age: {self.age}")

    def greet_user(self):
        print(f"Welcome {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
