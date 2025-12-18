# 练习 6.9：喜欢的地方 
#   创建一个名为 favorite_places 的字典。
#   在这个字典中，将三个人的名字用作键，并存储每个人喜欢的 1～3个地方。
#   为让这个练习更有趣些，让一些朋友说出他们喜欢的几个地方。
#   遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。

favorite_places = {
    'jimi': ['seattle', 'paris', 'lisbon'],
    'john': ['london'],
    'eric': ['miami', 'barcelona', 'rio de janeiro'],
}

for name, places in favorite_places.items():
    if len(places) == 1:
        print(f"\n{name.title()}'s favorite place is:")
    else:
        print(f"\n{name.title()}'s favorite places are:")

    for place in places:
        print(f"\t{place.title()}")
print()        