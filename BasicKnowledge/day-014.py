prompt = "\nTell me something,and I will repeat back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)

    if message != "quit":   # 检查是否为quit
        print(message)

prompt = "\nTell me something,and I will repeat back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)

    if message == "quit":  # 可以用elif设置其他不符合的情况,来停止while循环,更简洁,更方便!
        active = False
    else:
        print(message)

prompt = "\nPlease enter a name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == "quit":
        break   # 使用break退出循环
    else:
        print(f"I'd love to go to {city.title()}.")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

x = 1
while x <= 5:
    x += 1  # 若漏掉这一行,就无限循环,可以ctrl+c停止,也可关闭窗口
    print(x)

# 练习7-4
toppings = []
prompt = "\nTell me what toppings do you want?"
prompt += "\n(Enter 'quit' when  you finished.)"

active = True
while active:
    topping = input(prompt)
    toppings.append(topping)
    if topping == 'quit':
        active = False
        toppings.remove('quit')
print(toppings)
