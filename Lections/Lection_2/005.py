def concatenatio(*params):
    res: str = "" # Прописывание данных (str, int) (указание не обязательное)
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w'))
print(concatenatio('a', '1'))
# print(concatenatio(1, 2, 3, 4)) TypeError: can only concatenate str (not "int") to str