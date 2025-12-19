# 练习 7.6：三种出路 
#   以不同的方式完成练习 7.4 或练习 7.5，在程序中采取如下做法。
#       1、在 while 循环中使用条件测试来结束循环。
#       2、使用变量 active 来控制循环结束的时机。
#       3、使用 break 语句在用户输入 'quit' 时退出循环。

pizza = ""

while pizza != 'quit':
    pizza = input("\nWhat kind of pizza do you want?(Type 'quit' to end the program) ")
    if pizza != 'quit':
        print(f"I love {pizza} pizza!")     

active = True
while active:
    message = input("\nTell me something, and I will repeat it back to you: ")
    if message == 'quit':
        active = False
    else:
        print(message)

while True:
    pizza = input("\nWhat kind of pizza do you want?(Type 'quit' to end the program) ")
    if pizza == 'quit':
        break
    else:
        print(f"I love {pizza} pizza!")

