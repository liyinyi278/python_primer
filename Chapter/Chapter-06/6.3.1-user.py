user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
print (user_0)

# Python 支持对字典进行遍历，字典可用于以各种方式存储信息。
# 因此有多种遍历方式：既可遍历字典的所有键值对，也可只遍历键或值。

# for 语句的第二部分包含字典名和方法 items()，这个方法返回一个键值对列表。
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)