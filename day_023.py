class Dog:
    """dog"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over.")


my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()


class Restaurant:

    def __init__(self, name, c_type):
        self.name = name
        self.c_type = c_type

    def describe_restaurant(self):
        print(f"The restaurant is called {self.name},and it's a {self.c_type} restaurant.")

    @staticmethod
    def open_restaurant():
        print("The restaurant is open.")


hls = Restaurant('hls', 'quick')
hls.describe_restaurant()
hls.open_restaurant()

mdl = Restaurant('mdl', 'quick')
mdl.describe_restaurant()
kdj = Restaurant('kdj', 'quick')
kdj.describe_restaurant()


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"First name: {self.first_name.title()} Last name: {self.last_name.title()}")

    def greet_user(self):
        print(f"Welcome {self.first_name.title()} {self.last_name.title()}")


dq = User('elf', 'dobby')
dq.describe_user()
dq.greet_user()
mx = User('xiao', 'ma')
mx.describe_user()
mx.greet_user()


