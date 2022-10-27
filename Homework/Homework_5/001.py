# Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "абв".

s = [i for i in str(input('Введите текст: ')).split()]

print(s)

res = []
for i in range(len(s)):
        if 'а' not in s[i] and 'б' not in s[i] and 'в' not in s[i]:
            res.append(s[i])

print(res)