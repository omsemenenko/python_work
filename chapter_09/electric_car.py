class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometr(self):
        print(f"This car has {self.odometr_reading} miles on it.")

    def update_odometr(self, mileage):
        if mileage >= self.odometr_reading:
            self.odometr_reading = mileage
        else:
            print("You can't roll back an odometer!")
        # self.odometr_reading = mileage

    def increment_odometer(self, miles):
        self.odometr_reading += miles

    def fill_gas_tank(self):
        print("This car has tank of 50 litres.")

class Battery():
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
         self.battery_size = 100


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(). __init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.fill_gas_tank()
# my_tesla.battery.get_range()

your_tesla = ElectricCar('tesla', 'model s', 2019)
your_tesla.battery.get_range()
your_tesla.battery.upgrade_battery()
your_tesla.battery.get_range()