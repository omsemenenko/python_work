def count_words(filename):
    """Подсчет приблизительного количества строк в файлею"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
        #print(f"Sorry, the file {filename} does not exist.")
    else:
        # Подсчет приблизительного количества строк в файле.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
