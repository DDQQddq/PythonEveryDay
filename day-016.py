responses = {}   # 字典为{}，而不是【】
# 设置一个标志，指出调查是否继续
polling_active = True
while polling_active:   # 提出输入被调查者的名字和回答
    name = input("\nWhat's your name?")
    response = input("Which mountain would you like to climb someday?")
    # 将回答储存在字典中
    responses[name] = response
    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        polling_active = False
# 调查结果，显示结果
print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name.upper()} would like to climb {response.title()}.")

# 联系7-8
sandwich_orders = ["s_1", "s_2", "s_3"]
finished_sandwiches = []
for s_0 in sandwich_orders:
    print(f"I made your {s_0} sandwich.")
while sandwich_orders:
    s = sandwich_orders.pop()
    finished_sandwiches.append(s)
finished_sandwiches = sorted(finished_sandwiches)
print("I made them all!")
print(finished_sandwiches)

# 练习7-9
# 练习7-10
results = {}
active = True
while active:
    name_1 = input("\nWhat's your name?")
    prompt = input("\nIf you could visit one place in the world,where would you go?")
    results[name_1] = prompt
    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == "no":
        active = False
print("\n---RESULT---")
for name_1, prompt in results.items():
    print(f"{name_1.upper()} want to visit {prompt.title()}")
