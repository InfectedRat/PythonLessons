from os import path

file_name = 'test1.txt'
file_path = path.join(path.dirname(__file__), file_name)
file = open(file_path, 'r',  encoding='utf-8')
lines = file.readlines()

print(f'В файле {len(lines)} строк')
i = 1
for _ in lines:
    print(f'В {i}-й строке: {len(_.split())} слов')
    i+=1
file.close()