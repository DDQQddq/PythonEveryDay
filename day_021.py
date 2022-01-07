# 练习8-9
def show_msg(mane, send):
    for ms in mane:
        print(ms)
        send.append(ms)
    print(mane)
    print(send)


msg = ['hello', 'hi', 'fine', 'ok']
sen = []
show_msg(msg, sen)


def make_pizza(*toppings):  # * 可以让python创建一个空元组，将所有的值封装到元组中
    print("\nMaking a pizza with the following toppings")
    for topping in toppings:
        print(f" - {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza1(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings")
    for topping in toppings:
        print(f" - {topping}")


make_pizza1(16, 'pepperoni')
make_pizza1(12, 'mushrooms', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info):  # ** 创造空字典
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
