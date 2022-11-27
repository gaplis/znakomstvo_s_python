def menu():
    print('''
Меню действий:

|R| Отобразить базу
|W| Добавить запись в базу
|D| Удалить запись из базы
|E| Редактировать запись в базе
|Q| Выйти из приложения''')

def show_database(db):
    print()
    if db == False:
        database_here()
    elif db == True:
        database_empty()
    else:
        for i in db:
            print(*i)

def id_here():
    print('Этот id уже занят')

def database_here():
    print('Файла не существует')

def database_empty():
    print('Файл пустой')

def edit_menu():
    print('''
Что хотите изменить?:

|1| Номер телефона
|2| Номер класса
|Q| Выйти из меню редактирования''')

def id_not_found():
    print('Такого id не существует')