responses = []

pooling_active = True

while pooling_active:
    response = input("\nWhere do you want to spent your vacation? ")

    responses = response

    repeat = input("\nDo you want to add another place? (Enter yes/ no) ")
    if repeat == 'no':
        pooling_active = False

print("\n--- Poll Results ---")
for response in responses:
    print(f"You want to spent your vacation in {response.title()}.")