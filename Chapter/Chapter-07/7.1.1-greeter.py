# 每当使用 input() 函数时，都应指定清晰易懂的提示，准确地指出希望用户提供什么样的信息。

# 通过在提示末尾（这里是冒号后面）添加一个空格，
# 可将提示与用户输入分开，让用户清楚地知道其输入始于何处。
name = input("Please enter your name: ")
print("\nHello, " + name + "!")
print()

# 有时候，提示可能超过一行。
# 例如，你可能需要指出获取特定输入的原因。
# 在这种情况下，可先将提示赋给一个变量，
# 再将这个变量传递给 input()函数。
# 这样，即便提示超过一行，input() 语句也会非常清晰。
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")
print()
