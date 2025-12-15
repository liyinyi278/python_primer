# 还有些时候，确定特定的值不在列表中很重要。在这种情况下，可使用关键字 not in。

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# 随着对编程的了解越来越深入，你将遇到术语布尔表达式，它不过是条件测试的别名罢了。
# 与条件表达式一样，布尔表达式的结果要么为 True，要么为 False。
# 布尔值通常用于记录条件，如游戏是否正在运行或用户是否可以编辑网站的特定内容：
game_active = True
can_edit = False
print(game_active)
print(can_edit)
# 在跟踪程序状态或程序中重要的条件方面，布尔值提供了一种高效的方式。