filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('I love programming!\n')
    file_object.write('I love creating new games!\n')

# 读取模式 r 一般省略
# 写入模式 w
# 附加模式 a
# 读写模式 r+

with open(filename, 'a') as file_object:
    file_object.write('I also love finding meaning in large datasets!\n')
    file_object.write('I love creating apps that can run in browser!\n')

# 练习 10-3

guess = 'guess.txt'

name = input("Pls enter your name: ")
with open(guess, 'w') as guess_name:
    guess_name.write(name.title())

# 练习 10-4

guest_book = 'guest_book.txt'

guest = ''
with open(guest_book, 'w') as book_object:
    while guest != 'quit':
        guest = input("Pls enter you name(enter 'quit' to quit the program): ")
        if guest != 'quit':
            guest += '\n'
            book_object.write(guest.title())
            print(f"Welcome!{guest.title().rstrip()}")

# 练习 10-5

programming = 'love_programming.txt'
reason = ''
print("Enter the reason why you love programming: ")
with open(programming, 'a') as pro:
    while reason != 'quit':
        reason = input("Enter the reason why you love programming: ")
        pro.write(f"{reason}\n")
