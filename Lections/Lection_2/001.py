colors = ['red', 'green', 'blue']
data = open('lection2_001-002.txt', 'a')
data.writelines(colors)
data.write('\nLine 2\n')
data.write('Line 3\n')
data.close()

# Другой вариант

with open('lection2_001-002.txt', 'a') as data:
    data.write('Line 4\n')
    data.write('Line 5\n')