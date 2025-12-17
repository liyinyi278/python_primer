# 当确定需要使用多行来定义字典时，先在输入左花括号后按回车键，
# 再在下一行缩进 4 个空格，指定第一个键值对，并在它后面加上一个逗号。
# 此后再按回车键，文本编辑器将自动缩进后续键值对，且缩进量与第一个键值对相同。

# 定义好字典后，在最后一个键值对的下一行添加一个右花括号，
# 并且也缩进 4 个空格，使其与字典中的键对齐。
# 一种不错的做法是，在最后一个键值对后面也加上逗号，为以后添加键值对做好准备。
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# 使用字典时，可访问其中的任何信息。下面来访问 Phil 最喜欢的语言。
print("Phil's favorite language is " + favorite_languages['phil'].title() + ".")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

# 在不需要使用字典中的值时，keys() 方法很有用。
for name in favorite_languages.keys():
    print(name.title())

# 在遍历字典时，会默认遍历所有的键。因此，如果将上述代码中的
#   for name in favorite_languages.keys():
# 替换为
#   for name in favorite_languages:
# 输出将不变。

# 在这种循环中，可使用当前的键来访问与之关联的值。
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print("  Hi " + name.title() + ", I see your love " + language)

# 还可以使用 keys() 确定某个人是否接受了调查。
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# 遍历字典时将按插入元素的顺序返回其中的元素，
# 但是在一些情况下，你可能要按与此不同的顺序遍历字典。
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# 如果你感兴趣的是字典包含的值，可使用 values() 方法。
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# 以上做法提取字典中所有的值，而没有考虑值是否有重复。要消除重复项，可使用 set() 。
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# 注意：可以使用一对花括号直接创建集合，并在其中用逗号分隔元素
languages = {'python', 'rust', 'python', 'c'}
print(languages)

# 集合和字典很容易混淆，因为它们都是用一对花括号定义的。
# 当花括号内没有键值对时，定义的很可能是集合。
# 不同于列表和字典，集合不会以特定的顺序存储元素。