# 3.4

guests = ['mick', 'jim', 'paul']
print(guests)

print(len(guests))

print(f"Hi, {guests[0].title()}, I wish you to supper.")
print(f"Hi, {guests[1].title()}, I wish you to supper.")
print(f"Hi, {guests[2].title()}, I wish you to supper.")

# 3.5

guests = ['mick', 'jim', 'paul']

print(f"Hi, {guests[0].title()}, I wish you to supper.")
print(f"Hi, {guests[1].title()}, I wish you to supper.")
print(f"Hi, {guests[2].title()}, I wish you to supper.")

print("Sorry, but Jim can't be.")

guests[0] = 'edward'
print(f"Hi, {guests[0].title()}, I wish you to supper.")
print(f"Hi, {guests[1].title()}, I wish you to supper.")
print(f"Hi, {guests[2].title()}, I wish you to supper.")

# 3.6

guests = ['mick', 'jim', 'paul']

print(f"Hi, {guests[0].title()}, I wish you to supper.")
print(f"Hi, {guests[1].title()}, I wish you to supper.")
print(f"Hi, {guests[2].title()}, I wish you to supper.")

print("I bue a big table and can wish more guests.")

guests.insert(0, 'sarah')
guests.insert(3, 'ivan')
guests.append('john')

print(guests)

print(f"Hi, {guests[0].title()}, I wish you to supper.")
print(f"Hi, {guests[1].title()}, I wish you to supper.")
print(f"Hi, {guests[2].title()}, I wish you to supper.")
print(f"Hi, {guests[3].title()}, I wish you to supper.")
print(f"Hi, {guests[4].title()}, I wish you to supper.")
print(f"Hi, {guests[5].title()}, I wish you to supper.")

# 3.7

print("Sorry, but can wish only two guests.")

not_wished = guests.pop()
print(f"Sorry, {not_wished.title()}, but I can wish you to supper.")

not_wished = guests.pop()
print(f"Sorry, {not_wished.title()}, but I can wish you to supper.")

not_wished = guests.pop()
print(f"Sorry, {not_wished.title()}, but I can wish you to supper.")

not_wished = guests.pop()
print(f"Sorry, {not_wished.title()}, but I can wish you to supper.")

print(f"{guests[0].title()}, I wish you to supper.")
print(f"{guests[1].title()}, I wish you to supper.")

print(guests)

del guests[0]
print(guests)

del guests[0]
print(guests)

