# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите число: '))

array = [i for i in range(-n, n + 1)]
index = [45, 20, 4, 92, 10, 5, 79, 39, 63, 67, 2, 52, 83, 59, 18, 41, 11, 22, 90, 3]
power_numbers = 1
for i in index:
    if int(i) < len(array):
        power_numbers *= array[int(i)]
        print(power_numbers)
print(array, ', ', power_numbers)