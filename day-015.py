# 练习7-5
prompt = "\nCould you tell me how old are you?"
prompt += "\nSo I can tell how much the ticket is."

age = input(prompt)
age = int(age)
if age <= 3:
    print("You can enjoy the movie by free.")
elif age <= 12:
    print("You need to pay $10 to watch the movie.")
elif age > 12:
    print("You need to pay $15 to watch the movie.")

# 练习7-6
toppings = []
prompt = "\nTell me what toppings do you want?"
prompt += "\n(Enter 'quit' when  you finished.)"

topping = input(prompt)
while topping != 'quit':
    toppings.append(topping)
    topping = input(prompt)
    if topping == 'quit':
        break
print(toppings)

# 7-3
# 首先创建一个待验证用户列表，和一个用于储存已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户，直到没有未验证用户为止
# 将每个验证的用户都移到已验证的用户列表中
while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print(f"Verify user: {current_users.title()}")
    confirmed_users.append(current_users)

# 显示所有已验证的用户
print("\nThe following users have been confirm:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)
