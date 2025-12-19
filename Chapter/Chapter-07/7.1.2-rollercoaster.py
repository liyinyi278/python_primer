height = input("How tall are you, in inches? ")

# 使用函数 int() ，可以将输入的字符串转换为数值。
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
print()
