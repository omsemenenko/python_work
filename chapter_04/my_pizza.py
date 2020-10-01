my_pizzas = ['pepperoni', 'margarita', 'cheese supreme']
friend_pizzas = my_pizzas[:]

my_pizzas.append('meat supreme')
friend_pizzas.append('hunters')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)