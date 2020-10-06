reserve_table = input("How many seats do you want to book a table for? ")
reserve_table = int(reserve_table)

if reserve_table >= 8:
    print(f"Sorry, you must be wait.")
else:
    print("Your table is ready!")