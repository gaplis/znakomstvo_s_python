# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

s1 = input('Строка 1 = ')
s2 = input('Строка 2 = ')

print(s1.count(s2))

inkrement = 0
for i in range(len(s1)):
    if s2 in s1[i: i + len(s2)]:
        inkrement += 1
print(inkrement)