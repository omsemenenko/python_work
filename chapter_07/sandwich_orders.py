sandwich_orders = ['first', 'second', 'third', 'first', 'fourth', 'first']
finished_sandiches = []

while 'first' in sandwich_orders:
    sandwich_orders.remove('first')
print("Sorry, but first sandwich not present.")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich.")
    finished_sandiches.append(current_sandwich)

print("\nWe prepeared next sandwiches:")
for finished_sandich in finished_sandiches:
    print(f"{finished_sandich} sandwich")