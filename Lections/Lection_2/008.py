dictionary = {}
dictionary = \
    {
        'up': 'verh',
        'left': 'levo',
        'down': 'niz',
        'right': 'pravo'
    }

print(dictionary)
print(dictionary['right'])

for k in dictionary.keys():
    print(k)

for k in dictionary.values():
    print(k)

for v in dictionary:
    print(v)

for v in dictionary:
    print(dictionary[v])

print(dictionary['up'])
dictionary['up'] = 'VERH'
print(dictionary['up'])

del dictionary['left'] # удаление элемента

for item in dictionary:
    print('{}: {}'.format(item, dictionary[item]))