# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# *Примеры:*
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))

# a, b = int(input('Введите число a: ')), int(input('Введите число b: '))

if a**2 == b or b**2 == a:
    print('Является')
else:
    print('Не является')

# print('да' if a ** 2 == b or b ** 2 == a else 'нет')