number = input("Please, enter a number, and I answer to you, even or odd number 10: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe {number} is even 10.")
else:
    print(f"\nThe {number} is not even 10.")