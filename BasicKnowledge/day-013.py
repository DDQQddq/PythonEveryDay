print(4 % 3)
# 求模运算符

number = input("Enter a number,and I will tell you if it's even or odd:")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

# 练习
# 7-1
car = input("Which car would you like to buy?")
print(f"Let me see if I can find you a {car.title()}.")

# 7-2
number = input("How many people will come here to dinner?")
number = int(number)
if number >= 8:
    print("Sorry,there is not enough table to use.")
else:
    print("Enjoy your party later!")

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something,and I will repeat back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
