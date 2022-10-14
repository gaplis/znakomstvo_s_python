# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

num = int(input('Введите число: '))

num_list = range(-num, num + 1)

for i in num_list:
    print(i)

print(*range(-num, num + 1), sep=', ')