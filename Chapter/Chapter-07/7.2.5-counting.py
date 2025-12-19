# 要返回循环开头，并根据条件测试的结果决定是否继续执行循环，可使用continue 语句

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
print()

# 每个 while 循环都必须有结束运行的途径，这样才不会没完没了地执行下去。
# 如果程序陷入无限循环，既可按 Ctrl + C，也可关闭显示程序输出的终端窗口。
# 要避免编写无限循环，务必对每个 while 循环进行测试，确保它们按预期那样结束。