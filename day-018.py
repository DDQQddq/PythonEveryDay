def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:  # python将非空字符串解读为True
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


def build_person(first_name, last_name):
    """返回一个字典，其中包含一个人的有关信息"""
    person = {'first': first_name, 'last': last_name}
    return person


musician = person_1 = build_person('jimi', 'hendrix')
print(musician)


def build_persson_1(first_name, last_name, age=None):
    """返回一个字典，其中包含一个人的有关信息"""
    person1 = {'first': first_name, 'last': last_name}
    if age:
        person1['age'] = age
    return person1


musician = build_persson_1('jimi', 'hendrix', age=27)
print(musician)
