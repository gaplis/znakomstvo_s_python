# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# Функция для решения с функцией
def find_num(lst):    
    for item in lst:
        if n in item:
            return True
    return False

lst = ['f54g45g54g54hg54', 'f43ferf34f43f43', 'g4gtrg45gr3h76jh']
print(lst)

n = input('Введите искомое число: ')

# Решение с функцией
if find_num(lst) == True:
    print('Yes')
else:
    print('No')

# Просто if-else
for item in lst:
        if n in item:
            print('Yes')
            break
else:
    print('No')

# Решение через join
print('Да' if n in ' '.join(lst) else 'Нет')