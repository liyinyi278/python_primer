requested_toppings = 'mushrooms'

if requested_toppings != 'anchovies':
    print("Hold the anchovies!")

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age_0 = 22
age_1 = 18

# 要检查两个条件是否都为 True，可使用关键字 and 将两个条件测试合而为一。
if age_0 >= 21 and age_1 >= 21:
    print("Both are old enough to drink.")

# 关键字 or 也能够让你检查多个条件，但只要满足其中一个条件，就能通过整个条件测试。
if age_0 >= 21 or age_1 >= 21:
    print("At least one is old enough to drink.")

# 有时候，执行操作前必须检查列表是否包含特定的值。
# 例如，在结束用户的注册过程之前，需要检查他提供的用户名是否已在用户名列表中；
# 在地图程序中，需要检查用户提交的位置是否在已知位置的列表中。
# 要判断特定的值是否在列表中，可使用关键字 in。
requested_toppings = ['mushrooms', 'onions', 'pineapple']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
