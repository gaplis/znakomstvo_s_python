colors = {'red', 'green', 'blue'}

print(colors)
colors.add('red')
print(colors)
colors.add('gray')
print(colors)
colors.remove('red')
print(colors)
# colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok
print(colors)
colors.clear()
print(colors)