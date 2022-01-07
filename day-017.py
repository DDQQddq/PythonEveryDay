# 第八章 函数
def greet_user(username):
    """显示问候语"""  # 文档字符串的注释，三引号
    print(f"Hello,{username.title()}!")


greet_user('dq')


def display_massage(content):
    """学习内容"""
    print(f"We will learn {content} in this chapter.")


display_massage("函数")


def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(pet_name='harry', animal_type='hamster')


# 练习8-3
def make_shirt(size, pics):
    """制作T恤"""
    print(f"\nThe T-shirt's size is {size}.")
    print(f"And the pic you want to print is {pics.title()}")


make_shirt('L', 'sak')


# 练习8-4


def make_shirt_1(size, pics='I love Python.'):
    """制作T恤1"""
    print(f"\nThe size of the T-shirt is {size}.")
    print(f"The pics of the T-shirt is {pics}.")


make_shirt_1('L')
make_shirt_1('M')
make_shirt_1('M', 'GET IT!')


# 练习8-5


def describe_city(city, country):
    """城市与国家"""
    print(f"{city.title()} is in {country.title()}.")


describe_city('beijing', 'china')


def get_formatted_name(first_name, last_name):
    """返回整洁的名字"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


def get_formatted_name_1(first_name, middle_name, last_name):
    """返回整洁的名字"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musician = get_formatted_name_1('john', 'lee', 'hooker')
print(musician)
