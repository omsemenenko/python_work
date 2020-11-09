prompt = "\nWhy do you like to programming? "

while True:
    answer = input(prompt)

    if answer == 'quit':
        break
    else:
        with open('questionary.txt', 'a') as file_object:
            file_object.write(f"{answer}\n")
        print(answer)

