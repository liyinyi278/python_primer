# 在处理数值信息时，求模运算符（%）是个很有用的工具，它将两个数相除并返回余数。

number = int(input("Enter a number, and I'll tell you if it's even or odd: "))

if number % 2 == 0:
    print(f"{number} is a even")
else:
    print(f"{number} is a odd")
print()