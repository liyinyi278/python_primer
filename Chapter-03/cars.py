#sort() 方法能永久地修改列表元素的排列顺序。
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#还可以按与字母顺序相反的顺序排列列表元素，
#只需向 sort() 方法传递参数 reverse=True 即可。
cars.sort(reverse=True)
print(cars)

#使用 sorted() 函数对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\n")
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#要反转列表元素的排列顺序，可使用 reverse() 方法。
#reverse() 方法会永久地修改列表元素的排列顺序，但可随时恢复到原
#来的排列顺序，只需对列表再次调用 reverse() 即可。
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print("\n" + str(cars)) #利用str函数，可以将列表转换为字符串，方便打印

#使用 len() 函数可快速获悉列表的长度。
print("\n" + str(len(cars)) + " cars in the list")

#注意：Python 在计算列表元素数时从 1 开始，因此你在确定列表长
#度时应该不会遇到差一错误。

