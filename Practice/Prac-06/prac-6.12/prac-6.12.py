# 练习 6.12：扩展 
#   本章的示例足够复杂，能以很多方式进行扩展。
#   请对本章的一个示例进行扩展：添加键和值，调整程序要解决的问题，或改进输出的格式。

user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi',}
user_1 = {'username': 'mcurie', 'first': 'marie', 'last': 'curie',}
user_2 = {'username': 'davinci', 'first': 'leonardo', 'last': 'da vinci',}

users = [user_0, user_1, user_2]

for user in users:
    print("Username: " + user['username'].title() + ", Full Name: " + user['first'].title() + " " + user['last'].title())
print()
