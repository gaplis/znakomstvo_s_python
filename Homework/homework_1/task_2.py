# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

result = []
for x in range(2):
    for y in range(2):
        for z in range(2):
            result.append(not (x or y or z) == (not x and not y and not z))

for i in result:
    if result[0] != i:
        print("Не верно")
        break
else:
    print("Верно")