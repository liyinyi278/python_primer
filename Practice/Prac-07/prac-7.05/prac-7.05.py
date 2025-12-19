# 练习 7.5：电影票 
#   有家电影院根据观众的年龄收取不同的票价：
#       不到 3 岁的观众免费；
#       3（含）～12 岁的观众收费 10 美元；
#       年满 12 岁的观众收费 15 美元。
#   请编写一个循环，在其中询问用户的年龄，并指出其票价。

message = ""

while message != 'quit':
    age = input("How old are you? ")
    if age != 'quit':
        if age.isalpha():
            print("Please enter a number.")
            continue
        age = int(age)

        if age < 3:
            message = "You can enter for free."
        elif age < 12:
            message = "You can enter for $10."
        else:
            message = "You can enter for $15."
        print(message)
    else:
        message = 'quit'
print()            