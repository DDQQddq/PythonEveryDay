favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'eward': 'ruby',
    'phil': 'python',
    }
for name in sorted(favorite_language):
    print(f"{name.title()},thank you take the poll!")
print('The following language have been mentioned:')
for language in favorite_language.values():   # 包含重复项
    print(language.title())
print('The following language have been mentioned:')
for language in set(favorite_language.values()):
    print(language.title())
