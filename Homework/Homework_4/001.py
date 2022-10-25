# Вычислить число c заданной точностью d
# при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)

from decimal import Decimal

num = Decimal(input('Введите число: '))
print(num)
d = Decimal(input('Точность числа: '))
print(d)

res = num.quantize(Decimal(d))
print(res)