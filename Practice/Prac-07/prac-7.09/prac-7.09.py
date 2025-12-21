# 练习 7.9：五香烟熏牛肉卖完了 
#   使用为练习 7.8 创建的列表sandwich_orders，并确保 'pastrami' 在其中至少出现了三次。
#   在程序开头附近添加这样的代码：先打印一条消息，指出熟食店的五香烟熏牛肉（pastrami）卖完了；
#   再使用一个 while 循环将列表sandwich_orders 中的 'pastrami' 都删除。
#   确认最终的列表finished_sandwiches 中未包含 'pastrami'。

sandwich_orders = ['pastrami', 'ham', 'pastrami', 'pastrami', 'cheese', 'pastrami']
finished_sandwiches = []

print("We are out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("sandwich_orders:" , sandwich_orders)
print()

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print("I made your " + current_sandwich.title() + " sandwich.")
print()

print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
print()

