prompt = "Enter the toppings to your pizza:"
prompt = "\n(Enter 'quit' if you want to continue.) "

# active = True
# while active:
#     topping = input(prompt)
#
#     if topping == 'quit':
#         active = False
#     else:
#         print(f"You ordered {topping}.")

# while True:
#     topping = input(prompt)
#
#     if topping == 'quit':
#         break
#     else:
#         print(f"You ordered {topping}.")

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(f"You ordered {message}.")
