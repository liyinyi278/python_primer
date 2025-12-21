# 练习 7.4：比萨配料 
#   编写一个循环，提示用户输入一系列比萨配料，并在用户输入 'quit' 时结束循环。
#   每当用户输入一种配料后，都打印一条消息，指出要在比萨中添加这种配料。

burdening = ""

while burdening != 'quit':
    burdening = input("What is your burdening? (Enter 'quit' to end)")
    if burdening != 'quit':
        print(burdening)
    else:
        print("Thank you for sharing your burdens.")
print()    