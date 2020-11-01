class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 10

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

restaurant = Restaurant('oazis', 'ukrainian')
restaurant.set_number_served(25)
restaurant.served_number()

restaurant.increment_number_served(20)
restaurant.served_number()












# restaurant = Restaurant('oazis', 'ukrainian')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
#
# my_restaurant = Restaurant('paris', 'french')
# my_restaurant.describe_restaurant()
#
# your_resaurant = Restaurant('rome', 'italian')
# your_resaurant.describe_restaurant()