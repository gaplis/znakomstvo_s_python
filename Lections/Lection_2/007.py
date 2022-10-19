a = (3, 4, 5)
print(a)
print(a[0])
print(a[-1])

for item in a:
    print(item)

t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))