# 在 if 语句中，缩进的作用与 for 循环中相同。
# 如果条件测试通过了，将执行 if 语句后面所有缩进的代码行，否则将忽略它们。

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
