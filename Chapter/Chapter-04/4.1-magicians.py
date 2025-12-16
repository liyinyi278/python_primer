magicians = ['alice', 'david', 'carolina']

# 在 for 循环后面，没有缩进的代码都只执行一次，不会重复执行。
for magician in magicians:
    print(magician)
print('\n')


# 在for循环中，使用单数和复数形式的名称，
# 可帮助你判断代码段处理的是单个列表元素还是整个列表。
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

# for 语句末尾的冒号告诉 Python，下一行是循环的第一行。
# magicians = ['alice', 'david', 'carolina']
# ❶ for magician in magicians
#   print(magician)
# 如果不小心遗漏了冒号（见❶），将导致语法错误，因为 Python 不知道你
#   想干什么：
# File "magicians.py", line 2
#   for magician in magicians
# 
# SyntaxError: expected ':'

# 对于一些错误，Python 通过traceback 提供了修复建议，
# 因此很容易修复。但有些错误解决起来要困难得多，
# 虽然最终的修复方案可能只是修改单个字符。
# 即使你花了很长时间才将一个小问题修复，也不要感到难过，因为有这种遭遇的人比比皆是。

