# 向函数传递实参的方式很多：
#   既可以使用位置实参，这要求实参的顺序与形参的顺序相同；
#   也可以使用关键字实参，其中每个实参都由变量名和值组成；
#   还可以使用列表和字典。

def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# 位置实参
describe_pet('hamster', 'harry')

# 关键字实参
# 注意：在使用关键字实参时，务必准确地指定函数定义中的形参名。
describe_pet(animal_type='dog', pet_name='willie')

# 使用列表和字典
pets = ['dog', 'willie']
describe_pet(*pets)

pets = {'animal_type': 'cat', 'pet_name': 'kitty'}
describe_pet(**pets)
