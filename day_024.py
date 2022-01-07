class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        print(long_name.title())

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_car = Car('audi', 'a4', 2019)
my_car.get_descriptive_name()
my_car.read_odometer()

my_car.odometer_reading = 23     # 直接修改属性的值
my_car.read_odometer()

my_car.update_odometer(65_500)   # 变量赋值
my_car.read_odometer()


class Restaurant:

    def __init__(self, name, c_type):
        self.name = name
        self.c_type = c_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant is called {self.name},and it's a {self.c_type} restaurant.")

    def number(self):
        print(f"{self.number_served} people have(has) dinner in the restaurant.")


restaurant = Restaurant('kdj', 'quick')
restaurant.number()
restaurant.number_served = 23
restaurant.number()
