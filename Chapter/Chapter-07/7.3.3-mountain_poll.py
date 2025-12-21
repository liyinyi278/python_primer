# 可以使用 while 循环提示用户输入任意多的信息。
# 下面创建一个调查程序，其中的循环在每次执行时都提示输入被调查者的名字和回答。
# 我们将收集到的数据存储在一个字典中，以便将回答与被调查者关联起来。

# 测试数据：
#   Eric Denali yes 
#   Lynn Devil's Thumb no

responses = {}

polling_active = True
while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # 将被调查者的答案存储在字典中
    responses[name] = response

    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# 打印结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
print()