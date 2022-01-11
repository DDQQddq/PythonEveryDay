# print(5/0)  达咩
import json

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Give me two number, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)


def count_number(name):
    try:
        with open(name, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {name} doesn't exist.")  # 或者使用 pass 静默失败
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {name} has about {num_words} words.")


filename = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for name in filename:
    count_number(name)

# 练习 10-6

num_1 = input('Enter the first numbers: ')
num_2 = input('Enter the second numbers: ')
try:
    num = int(num_1) + int(num_2)
    print(num)
except ValueError:
    print('Value Error')

number = [2, 3, 5, 7, 11, 13]

filename = 'number.json'
with open(filename, 'w') as f:
    json.dump(number, f)

with open(filename) as f:
    numbers = json.load(f)

print(numbers)

name = 'username.json'

try:
    with open(name) as n:
        username = json.load(n)
except FileNotFoundError:
    username = input("What's your name? ")
    with open(name, 'w') as n:
        json.dump(username, n)
        print(f"We will remember you when you back, {username.title()}.")

else:
    print(f"Welcome back, {username.title()}.")

verify = input(f"Are you {username}?(yes/no) ")
if verify != 'yes':
    real_name = input("Pls enter your name: ")
    with open(name, 'w') as user:
        json.dump(real_name, user)
        print(f"We will remember you when you back, {real_name.title()}.")

else:
    print(f"Welcome back again, {username.title()}.")
