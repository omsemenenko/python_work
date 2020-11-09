import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(number, f)
        print(f"Your favorite number is {number}.")
else:
    print(f"I know your favorie number. It's {favorite_number}.")