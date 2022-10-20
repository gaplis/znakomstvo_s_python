# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

lst1 = [2, 3, 4, 5, 6]
lst2 = [2, 3, 5, 6]

def power_num(lst):
    new_lst = []

    if len(lst) % 2 == 0:
        size = len(lst) / 2
    else:
        size = (len(lst) + 1) / 2

    for i in range(int(size)):
        result = lst[i] * lst[-i - 1]
        new_lst.append(result)
    return new_lst

print(lst1, '->', power_num(lst1))
print(lst2, '->', power_num(lst2))