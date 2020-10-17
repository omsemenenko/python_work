def send_message(show_messages, sending_messages):
    while show_messages:
        messages = show_messages.pop()
        print(f"Show messages: {messages}")
        sending_messages.append(messages)

def sent_messages(sending_messages):
    print("\nThe sending messages:")
    for sending_message in sending_messages:
        print(sending_message)

show_messages = ['Hello', 'What is your name?', 'How old are you?']
sending_messages = []

send_message(show_messages[:], sending_messages)
sent_messages(sending_messages)

print(show_messages)
print(sending_messages)


# def show_messages(message):
#     for message in message:
#         print(message)
#
# msg = ['Hello', 'What is your name?', 'How old areyou?']
# show_messages(msg)