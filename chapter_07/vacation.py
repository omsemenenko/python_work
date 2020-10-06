responses = {}

pooling_active = True

while pooling_active:
    name = input("What is your name? ")
    response = input("\nWhere do you want to spent your vacation? ")

    responses[name] = response

    repeat = input("\nDo you want to add another place? (Enter yes/ no) ")
    if repeat == 'no':
        pooling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} want to spent your vacation in {response.title()}.")

