# 练习  name_case.py   P42
# 2-3

name = "Eric"
print("Hello "+name+",would you like to learn some Python today")

# 2-4
name_1 = "Elf Dobby"
print(name_1.upper())
print(name_1.lower())
print(name_1.title())

# 2-5
idol = "Cap A"
words = "Avengers,assemble!"
print(idol+" once said:"+words)   # 淦，咋个加引号？！
print(f"{idol} once said:'{words}'!")   # 会加了！
# 2-6，见2-5（蛤）

# 2-7
name_2 = " Emma Watson "
print("\t"+name_2)
print("\n"+name_2)
print("\n\t"+name_2)
print(name_2.lstrip())
print(name_2.rstrip())
print(name_2.strip())
# 练习结束
# 字符串
age = 23
message = "Happy "+str(age)+"rd birthday"  # age-23为整数int变量，用str转化为字符串（string）
print(age)
print(message)

# 2-8
print(2+6)
print(10-2)
print(2*4)
print(64/8)

# 2-9
fav_number = 3.0   # 3.0 yyds
message = "My favorite number is "+str(fav_number)+"!"
print(message)

# 第三章
# 列表
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)
print(bicycles[0])   # 从零开始
print(bicycles[0].title())
print(bicycles[0].upper())
print(bicycles[-1])    # -1为倒数第一个
print(bicycles[-2])
message = "My first bicycle was a "+bicycles[0]+"."
print(message)

# 练习
# 3-1
names = ["DQ", "SH", "WYL", "WYN"]
print(names)

message = names[0]+" is my friend!"
print(message)
message = names[1]+" is my friend!"
print(message)
message = names[2]+" is my friend!"
print(message)
message = names[3]+" is my friend!"
print(message)
