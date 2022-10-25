# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x = 0

import random

k = int(input('\nВведите натуральную степень k: '))
res = []
def rnd(): return random.randint(0, 100)

for i in range(k, 1, -1):
    c = rnd()
    if c:
        res.append(f'{c}x^{i}')

c = rnd()
if c:
    res.append(f'{c}x')
c = rnd()
if c:
    res.append(f'{c}')

res_line = ' + '.join(res) + ' = 0'

with open('file004.txt', 'w') as file:
    file.write(res_line + '\n')

print(res_line)