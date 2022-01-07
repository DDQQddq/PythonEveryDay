
a = "hello,world"
print(a)

a = 'hello python crash course world'
print(a.title())

name = "ade lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name+" "+last_name
print(full_name)
print("Hello,"+full_name.title()+"!")  # .title()

print("\tPython")  # \t  制表符
print("languages:\nPython\nC\nJavascript")   # \n  换行符（就当做new line吧)
print("languages:\n\tPython\n\tC\n\tJavascript")   # 既换行又制表

language = "python "
print(language)
language = language.rstrip()   # rstrip 去除尾部空格
print(language)
language = " python "
print(language)
print(language.lstrip())  # 去掉开头空白
print(language.rstrip())  # 尾部
print(language.strip())   # 两头
