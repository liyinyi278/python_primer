# 要创建数值列表，可使用 list() 函数将 range() 的结果直接转换为列表。
# 如果将 range() 作为 list() 的参数，输出将是一个数值列表。
numbers = list(range(1, 6))
print(numbers)

# 在使用 range() 函数时，还可指定步长。
# 为此，可以给这个函数指定第三个参数，Python 将根据这个步长来生成数。
even_numbers = list(range(2, 11, 2))
print(even_numbers)
