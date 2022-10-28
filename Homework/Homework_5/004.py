# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle(string):
    res = []
    count = 0
 
    if len(string) == 1:
        res.append((1, string[0]))
        return res
 
    for i in range(len(string)):
        count += 1
        if (i + 1) == len(string) or string[i] != string[i + 1]:
            res.append((count, string[i]))
            count = 0
            
    return res

with open('file004_1.txt', 'r') as data1:
    string = data1.readline()
    
res = rle(string)   
print(res)
with open('file004_2.txt', 'w') as data2:   
    for amount, figure in res:
        print(amount, figure)
        i = [amount, figure]
        data2.write(f'{str(amount)}\n')
        data2.write(f'{figure}\n')
        
     
# С восстановлением данных у меня возникли некоторые проблемы, не совсем понял что не так, и split не работает, 
# и перебор также как-то не получился, так же почему при выводе получается ['12\n', 'q\n', '8\n', 'w\n', '5\n', 'q\n'], 
# хотя в самом файле \n нет)

exit()
with open('file004_2.txt', 'r') as data3:   
    new_string = []
    for line in data3:
            new_string.append(line)

print(new_string)
with open('file004_3.txt', 'w') as data4:   
    for amount, figure in new_string:
        while i < amount:
            data4.write(figure)

