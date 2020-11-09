def frequent_words(filename):
    """Подсчет приблизительного количества строк в файлею"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
        #print(f"Sorry, the file {filename} does not exist.")
    else:
        # Подсчет приблизительного количества строк в файле.
        words = contents.count('the')
        #num_words = len(words)
        print(f"The word 'the' in file {filename} has about {words} words.")

filenames = ['travels.txt', 'mutiny.txt']
for filename in filenames:
    frequent_words(filename)
