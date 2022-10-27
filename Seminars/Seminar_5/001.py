# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

# with open('file001.txt', 'r') as data:
#     lst = list(map(int, data.read().split()))

with open('file001.txt', 'r') as data:
     lst = [int(i) for i in data.read().split()]

print(lst)

lst.sort()

print(lst)

for i in range(1, len(lst)):
    if lst[i] - 1 != lst[i - 1]:
        print(f'Не хватает {lst[i] - 1}')