# 练习 6.8：宠物 
#   创建多个表示宠物的字典，每个字典都包含宠物的类型及其主人的名字。
#   将这些字典存储在一个名为 pets 的列表中，再遍历该列表，并将有关每个宠物的所有信息打印出来。

pet_0 = {'type':'cat', 'owner':'Jimi Hendrix'}
pet_1 = {'type':'dog', 'owner':'Eric Clapton'}
pet_2 = {'type':'bird', 'owner':'John Lennon'}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(pet['type'] + ' is owned by ' + pet['owner'])
print()