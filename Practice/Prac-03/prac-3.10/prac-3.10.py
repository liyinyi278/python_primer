loves = ["山川","河流","国家","城市","语言"]

for love in loves:
    print("我爱：" + love + ".")

print("\n原始列表：")
print(loves)

print("\n排序后的列表：")
print(sorted(loves))

print("\n再次打印原始列表：")
print(loves)

print("\n倒序打印列表：")
print(loves[::-1])
print(sorted(loves, reverse=True))

print("\n再次打印原始列表：")
print(loves)

print("\n永久倒序打印列表：")
loves.reverse()
print(loves)

print("\n再次永久倒序打印列表：")
loves.reverse()
print(loves)

print("\n永久排序打印列表：")
loves.sort()
print(loves)

print("\n再次永久倒序打印列表：")
loves.sort(reverse=True)
print(loves)

print("\n列表长度：")
print(len(loves))

del loves[0]
print(f"\n{loves}")

loves.remove("国家")
print(loves)

loves.pop()
print(loves)

loves.append("音乐")
print(loves)

loves.insert(0, "舞蹈")
print(loves)

