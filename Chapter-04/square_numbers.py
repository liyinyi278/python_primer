# 要创建一个列表，其中包含前 10 个整数平方，可使用 range() 函数生成这些值，
# 并将它们转换为列表：
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# 也可以在一行中完成这些操作，这样代码更简洁：
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# 使用列表解析
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# 几个 Python 函数可帮助你处理数值列表。
# 比如，求列表中的最大值、最小值和总和：
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))