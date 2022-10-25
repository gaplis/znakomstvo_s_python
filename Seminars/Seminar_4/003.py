# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

from math import lcm

x = int(input('Введите x: '))
y = int(input('Введите y: '))

if x > y: 
    big = x
else: 
    big = y
while(True):
    if big % x == 0 and big % y == 0:
        result = big
        break
    big += 1
print(result)

def gcd(x, y):
    if y > x:
        x, y = y, x
    if y == 0:
        return x
    
    return gcd(y, x % y)

a, b = tuple(map(int, input('Введите числа через пробел: ').split()))

print(f'lcm = {a * b / (gcd(a, b))}')
print(f'{lcm(a, b) = }') # Самодокументация