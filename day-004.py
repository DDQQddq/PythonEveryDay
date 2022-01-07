#  补充
first_name = "ade"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"   # f format的简写（？），
print(full_name)
print(f"Hello,{full_name.title()}!")

message = f"Hello,{full_name.title()}!"
print(message)     # NB

motors = ["honda", "yamaha", "suzuki"]
print(motors)

popped_motors = motors.pop()    # 弹出尾部的值，并赋值给变量
print(motors)
print(popped_motors)

motors = ["honda", "yamaha", "suzuki"]
last_owned = motors.pop()
print(f"The last motor I owned was a {last_owned.title()}!")

motors = ["honda", "yamaha", "suzuki"]
last_owned = motors.pop(0)     # 弹出第一个元素
print(motors)
print(f"The last motor I owned was a {last_owned.title()}!")

motors = ["honda", "yamaha", "suzuki", "lua"]
print(motors)
motors.remove("lua")   # 根据值删除元素
print(motors)

motors = ["honda", "yamaha", "suzuki", "lua"]
print(motors)
too_expensive = "lua"
motors.remove(too_expensive)
print(motors)
print(f"\nA {too_expensive.title()} is too expensive for me!")

# 练习
# 3-4
list_1 = ["DQ", "WYL", "SH", "WYN"]
message = f"I want to invite {list_1[0]} to the dinner!"
print(message)
message = f"I want to invite {list_1[1]} to the dinner!"
print(message)
message = f"I want to invite {list_1[2]} to the dinner!"
print(message)
message = f"I want to invite {list_1[3]} to the dinner!"
print(message)

# 3-5
list_1 = ["DQ", "WYL", "SH", "WYN"]
message = f"I want to invite {list_1[0]} to the dinner!"
print(message)
message = f"I want to invite {list_1[1]} to the dinner!"
print(message)
message = f"I want to invite {list_1[2]} to the dinner!"
print(message)
message = f"I want to invite {list_1[3]} to the dinner!"
print(message)
print(f"But {list[3]} is too busy to attend the party!")

del list_1[3]
list_1.append("MX")
print(list_1)
message = f"I want to invite {list_1[0]} to the dinner!"
print(message)
message = f"I want to invite {list_1[1]} to the dinner!"
print(message)
message = f"I want to invite {list_1[2]} to the dinner!"
print(message)
message = f"I want to invite {list_1[3]} to the dinner!"
print(message)

# 3-6
print(f"I got a bigger table!")
list_1.insert(0, "WYB")
list_1.insert(3, "ZL")
list_1.append("ZQA")
print(list)
message = f"I want to invite {list_1[0]} to the dinner!"
print(message)
message = f"I want to invite {list_1[1]} to the dinner!"
print(message)
message = f"I want to invite {list_1[2]} to the dinner!"
print(message)
message = f"I want to invite {list_1[3]} to the dinner!"
print(message)
message = f"I want to invite {list_1[4]} to the dinner!"
print(message)
message = f"I want to invite {list_1[5]} to the dinner!"
print(message)
message = f"I want to invite {list_1[6]} to the dinner!"
print(message)

# 3-7
print("Oops!Only two people could attend the party!")
popped_name = list_1.pop(2)
print(f"I'm sorry to tell you that the party is cancelled，{popped_name}.")
popped_name = list_1.pop(2)     # 已经删完了，列表已变，一直弹出2就可
print(f"I'm sorry to tell you that the party is cancelled，{popped_name}.")
popped_name = list_1.pop(2)
print(f"I'm sorry to tell you that the party is cancelled，{popped_name}.")
popped_name = list_1.pop(2)
print(f"I'm sorry to tell you that the party is cancelled，{popped_name}.")
popped_name = list_1.pop(2)
print(f"I'm sorry to tell you that the party is cancelled，{popped_name}.")
print(list_1)
message = f"Welcome to my party,{list_1[0]}!"
print(message)
message = f"Welcome to my party,{list[1]}!"
print(message)

del list_1[0]
print(list_1)
del list_1[0]
print(list_1)

# 组织列表
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()    # sort 按字母顺序永久排序
print(cars)

cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse=True)      # 传递 reverse=True 参数，反向排序（永久）
print(cars)

cars = ["bmw", "audi", "toyota", "subaru"]
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list；")
print(sorted(cars))   # 实测 cars.sorted 无效（why）  sorted 临时排序
print(sorted(cars, reverse=True))   # 传递参数 reverse=True 反向排序
print("\nHere is the original list again:")
print(cars)

cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
cars.reverse()   # 倒着打印列表，再次使用可恢复
print(cars)

# cars = ["bmw", "audi", "toyota", "subaru"]
# len(cars)    # 列表长度  4

# 练习
# 3-8
place = ["BJ", "NJ", "CD", "QD", "DL"]
print(place)
print(sorted(place))
print(place)
print(sorted(place, reverse=True))
print(place)
place.reverse()
print(place)
place.reverse()
print(place)

place.sort()
print(place)
place.sort(reverse=True)
print(place)

# 3-9,3-10 （略）
