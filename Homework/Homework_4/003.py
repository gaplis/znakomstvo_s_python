# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

numbers_lst = list(map(int, input('Введите числа через пробел: ').split()))

print(f'Список: {numbers_lst}')

sorted_lst = []
numbers_lst.sort()
item = 0
while item < len(numbers_lst):
    col = numbers_lst.count(numbers_lst[item])
    if col > 1:
        for i in range(col):
            numbers_lst.remove(numbers_lst[item])
    else:
        sorted_lst.append(numbers_lst[item])
        numbers_lst.remove(numbers_lst[item])
print(f'Неповторяющиеся числа в списке: {sorted_lst}')