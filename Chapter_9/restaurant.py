class Restaurant:
    """A class used to represent a restaurant"""

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
