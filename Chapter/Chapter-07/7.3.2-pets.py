# 在第 3 章中，我们使用 remove() 函数来删除列表中的特定值。
# 这之所以可行，是因为要删除的值在列表中只出现了一次。
# 如果要删除列表中所有为特定值的元素，该怎么办呢？

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)