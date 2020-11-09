filename = 'cats.txt'

try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    print(f"File {filename} is not exist")
else:
    print(contents)

filename = 'dogs.txt'

try:
    with open('dogs.txt') as f:
        contents = f.read()
except FileNotFoundError:
    pass
    #print(f"File {filename} is not exist")
else:
    print(contents)



# filenames = ['cats.txt', 'dogs.txt']
#
#
# with open(filenames, encoding='utf-8') as f:
#     for filename in filenames:
#     print(filename)