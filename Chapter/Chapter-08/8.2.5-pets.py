# 等你开始使用函数后，也许会遇到实参不匹配错误。
# 当你提供的实参多于或少于函数完成工作所需的实参数量时，将出现实参不匹配错误。

def describe_pet(animal_type, pet_name):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet()

# 在这个示例中，函数describe_pet()需要两个实参：一个用于animal_type，一个用于pet_name。
# 由于没有给这两个参数提供任何值，Python指出我们提供的实参过少，导致出现错误。

# 错误信息：
# Traceback (most recent call last):
#   File "8.2.5-pets.py", line 6, in <module>
#     describe_pet()
# TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'

# traceback 指出该函数调用缺少两个实参，并指出了相应形参的名称。
# 如果这个函数存储在一个独立的文件中，
# 我们也许无须打开这个文件并查看函数的代码，就能重新正确地编写函数调用。

# 这是应该给变量和函数指定描述性名称的另一个原因：
#   如果这样做了，那么无论对于你，
#   还是可能使用你编写的代码的其他任何人来说，
#   Python 提供的错误消息都将更有帮助性。