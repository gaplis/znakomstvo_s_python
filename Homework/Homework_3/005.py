# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Введите число: '))

fib_lst = [0]
nega_fib_lst = []

for i in range(1, num + 1):
    if i == 1:
        res = 1
    else:
        res = fib_lst[i - 1] + fib_lst[i - 2]
    fib_lst.append(res)

for i in range(1, num + 1):
    if int(i) % 2 == 0:
        res = -fib_lst[i]
    else:
        res = fib_lst[i]
    nega_fib_lst.append(res)

print(nega_fib_lst)
print(fib_lst)
print(nega_fib_lst[::-1] + fib_lst)