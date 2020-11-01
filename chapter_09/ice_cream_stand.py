class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 10
        self.flavors = ['vanilla', 'cream brulea', 'fruits']

    def get_flavors(self):
        print(self.flavors)

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()}")
        print(f"{self.cuisine_type}")

    def served_number(self):
        print(f"We served {self.number_served} guests today.")

    def set_number_served(self, guest):
        self.number_served = guest

    def increment_number_served(self, serveses):
        self.number_served += serveses

    def open_restaurant(self):
        print("Restaurant is open!")

restaurant = Restaurant('oasis', 'ukrainian')
restaurant.get_flavors()



