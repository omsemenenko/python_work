prompt = "\nEnter your name, please: "

while True:
    name = input(prompt)

    if name == 'quit':
        break
    else:
        with open('guest_book.txt', 'a') as file_object:
            file_object.write(f"{name.title()}\n")
        print(f"You are in guest book, {name.title()}")

