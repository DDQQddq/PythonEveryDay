def greet_users(names):
    """问候"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


# 修改列表
# 常规无函数版本
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Print model : {current_design}")
#     completed_models.append(current_design)
# print("\nThe following models have been printed: ")
# for c_m in completed_models:
#     print(c_m)


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Print model : {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for c_m in completed_models:
        print(c_m)


unprinted_design = ['phone case', 'robot pendant', 'dodecahedron']
completed_model = []
print_models(unprinted_design[:], completed_model)
show_completed_models(completed_model)
print_models(unprinted_design, completed_model)
show_completed_models(completed_model)
