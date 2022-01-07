alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']   # 永久消失！
print(alien_0)

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'eward': 'ruby',
    'phil': 'python',
    }
language = favorite_language['sarah']
print(f"Sarah's favorite language is {language}")

# 使用 get() 访问值
alien_0 = {'color': 'green', 'points': 5}
point_value = alien_0.get('point', 'No point value assigned.')
print(point_value)

# 练习
# 6-1
person = {'first_name': 'qun',
          'last_name': 'dong',
          'age': 18,
          'city': 'jc',
          }
print(person)

# 6-2
number = {'DQ': 3.0, 'WYL': 5, 'SH': 6, 'MX': 24, 'WYN': 73}
print(number)
# print(f"\nD's favorite number is {number['DQ']}")
# print(f"\nWeyl's favorite number is {number['WYL']}")
# print(f"\nShe's favorite number is {number['SH']}")
# print(f"\nMax's favorite number is {number['MX']}")
# print(f"\nWyn's favorite number is {number['WYN']}")
# 更简洁的方法！
for k, v in number.items():
    print(f"\n{k}'s favorite number is {v}")

user_0 = {
    'username': 'Fermi',
    'first': 'enrico',
    'last': 'fermi'
    }
for key, value in user_0.items():
    print(f"\nKey:{key}")
    print(f"Value:{value}")

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'eward': 'ruby',
    'phil': 'python',
    }
for name, language in favorite_language.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}")

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'eward': 'ruby',
    'phil': 'python',
    }
for name in favorite_language.keys():
    print(name.title())

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'eward': 'ruby',
    'phil': 'python',
    }
friends = ['phil', 'sarah']
for name in favorite_language.keys():
    print(f"Hi {name.title()}")
    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()},I see you love {language}.")
