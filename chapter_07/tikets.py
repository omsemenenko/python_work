age = input("Enter your age: ")
age = int(age)

if age < 3:
    print("You must pay $0.")
elif age < 12:
    print("you must pay $10.")
else:
    print("You must pay $15.")
