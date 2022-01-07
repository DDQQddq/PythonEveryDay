age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is {price}.")

age = 86
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is {price}.")

age = 86
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is {price}.")

requested_topping = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_topping:
    print("Adding mushrooms.")
if "pepperoni" in requested_topping:
    print("Adding pepperoni.")
if "extra cheese" in requested_topping:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

# 练习
# 5-3
alien_color = "red"
if alien_color == "green":
    print("Congratulations!5 points!")

alien_color = "green"
if alien_color == "green":
    print("Congratulations!5 points!")

# 5-4
alien_color = "green"
if alien_color == "green":
    print("Congratulations!5 points!")
else:
    print("Congratulations!10 points!")

alien_color = "red"
if alien_color == "green":
    print("Congratulations!5 points!")
else:
    print("Congratulations!10 points!")

# 5-5
alien_color = "green"
if alien_color == "green":
    print("Congratulations!5 points!")
elif alien_color == "yellow":
    print("Congratulations!10 points!")
else:
    print("Congratulations!15 points!")

alien_color = "red"
if alien_color == "green":
    print("Congratulations!5 points!")
elif alien_color == "yellow":
    print("Congratulations!10 points!")
else:
    print("Congratulations!15 points!")

alien_color = "yellow"
if alien_color == "green":
    print("Congratulations!5 points!")
elif alien_color == "yellow":
    print("Congratulations!10 points!")
else:
    print("Congratulations!15 points!")

# 5-6
# age = int(input("请输入年龄："))    # input 输入为字符串 string ,若比较，需转化为int
age = 88
if age < 2:
    print("A cute bobby!")
elif age < 4:
    print("A cute child!")
elif age < 13:
    print("A lovely kid!")
elif age < 20:
    print("A young man!")
elif age < 65:
    print("A truly man!")
else:
    print("A old man!")

fruits = ["apple", "pear", "peach"]
if "apple" in fruits:
    print("Apple is in the list!")
if "pineapple" in fruits:
    print("Pineapple is in the list!")

requested_toppings = ["mushroom", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry,we are out of green peppers right now!")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ["mushrooms", "olives", "green peppers",
                      "pepperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping.title()}.")
    else:
        print(f"Sorry,we don't have {requested_topping.title()}.")
print("\nFinished making your pizza!")
