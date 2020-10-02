# 1

names = ['ivan', 'admin', 'edward', 'sarah', 'jaden']

if names:
    for name in names:
        if name == 'admin':
            print("Hello admin, would you like to see a status report?")
        elif name in names:
            print(f"Hello {name.title()}, than you for logging in again.")
else:
    print("We need to ind some users!")


