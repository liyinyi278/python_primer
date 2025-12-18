# 练习 6.7：人们 
#   在为练习 6.1 编写的程序中，再创建两个表示人的字典，
#   然后将这三个字典都存储在一个名为 people 的列表中。
#   遍历这个列表，将其中每个人的所有信息都打印出来。

person_0 = {'first_name': 'Jimi', 'last_name': 'Hendrix', 'age': 27, 'city': 'Seattle'}
person_1 = {'first_name': 'Eric', 'last_name': 'Clapton', 'age': 74, 'city': 'London'}
person_2 = {'first_name': 'John', 'last_name': 'Lennon', 'age': 40, 'city': 'Liverpool'}

people = [person_0, person_1, person_2]

# 利用str函数，可以将数字类型的值转换为字符串类型
for person in people:
    print(person['first_name'].title() + ' ' + person['last_name'].title())
    print('\t' + person['city'].title() + ', ' + str(person['age']) + ' years old')
    print()
print()
