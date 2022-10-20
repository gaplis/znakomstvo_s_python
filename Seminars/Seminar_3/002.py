# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

def second_enter(lst, fnd):
    count = 0
    for i in range(len(lst)):
        if lst[i] == fnd:
            count += 1
            if count == 2:
                return i
    return -1

lst1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
lst2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
lst3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
lst4 = ["123", "234", 123, "567"]
lst5 = []

fnd1 = "qwe"
fnd2 = "йцу"
fnd3 = "йцу"
fnd4 = "123"
fnd5 = "123"

print(second_enter(lst1, fnd1))
print(second_enter(lst2, fnd2))
print(second_enter(lst3, fnd3))
print(second_enter(lst4, fnd4))
print(second_enter(lst5, fnd5))