# 练习 6.1：
#   使用一个字典来存储一个人的信息，
#   包括名、姓、年龄和居住的城市。
#   该字典应包含键 first_name、last_name、age 和city。
#   将存储在该字典中的每项信息都打印出来。

person = {'first_name': 'Jimi', 'last_name': 'Hendrix', 'age': 27, 'country': 'USA'}

for key, value in person.items():
    print(f"{key}: {value}")
