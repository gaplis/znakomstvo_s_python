# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

N = int(input('Введиче число N: '))

d = {i : 3 * i + 1 for i in range(1, N + 1)}
print(f"Итоговая послежовательность: {d}")

dct = {}
for i in range(1, N + 1):
    dct[i] = 3 * i + 1

print(f' Для N = {N}: ', dct)