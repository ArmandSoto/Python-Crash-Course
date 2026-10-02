from restaurant import Restaurant
from roles import User
from super_roles import Admin
from random import randint, choice


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


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Initialize attributes of parent class"""

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print("Available flavors:")

        for flavor in self.flavors:
            print(f"    {flavor}")


def f_6():
    ice_cream_stand = IceCreamStand(
        "3 Flavors",
        "Ice Cream",
        ["Vanilla", "Chocolate", "Cookie Dough"],
    )

    ice_cream_stand.show_flavors()


def f_7():

    admin = Admin("Riku", "Hacker", "r_hacker", "Baruch", "22")
    admin.show_privileges()


def f_8():
    admin = Admin("Riku", "Hacker", "r_hacker", "Baruch", "22")
    admin.privileges.show_privileges()


class Car:

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):

        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):

        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


def f_9():
    my_leaf = ElectricCar("nissan", "leaf", 2024)
    print(my_leaf.get_descriptive_name())
    my_leaf.battery.describe_battery()
    my_leaf.battery.get_range()

    print("---- Upgrade Battery Test ----")

    my_car = ElectricCar("porsche", "taycan", 2026)
    my_car.battery.get_range()
    my_car.battery.upgrade_battery()
    my_car.battery.get_range()


def f_10():
    restaurant = Restaurant("Le Food", "French")
    restaurant.describe_restaurant()


def f_11():
    admin = Admin("Riku", "Hacker", "r_hacker", "Baruch", "22")
    admin.privileges.show_privileges()


def f_12():
    admin = Admin("Riku", "Hacker", "r_hacker", "Baruch", "22")
    admin.privileges.show_privileges()


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(f"Result: {randint(1, self.sides)}")


def f_13():
    die_6 = Die()

    print("---- 6 Sided Rolls ----")

    for _ in range(10):
        die_6.roll_die()

    die_10 = Die(10)
    die_20 = Die(20)

    print("---- 10 Sided Rolls ----")

    for _ in range(10):
        die_10.roll_die()

    print("---- 20 Sided Rolls ----")
    for _ in range(10):
        die_20.roll_die()


def f_14():
    lottery = (16, 24, 98, 11, 54, 2, 63, 49, 22, 37, "A", "Z", "G", "B", "J")
    winning_ticket = []

    for _ in range(4):
        pick = choice(lottery)
        winning_ticket.append(pick)

    print("Any ticket matching these 4 numbers or letters wins a prize: ")
    print(winning_ticket)


def f_15():
    lottery = (16, 24, 98, 11, 54, 2, 63, 49, 22, 37, "A", "Z", "G", "B", "J")
    winning_ticket = []

    for _ in range(4):
        pick = choice(lottery)
        winning_ticket.append(pick)

    print(winning_ticket)

    # Buy tickets until winning ticket is matched, record information

    my_ticket = []
    attempts = 0
    is_winner = False

    while not is_winner:

        my_ticket = []

        attempts += 1

        for i in range(4):
            pick = choice(lottery)
            my_ticket.append(pick)

        # we have our ticket now we need to check to see if winner

        for i in range(4):
            if my_ticket[i] != winning_ticket[i]:
                is_winner = False
                break
            else:
                is_winner = True
                # to show that the ticket is the same as the wining ticket
                if i == 3:
                    print(my_ticket)

    print(f"The number of attempts: {attempts}")


def main():
    f_15()


if __name__ == "__main__":
    main()
