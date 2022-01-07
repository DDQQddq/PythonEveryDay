def get_formatted_name(first_name, last_name):
    """返回整洁的名字"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print(f"\nPlease tell me your name:")
    print("(enter 'q' at any time to quit.)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name.title()}")


# 练习8-6
def city_country(city, country):
    """输出地名和国家"""
    c_c = f"{city} {country}"
    return c_c.title()


while True:
    print("Tell me where are you from please,your city and your country?")
    print("(enter 'q' at any time to quit.)")
    ci = input("Which city are you live now?")
    if ci == 'q':
        break
    co = input("Where are you from?")
    if co == 'q':
        break
    c_1 = city_country(ci, co)
    print(c_1)


# 练习8-7
def make_album(name, album):
    """m描述音乐专辑"""
    al = {'name': name, 'album': album}
    return al


musician = make_album('mo', 'fate')
print(musician)
while True:
    print("Tell me the musician of the album.")
    print("And tell me the name of album.")
    print("(enter 'q' to quit the program.)")
    name1 = input('Name: ')
    if name1 == 'q':
        break
    album1 = input('Album: ')
    if album1 == 'q':
        break

    musician1 = make_album(name1, album1)
    print(musician1)
