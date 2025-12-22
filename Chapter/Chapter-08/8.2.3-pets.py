# 在编写函数时，可以给每个形参指定默认值。
# 请注意，在这个函数的定义中，修改了形参的排列顺序。
# 如果函数调用只包含宠物的名字，这个实参将被关联到函数定义中的第一个形参。
# 这就是需要将 pet_name 放在形参列表开头的原因。

def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie')
describe_pet(pet_name='harry', animal_type='hamster')

# 如果调用函数时没有给一个有默认值的形参指定值，Python将使用这个形参的默认值。

# 注意：当使用默认值时，必须在形参列表中先列出没有默认值的形参，
# 再列出有默认值的形参。这让 Python 依然能够正确地解读位置实参。

# 鉴于可混合使用位置实参、关键字实参和默认值，通常有多种等效的函数调用方式。
# 使用哪种调用方式无关紧要。
# 可以使用对你来说最容易理解的调用方式，只要函数调用能生成你期望的输出就好。