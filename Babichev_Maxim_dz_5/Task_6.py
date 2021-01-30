from os import path
from re import sub

file_name = 'lessons_hours.txt'
file_path = path.join(path.dirname(__file__), file_name)

def hours(line: str):
    line_hours = sub(r"\D", ' ', line)
    sum = 0
    for _ in line_hours.split():
        sum += float(_)
    return sum

my_dict = {}
with open(file_path, 'r', encoding='utf-8') as file_read:
    for _ in file_read.readlines():
        lines = _.split(': ')
        my_dict[lines[0]] = hours(lines[1])

print(f'Результат: {my_dict}')