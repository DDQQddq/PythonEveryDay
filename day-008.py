# 练习
# 5-8
names = ["DQ", "WYL", "SH", "admin", "WYB", "ZQA"]
for name in names:
    if name == "admin":
        print("Hello admin,would you like to see a status reports?")
    else:
        print(f"Hello {name},thank you for logging again!")
a = 1
while a <= 6:    # 代码精简完成
    del names[0]
    a = a+1
print(names)
if names:
    for name in names:
        print(f'Welcome,{name}.')
else:
    print("We need to find some users!")

# 5-10
current_users = ["DQ", "WYL", "SH", "ZQA", "WYB", "XSZ"]
new_users = ["LY", "MX", "WYN", "WYL", "ZQA"]
for user in new_users:
    if user in current_users:
        print(f"Please try another name,{user}!")
    else:
        print(f"This name is allowed,{user}!")
current_users_1 = []
for name in current_users:
    name = name.lower()
    current_users_1.append(name)
print(current_users_1)
for user in new_users:
    if user.lower() in current_users:
        print(f"Please try another name,{user}!")
    else:
        print(f"This name is allowed,{user}!")

# 5-11
number = []
for value in range(1, 10):
    number.append(value)
print(number)
for value in number:
    if value == 1:
        print(f"{value}st")
    elif value == 2:
        print(f"{value}nd")
    elif value == 3:
        print(f"{value}rd")
    else:
        print(f"{value}th")

# 第六章 字典
alien_0 = {'color': 'green', 'points': 5}  # 一系列键值对，color键，green值
print(alien_0['color'])
print(alien_0['points'])

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f'You just earned {new_points} points!')

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


alien_0 = {'color': 'green'}
print(f'The alien is {alien_0["color"]}')
alien_0['color'] = 'yellow'
print(f'The alien is {alien_0["color"]}')

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f'Original x_position: {alien_0["x_position"]}')
# 向右移动外星人
# 根据当前速度确定将外星人向右移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人速度很快
    x_increment = 3
# 新位置为旧位置加上移动距离
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f'New x_position:{alien_0["x_position"]}')
