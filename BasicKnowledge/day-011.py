# 练习
# 6-5
rivers = {'nile': 'egypt', 'rang': 'china', 'heng': 'india'}
for r, c in rivers.items():
    print(f"The {r.title()} runs through {c.title()}.")

for r in rivers.keys():
    print(r.title())

for c in rivers.values():
    print(c.title())

# 6-6
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'eward': 'ruby',
    'phil': 'python',
    }
oral_list = ['jen', 'john', 'sarah', 'eva', 'elf', 'eward', 'phil']
list_1 = []
for name in favorite_language.keys():
    list_1.append(name)
for name_1 in oral_list:
    if name_1 in list_1:
        print(f"Thank you,{name_1.title()}!")
    else:
        print(f"Please join the project in your earliest convenient,{name_1.title()}!")

# 嵌套
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
print(aliens)   # 有区别！

# 创建一个用于储存外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print('...')
# 显示创建了多少个外星人
print(f"Total number of aliens: {len(aliens)}.")

# 创建一个用于储存外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)    # 嵌套
# 修改前三个外星人
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print('...')

# 存储pizza的相关信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
    }
# 概述所点的pizza
print(f"You order a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print('\t' + topping)

# 究极套娃
users = {
    'einstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'curie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation：{location.title()}")
