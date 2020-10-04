favorite_numbers = {
    'oleksandr': [1, 7],
    'nadiia': [7, 12, 14],
    'dmytriy': [12],
    'iryna': [18, 22],
    'mykola': [11],
    }

for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"\n{name.title()} favorite number is:")
    else:
        print(f"\n{name.title()} favorite numbers are:")
    for number in numbers:
        print(f"\t{number})

# print(f"The Oleksandr's favorite number is {favorite_numbers['oleksandr']}.")
# print(f"The Nadiia's favorite number is {favorite_numbers['nadiia']}.")
# print(f"The Dmytriy's favorite number is {favorite_numbers['dmytriy']}.")
# print(f"The Iryns's favorite number is {favorite_numbers['iryna']}.")
# print(f"The Mykola's favorite number is {favorite_numbers['mykola']}.")

