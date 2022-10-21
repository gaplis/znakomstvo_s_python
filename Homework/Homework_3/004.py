# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# 45 -> 101101
# 3 -> 11
# 2 -> 10

num = int(input('Введите число: '))

binary_string = ''

if num == 0:
    binary_string = str(num)
else:
    while num > 0:
        binary_string = str(num % 2) + binary_string
        num //= 2

print(binary_string)