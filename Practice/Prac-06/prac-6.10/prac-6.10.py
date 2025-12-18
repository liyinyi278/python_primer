# 练习 6.10：喜欢的数 2 
#   修改练习 6.2 编写的程序，
#   让每个人都可以有多个喜欢的数字，
#   然后将每个人的名字及其喜欢的数打印出来。

favorite_numbers = {
    'Tom': [7, 8, 9, 3],
    'Jerry': [3, 4, 5],
    'Alice': [5, 6],
    'Bob': [2],
    'Jack': [9, 10, 11, 4],
}

for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"{name}'s favorite number is: {numbers[0]}.")
    else:
        # ', '是分隔符（逗号 + 空格），
        # join()方法会将传入的可迭代对象，
        # （这里是生成器表达式str(num) for num in numbers）中的所有字符串元素，
        # 用该分隔符连接成一个整体字符串。
        print(f"{name}'s favorite numbers are: {', '.join(str(num) for num in numbers)}.")
print()        