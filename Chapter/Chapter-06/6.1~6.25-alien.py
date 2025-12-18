# 字典（dictionary）是一系列键值对。
# 每个键都与一个值关联，可以使用键来访问与之关联的值。
# 与键相关联的值可以是数、字符串、列表乃至字典。
# 事实上，可将任意 Python 对象用作字典中的值。

# 键值对包含两个相互关联的值。
# 当你指定键时，Python 将返回与之关联的值。
# 键和值之间用冒号分隔，而键值对之间用逗号分隔。
# 在字典中，你想存储多少个键值对都可以。

# 字典用放在花括号（{}）中的一系列键值对表示。
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# 字典是一种动态结构，可随时在其中添加键值对。
# 要添加键值对，可依次指定字典名、用方括号括起来的键和与该键关联的值。
print()
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 字典会保留定义时的元素排列顺序。
# 如果将字典打印出来或遍历其元素，
# 将发现元素的排列顺序与其添加顺序相同。

# 有时候，在空字典中添加键值对很方便，甚至是必需的。
# 为此，可先使用一对空花括号定义一个空字典，再分行添加各个键值对。
print()
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# 要修改字典中的值，可依次指定字典名、
# 用方括号括起来的键和与该键关联的新值。
print()
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# 例子：对一个能够以不同速度移动的外星人进行位置跟踪。
print()
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# 向右移动外星人
# 根据当前速度确定将外星人向右移动多远。
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的移动速度肯定很快
    x_increment = 3

# 新位置为旧位置加上移动距离。
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

# 对于字典中不再需要的信息，
# 可使用 del 语句将相应的键值对彻底删除。
# 在使用 del 语句时，必须指定字典名和要删除的键。
print()
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# 注意：删除的键值对永远消失了。
print("\nDeleting points")
del alien_0['points']
print(alien_0)
