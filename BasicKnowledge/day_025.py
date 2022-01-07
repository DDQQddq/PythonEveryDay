class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"First name: {self.first_name.title()} Last name: {self.last_name.title()}")

    def greet_user(self):
        print(f"Welcome {self.first_name.title()} {self.last_name.title()}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


dq = User('elf', 'dobby')
dq.increment_login_attempts()
print(dq.login_attempts)
dq.increment_login_attempts()
print(dq.login_attempts)
dq.increment_login_attempts()
print(dq.login_attempts)

dq.reset_login_attempts()
print(dq.login_attempts)

# 继承


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


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")


my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
