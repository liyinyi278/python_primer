prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
print()

# 在要求满足很多条件才继续运行的程序中，可定义一个变量，
# 用于判断整个程序是否处于活动状态。
# 这个变量称为标志（flag），充当程序的交通信号灯。
# 可以让程序在标志为 True 时继续运行，并在任何事件导致标志的值为False 时让程序停止运行。
# 这样，在 while 语句中就只需检查一个条件：标志的当前值是否为 True。然后将所有测试
# （是否发生了应将标志设置为False 的事件）都放在其他地方，从而让程序更整洁。
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
print()