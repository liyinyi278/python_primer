# 练习 7.8：熟食店 
#   创建一个名为 sandwich_orders 的列表，其中包含各种三明治的名字，
#   再创建一个名为 finished_sandwiches 的空列表。
#   遍历列表 sandwich_orders，对于其中的每种三明治，都打印一条消息，
#   如“I made your tuna sandwich.”，并将其移到列表finished_sandwiches 中。
#   当所有三明治都制作好后，打印一条消息，将这些三明治列出来。

sandwich_orders = ['pastrami', 'ham', 'pastrami', 'pastrami', 'cheese', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print("I made your " + current_sandwich.title() + " sandwich.")
print()

print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
print()

