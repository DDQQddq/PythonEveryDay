class Car:

    def __init__(self, make, model, year):
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

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def upgrade_battery(self, odi=100):
        if self.battery_size != 100:
            self.battery_size = odi

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range0 = 260
        else:
            range0 = 315
        print(f"This car can go about {range0} miles on a full charge.")


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)
my_pen = ElectricCar('pen', 'e3', '2021')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_pen.battery.describe_battery()

# 练习 9-6


class Restaurant:

    def __init__(self, name, c_type):
        self.name = name
        self.c_type = c_type

    def describe_restaurant(self):
        print(f"The restaurant is called {self.name},and it's a {self.c_type} restaurant.")

    @staticmethod
    def open_restaurant():
        print("The restaurant is open.")


class IceCreamStand(Restaurant):

    def __init__(self, name, c_type):
        super().__init__(name, c_type)
        self.flavors = ['red', 'yellow', 'green']

    def describe_flavors(self):
        flavors = self.flavors
        for kind in flavors:
            print(kind)


DQ = IceCreamStand('dq', 'nb')
DQ.describe_flavors()
DQ.flavors = ['red']
DQ.describe_flavors()

# 练习 9-7


class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"First name: {self.first_name.title()} Last name: {self.last_name.title()}")

    def greet_user(self):
        print(f"Welcome {self.first_name.title()} {self.last_name.title()}")


class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privilege(self):
        privileges = self.privileges
        for pri in privileges:
            print(pri.title())


elf = Admin('elf', 'dobby')
elf.show_privilege()
