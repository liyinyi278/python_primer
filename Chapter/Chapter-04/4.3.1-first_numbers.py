# range() 只打印数 1～4，这是编程语言中常见的差一行为的结果。
for value in range(1, 5):
    print(value)

# 在调用 range() 函数时，也可只指定一个参数，这样它将从 0 开始，
# 例如，range(6) 返回数 0～5（含）。
for value in range(6):
    print(value)

# 要创建数值列表，可使用 list() 函数将 range() 的结果直接转换为列表。
# 如果将 range() 作为 list() 的参数，输出将是一个数值列表。
numbers = list(range(1, 6))
print(numbers)

# range() 还可指定步长。例如，下面的代码打印 1～10 内的偶数：
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# 同样，要创建 1～10 内的奇数，可将步长设置为 2（如下所示）：
odd_numbers = list(range(1, 11, 2))
print(odd_numbers)
