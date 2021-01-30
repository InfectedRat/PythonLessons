from os import path

file_name = 'word.txt'
file_name2 = 'word_rus.txt'
file_path = path.join(path.dirname(__file__), file_name)
file_path2 = path.join(path.dirname(__file__), file_name2)
my_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open(file_path, 'r', encoding='utf-8') as file_read:
    lines = file_read.readlines()

with open(file_path2, 'a', encoding='utf-8') as file_write:
    for _ in lines:
        row = _.split()
        row[0] = my_dict[row[0]]
        print(' '.join(row), file=file_write)