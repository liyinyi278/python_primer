# 你经常需要检查两个以上的情形，此时可使用 Python 提供的 if-elif-else 语句。
# Python 只执行 if-elif-else 结构中的一个代码块。
# 它依次检查每个条件测试，直到遇到通过了的条件测试。
# 条件测试通过后，Python 将执行紧跟在它后面的代码，并跳过余下的条件测试。

# if-elif-else 语句结构
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# 更简洁的写法，程序的可修改性也更强
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print("Your admission cost is $" + str(price) + ".")

# 使用多个 elif 代码块
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print("Your admission cost is $" + str(price) + ".")

# 省略 else 代码块

# else 是一条包罗万象的语句，
# 只要不满足任何 if 或 elif 中的条件测试，其中的代码就会执行。
# 这可能引入无效甚至恶意的数据。
# 如果知道最终要测试的条件，应考虑使用一个 elif 代码块来代替 else 代码块。
# 这样就可以肯定，仅当满足相应的条件时，代码才会执行。
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print("Your admission cost is $" + str(price) + ".")