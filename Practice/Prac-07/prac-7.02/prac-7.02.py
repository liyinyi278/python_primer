# 练习 7.2：餐馆订位 
#   编写一个程序，询问用户有多少人用餐。
#   如果超过 8 个人，就打印一条消息，指出没有空桌；否则指出有空桌。

peoples = int(input("Enter the number of people: "))

if peoples >= 8:
    print("Table is full")
elif peoples <= 0:
    print("No one is coming")
else:
    print("Table is not full")