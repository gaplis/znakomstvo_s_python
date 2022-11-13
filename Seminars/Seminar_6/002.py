# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('task002_input.txt','r', encoding='utf-8') as input_file:
    input_data = input_file.readlines()[0]

with open('task002_output.txt','w', encoding='utf-8') as output_file:
    result = ''
    count = 0
    while True:
        for i in range(len(input_data)):
            if input_data[0] == input_data[i]:
                count += 1
            else:
                break
        if count > 9:
            temp = count
            while temp > 0:
                result += f'{9 if temp > 9 else temp}{input_data[0]}'
                temp -= 9
        else:
            result += f'{count}{input_data[0]}'
        input_data = input_data[count:]
        count = 0
        if len(input_data) == 0:
            break
    output_file.write(result)
print(f'Сжатая строка: {result}\n')
    #f'Размер файла {os.path.getsize('task002_output.txt')} Байт' Узнать что это???