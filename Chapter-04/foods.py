my_foods = ['pizza', 'falafel', 'carrot cake']

# 要复制列表，可以创建一个包含整个列表的切片，
# 方法是同时省略起始索引和终止索引（[:]）。
friend_foods = my_foods[:]

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# 现在我们分别向两个列表中添加一种食物
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# 在不使用切片的情况下复制列表的情况：
# friend_foods = my_foods
# 这样，friend_foods和my_foods都指向同一个列表，
# 因此一个列表中的任何修改都会反映在另一个列表中。
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)


