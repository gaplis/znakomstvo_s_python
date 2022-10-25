# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import re
from sympy import Symbol, collect

def convert(line):
    line = re.sub(r'(\d)(x)', r'\1*\2', line)
    line = line.replace('^', '**')
    line = line[:-4:]
    return line

with open('file005_1.txt', 'r') as data1:
    rec1 = data1.readline()

with open('file005_2.txt', 'r') as data2:
    rec2 = data2.readline()

print(f'Первый файл: {rec1}')
print(f'Второй файл: {rec2}')

rec1 = convert(rec1)
rec2 = convert(rec2)

print(f'Первый файл конвертированный: {rec1}')
print(f'Второй файл конвертированный: {rec2}')

x = Symbol('x')

res = str(collect(rec1 + ' + ' + rec2, 'x'))
res = res.replace('**', '^')
res = res.replace('*', '')
res += ' = 0'
print(f'Сумма многочленов: {res}')

with open('file005_3.txt', 'w') as data3:
    data3.write(res)