# 可以在字典中嵌套字典，但这样可能会让代码很快变得非常复杂。

# 如果有一网站有多个用户，每个用户都有独特的用户名，
# 可在字典中将用户名作为键，然后将每个用户的信息存储在一个字典中，
# 并将该字典作为与用户名关联的值。

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
print()

# 请注意，表示每个用户的字典都有相同的结构，
# 虽然 Python 并没有这样的要求，但这使得嵌套的字典处理起来更容易。
# 倘若表示每个用户的字典都包含不同的键，for 循环内部的代码将更复杂。