value = None
print(type(value))
a = 123
b = 1.23
print(type(a))
print(type(b))
value = 12345
print(type(value))
s = 'qwe \'rt \ny'
print(s) # вывод строки
print(a, '-', b, '-', s)
print('{} - {} - {}'.format(a, b, s))
print(f'{a} - {b} - {s}')
print('{1} - {2} - {0}'.format(a, b, s))

f = True
print(f)