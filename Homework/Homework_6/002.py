# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности, 
# список повторяемых и убрать дубликаты из заданной последовательности.
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и  [1, 3, 5] и [1, 2, 5, 3, 10]


lst = [1, 2, 3, 5, 1, 5, 3, 10]

res = {i: 0 for i in set(lst)}
for i in lst:
    res[i] += 1
print(res)
print(lst)
print(list(filter(lambda x: res[x] == 1, res)))
print(list(filter(lambda x: res[x] > 1, res)))
print(list(set(lst)))