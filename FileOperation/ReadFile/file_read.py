filename = 'pi_digits.txt'
file_path = '/Users/elfdobby/pythonProject/FileOperation/pi_digits.txt'

with open(filename) as file_object:
    contents = file_object.read()
print(contents)
print(contents.rstrip())  # 删除末尾空行（感觉好像没有空行啊）


with open(file_path) as file_object:
    contents = file_object.read()
print(contents)

with open(filename) as file_object:
    for line in file_object:  # 逐行读取
        print(line)

with open(filename) as file_object:
    for line in file_object:  # 逐行读取
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

for line_1 in lines:
    print(line_1.rstrip())

pi_str = ''
for line_1 in lines:
    pi_str += line_1.strip()

print(pi_str)
print(len(pi_str))

with open('pi_million_digits.txt') as big:
    line1 = big.readlines()

pi_string = ''
for line2 in line1:
    pi_string += line2

print(f"{pi_string[: 52]}")

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appears in the first million digits of pi!")

# 练习 10-1

file_python_name = 'learn_python.txt'

with open(file_python_name) as learn:
    learn_line = learn.readlines()
print(learn_line)

for ev_learn_line in learn_line:
    ev_learn_line.replace('Python', 'C')
    print(ev_learn_line.rstrip())
