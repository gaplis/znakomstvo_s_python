# Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = input('Введите строку: ')

tmp = []
for word in text.split():
    w = word.lower()
    if not ('а' in w and 'б' in w and 'в' in w):
        tmp.append(w)

print(' '.join(tmp))

# Программа удаляет слова, в которых есть все три буквы, в моей реализации удаляет каждое слово, где есть хоть одна буква

ref = set(input('Введите строку с символами: ').lower())

with open('task001_input.txt', 'r', encoding='utf-8') as input_file:
    input_data = input_file.readlines()
with open('task001_output.txt', 'w', encoding='utf-8') as output_file:
    for data in input_data:
        if not ref.issubset(set(data.lower())):
            output_file.write(f'{data}')
    #output_file.writelines([data for data in input_data if not ref <= set(data.lower())])

# my_text = ' '.join(filter(lambda x: not ('а' in x and 'б' in x and 'в' in x), my_text.lower().split()))

print(*filter(lambda x: not set(x) >= set('абв'), text.split()), sep=' ')

print(*filter(lambda x: not all(True if ch in x else False for ch in 'абв'), text.split()), sep=' ')