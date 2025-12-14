dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 这里的代码试图修改第一个元素的值，导致 Python 返回类型错误的消息。
# 由于试图修改元组的操作是被禁止的，因此 Python 指出不能给元组的元素赋值：
# Traceback (most recent call last):
# File "dimensions.py", line 2, in <module>
# dimensions[0] = 250
# TypeError: 'tuple' object does not support item assignment

# dimensions[0] = 250
# dimensions[1] = 100

# 虽然不能修改元组的元素，但可以给表示元组的变量赋值。
# 例如，要修改前述矩形的尺寸，可重新定义整个元组：
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# 严格地说，元组是由逗号标识的，圆括号只是让元组看起来更整洁、更清晰。
# 如果你要定义只包含一个元素的元组，必须在这个元素后面加上逗号：
# 创建只包含一个元素的元组通常没有意义，但自动生成的元组有可能只有一个元素。
my_t = (3,)
print(my_t)

# 列表一样，也可以使用 for 循环来遍历元组中的所有值：
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

