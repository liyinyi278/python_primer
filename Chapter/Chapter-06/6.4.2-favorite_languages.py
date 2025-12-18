# 每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表。
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is:")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
    
    for language in languages:
        print(f"\t{language.title()}")
print()    

# 注意：列表和字典的嵌套层级不应太多。
# 如果嵌套层级比前面的示例多得多，很可能有更简单的解决方案。