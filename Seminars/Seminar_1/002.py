# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
d = int(input('Введите четвертое число: '))
e = int(input('Введите пятое число: '))

max = a

if a > max: max = a
if b > max: max = b
if c > max: max = c
if d > max: max = d
if e > max: max = e

print(max)

nums = input('Введите 5 чисел через пробел: ').split()
max_nums = int(nums[0])
for i in nums:
    if int(i) > max_nums:
        max_nums = int(i)

print(max_nums)