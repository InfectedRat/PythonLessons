from os import path

file_name = 'test1.txt'
file_path = path.join(path.dirname(__file__), file_name)
file = open(file_path, 'a',  encoding='utf-8')

while True:
    u_string = input('Введите данные для файла: ')

    if not u_string:
        file.close()
        print('Ввод окончен')
        break

    file.write(f'{u_string}\n')