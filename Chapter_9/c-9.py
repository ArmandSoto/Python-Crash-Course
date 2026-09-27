class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print("Restaurant Now Open!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def print_number_served(self):
        print(
            f"{self.restaurant_name} has served  "
            f"{self.number_served} customers"
        )

    def increment_number_served(self, customers):
        self.number_served += customers


def f_1():
    r1 = Restaurant("Le Food", "French")
    r1.describe_restaurant()
    r1.open_restaurant()


def f_2():
    r1 = Restaurant("Le Food", "French")
    r2 = Restaurant("A Fooda Pizza", "Italian")
    r3 = Restaurant("Los Rice", "Spanish")

    r1.describe_restaurant()
    r2.describe_restaurant()
    r3.describe_restaurant()


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


def f_3():
    user_1 = User("Joe", "Shmo", "j_shmo", "Baruch", 21)
    user_2 = User("Jane", "Lawson", "j_lawson", "City", 26)

    user_1.greet_user()
    user_1.describe_user()

    print("-----------------------------------------")

    user_2.greet_user()
    user_2.describe_user()


def f_4():
    restaurant = Restaurant("Le Food", "French")
    restaurant.print_number_served()

    restaurant.number_served = 20
    restaurant.print_number_served()

    restaurant.set_number_served(45)
    restaurant.print_number_served()

    restaurant.increment_number_served(15)
    restaurant.print_number_served()


def f_5():
    user_1 = User("Joe", "Shmo", "j_shmo", "Baruch", 21)

    print(f"{user_1.login_attempts}")

    user_1.increment_login_attempts()
    user_1.increment_login_attempts()
    print(f"{user_1.login_attempts}")

    user_1.reset_login_attempts()
    print(f"{user_1.login_attempts}")


def main():
    f_5()


if __name__ == "__main__":
    main()
