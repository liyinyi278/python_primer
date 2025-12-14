youth = ["lihongrui", "liuweiwei", "chengcheng", "liuxiuxiu", "maoxihui", "liuxiaohang", "wangxingming"]

print(youth[0] + ", Please have dinner with me.")
print(youth[1] + ", Please have dinner with me.")
print(youth[2] + ", Please have dinner with me.")
print(youth[3] + ", Please have dinner with me.")
print(youth[4] + ", Please have dinner with me.")
print(youth[5] + ", Please have dinner with me.")
print(youth[6] + ", Please have dinner with me.")

youth.insert(0, "chengliudang")
youth.insert(2, "wenjing")
youth.append("liaoxiaoling")

print("\n")
print(youth[0] + ", Please have dinner with me.")
print(youth[1] + ", Please have dinner with me.")
print(youth[2] + ", Please have dinner with me.")
print(youth[3] + ", Please have dinner with me.")
print(youth[4] + ", Please have dinner with me.")
print(youth[5] + ", Please have dinner with me.")
print(youth[6] + ", Please have dinner with me.")
print(youth[7] + ", Please have dinner with me.")
print(youth[8] + ", Please have dinner with me.")
print(youth[9] + ", Please have dinner with me.")

print("\nOnly two guests can be invited.")

del_youth = youth[0]
del youth[0]
print("\n" + del_youth + ", I'm sorry, but I can't invite you to have dinner together")

del_youth = "lihongrui"
youth.remove("lihongrui")
print("\n" + del_youth + ", I'm sorry, but I can't invite you to have dinner together")

del_youth = youth[0]
del youth[0]
print("\n" + del_youth + ", I'm sorry, but I can't invite you to have dinner together")

del_youth = "liuxiuxiu"
youth.remove("liuxiuxiu")
print("\n" + del_youth + ", I'm sorry, but I can't invite you to have dinner together")

del_youth = youth.pop()
print("\n" + del_youth + ", I'm sorry, but I can't invite you to have dinner together")

del_youth = youth.pop()
print("\n" + del_youth + ", I'm sorry, but I can't invite you to have dinner together")

del_youth = youth.pop(0)
print("\n" + del_youth + ", I'm sorry, but I can't invite you to have dinner together")

del_youth = youth.pop()
print("\n" + del_youth + ", I'm sorry, but I can't invite you to have dinner together")


print("\n" + youth[0] + ", Please have dinner with me.")
print("\n" + youth[1] + ", Please have dinner with me.")

youth.pop()
youth.pop()

print("\n")
print(youth)