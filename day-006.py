# 练习
# 4-10
pets = ["dog", "clip", "bear", "boat", "one good"]
for pet in pets:
    print(f"A {pet.title()} would make a great pet!\n")
print("Any of these animals would make a great pet!")
print("The first three items in the list are:")
print(pets[:3])
print("Three items from the middle of the list are:")
print(pets[1:4])
print("The last three items in the list are:")
print(pets[-3:])

# 4-11， 4-12 略
# 元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)   # 重新赋值
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# 4-13

foods = ("water", "rice", "ham", "milk", "leaf")
for food in foods:
    print(food)
foods = ("water", "rice", "ham", "tea", "bread")
for food in foods:
    print(food)

# 第五章 if 语句 nice!
cars = ["audi", "bmw", "subaru", "benz"]
for car in cars:
    if car == "bmw":   # : 莫忘
        print(car.upper())
    else:
        print(car.title())
requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("Hold the anchovies!")

answer = 17
if answer != 42:
    print("That is not the correct answer.Please try again!")

banned_users = ["andrew", "caroline", "david"]
user = "marie"
if user not in banned_users:
    print(f"{user.title()},you can post a response if you wish.")
user = "andrew"
if user in banned_users:
    print(f"{user.title()},you can't post any response!")

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry,you are too young to vote!")
    print("Please register to vote as soon as you turn 18!")

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
