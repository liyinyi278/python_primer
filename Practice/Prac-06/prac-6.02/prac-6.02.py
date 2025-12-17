# 练习 6.2：喜欢的数 1 
#   使用一个字典来存储一些人喜欢的数。
#   请想出 5 个人的名字，并将这些名字用作字典中的键。
#   再想出每个人喜欢的一个数，并将这些数作为值存储在字典中。
#   打印每个人的名字和喜欢的数。

#   为了让这个程序更有趣，通过询问朋友确保数据是真实的。

favorite_numbers = {
    'Tom': 7,
    'Jerry': 3,
    'Alice': 5,
    'Bob': 2,
    'Jack': 9,
}

for name, number in favorite_numbers.items():
    print(f"{name} likes the number {number}.")