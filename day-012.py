# 练习
# 6-7
persons = {
    'person_1': {
        'first_name': 'qun',
        'last_name': 'dong',
        'age': 17,
        'city': 'jc',
          },
    'person_2': {
        'first_name': 'yl',
        'last_name': 'wu',
        'age': 19,
        'city': 'jc',
        },
    'person_3': {
        'first_name': 'xn',
        'last_name': 'dong',
        'age': 17,
        'city': 'jc'
        }
    }
for p, info in persons.items():
    print(f"\nUsername: {p}")
    full_name = f"{info['first_name']} {info['last_name']}"
    age = info['age']
    location = info['city']
    print(f"\tName: {full_name.title()}")
    print(f"\tAge：{age}")
    print(f"\tCity: {location.title()}")

# 第七章
message = input("Tell me something,and I will repeat back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"Hello,{name}")

prompt = "If you tell me who you are, I can personalize the message you see."
prompt += "\nWhat is your first name?"
name = input(prompt)
print(f"Hello, {name}")

height = input("How tall are you,in inches?")
height = int(height)
if height >= 48:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
