# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

s = str(input('Введите числа через пробел: '))
print(s)

lst = s.split(" ")
print(s)

print(max(list(map(int, lst))), min(list(map(int, lst))))

num = input('Введите числа через пробел: ').split()

min_num = int(num[0])
max_num = int(num[0])

for i in num:
    if int(i) > max_num:
        max_num = int(i)
    if int(i) < min_num:
        min_num =int(i)
print(min_num, max_num)