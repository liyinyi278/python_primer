# 练习 7.10：梦想中的度假胜地 
#   编写一个程序，调查用户梦想中的度假胜地。
#   使用类似于“If you could visit one place in the world,
#   where would you go?”的提示，并编写一个打印调查结果的代码块。

dream_places = {}

active = True
while active:
    name = input("Please input your name: ")
    place = input("If you could visit one place in the world,where would you go?: ")

    dream_places[name] = place

    repeat = input("Do you want to add more? (y/n) ")
    if repeat.lower() != "y":
        active = False

for name, place in dream_places.items():
    print(f"{name}'s dream place is: {place}")
print()
