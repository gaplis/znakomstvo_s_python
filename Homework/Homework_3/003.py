# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# [1.1, 1.2, 3.1, 5, 10.01] => 0.2


lst = [1.1, 1.2, 3.1, 5, 10.01]

new_lst = []

# Это решение не подходит, так как получается [0.10000000000000009, 0.19999999999999996, 0.10000000000000009, 0, 0.009999999999999787]
# Но мне оно показалось интересным, из float вычитать int)

# for i in range(len(lst)):
#     res = lst[i]  - int(lst[i])
#     new_lst.append(res)
#
# print(new_lst)

# Хотя тут получается тот же результат

# for i in range(len(lst)):
#     res = lst[i] % 1
#     new_lst.append(res)
# 
# print(new_lst)

print('Исходный список:', lst)

for i in range(len(lst)):
    res = round(lst[i] % 1, 5) # округление до 5, чтобы с запасом, но для этой задачи хватило бы и 2)
    new_lst.append(res)

print('Список из чисел после запятой:', new_lst)

min_num, max_num = new_lst[0], new_lst[0]
for item in new_lst:
    if item < min_num:
        min_num = item
    elif item > max_num:
        max_num = item

print('Минимальное значение:', min_num)
print('Максимальное значение:', max_num)
print('Разница между максимальным и минимальным значением:', max_num - min_num)