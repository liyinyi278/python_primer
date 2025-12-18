# 每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表。

# 存储顾客所点比萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# 当函数调用 print() 中的字符串很长，需要分成多行书写时，
# 可以在合适的位置分行，在每行末尾都加上引号，
# 并且对于除第一行外的其他各行，都在行首加上引号并缩进。

# 打印顾客点的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
print()