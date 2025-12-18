# 创建一个外星人列表，其中每个外星人都是一个字典。
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

print("Aliens list:")
for alien in aliens:
    print(alien)
print()

# 使用 range() 生成了 30 个外星人。
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 显示前五个外星人。
print("First five aliens:")
for alien in aliens[:5]:
    print(alien)
print("Total number of aliens: " + str(len(aliens)))
print()


# 修改前三个外星人，并再次显示前五个外星人。
print("Modified first three aliens:")
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
print()        

print("First five aliens:")
for alien in aliens[:5]:
    print(alien)
print()

# 你经常需要在列表中存储大量的字典，而且每个字典都包含特定对象的众多信息。
# 例如，为网站的每个用户创建一个字典（就像 6.3.1 节的 user.py中那样），
# 并将这些字典存储在一个名为 users 的列表中。在这个列表中，
# 所有字典的结构都相同，因此可遍历这个列表，并以相同的方式处理其中的每个字典。