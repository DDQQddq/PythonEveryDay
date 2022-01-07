#  操作列表
magicians = ["alice", "david", "carolina"]
for magician in magicians:    # 莫忘 ：
    print(magician)
    print(magician.title())

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()},that was a great trick!")
    print(f"I can't wait to see your next trick,{magician.title()}.\n")

print("Thank you,everyone.That was a great magic show!")

# 练习
# 4-1
planets = ["yang", "bai", "liu", "lian"]
for planet in planets:
    print(f"I like {planet.title()} tree!\n")

print("I really love planets!")

# 4-2
pets = ["dog", "clip", "bear", "boat"]
for pet in pets:
    print(f"A {pet} would make a great pet!\n")
print("Any of these animals would make a great pet!")

# 创建数值列表
for value in range(1, 5):   # 并不会打印 5
    print(value)
for value in range(6):     # 从 0 开始打印至 5
    print(value)

number = list(range(1, 6))
print(number)

even_number = list(range(2, 11, 2))   # 指定步长为 2
print(even_number)      # [2, 4, 6, 8, 10]

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)    # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# or
squares = []
for value in range(1, 11):
    squares.append(value ** 2)   # 少了一行，nice
print(squares)

# or
squares = [value ** 2 for value in range(1, 11)]   # 称为列表解析 nb!
print(squares)    # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 练习
# 4-3
for value in range(1, 21):
    print(value)

# 4-4
for value in range(1, 1_000_001):
    print(value)   # 太草了！

# 4-5
lists = []
for value in range(1, 1_000_001):
    lists.append(value)
print(min(lists))  # 最小值
print(max(lists))  # 最大值
print(sum(lists))  # 求和
# or
lists = [value for value in range(1, 1_000_001)]
print(sum(lists))   # 更简洁！nice!

# 4-6
list_1 = []
for value in range(1, 20, 2):    # 步长为2
    list_1.append(value)
print(list_1)
for value in list_1:
    print(value)

# 4-7
list_1 = []
for value in range(3, 31, 3):
    list_1.append(value)
print(list_1)
for value in list_1:
    print(value)

# 4-8
aha = []
for value in range(1, 11):
    aha.append(value ** 3)
print(aha)

# 4-9 列表解析
aha = [value ** 3 for value in range(1, 11)]
print(aha)

# 4-4 切片

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])
print(players[:4])   # 默认从 0 开始
print(players[2:])   # 在末尾结束
print(players[-3:])  # 从倒数第三个开始

players = ["charles", "martina", "michael", "florence", "eli"]
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ["pizza", "water", "cake"]
friend_foods = my_foods[:]   # 省略起始索引和终止索引，复制列表
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
