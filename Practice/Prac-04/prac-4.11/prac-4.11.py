my_pizzas = ["pepperoni", "margherita", "hawaiian", "vegetarian", "meat lovers"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("cheese")
friend_pizzas.append("bbq")

print("\nMy favourite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)