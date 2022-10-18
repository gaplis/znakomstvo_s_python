# Реализуйте алгоритм перемешивания списка.

from random import randint

array = [i for i in range(10)]
print(array)
for i in range(len(array)):
    random_num = randint(0, 9)
    array[i], array[random_num] = array[random_num], array[i]
print(array)