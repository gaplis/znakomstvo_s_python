# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def checkup(num, lst):
    if num in lst:
        return True
    for j in range(2, num // 2):
        if num % j == 0:
            return False
    else:
        if num not in lst:
            lst.append(num)
        return True


number = int(input("Введите число: "))
result_lst = []
multiplier = 2
num = number
while num != 1:
    if num % multiplier == 0:
        if checkup(multiplier, result_lst):
            num //= multiplier
        else:
            multiplier += 1
    else:
        multiplier += 1
    print(num)
print(f"Число {number} имеет следующие простые множители: {result_lst}")
