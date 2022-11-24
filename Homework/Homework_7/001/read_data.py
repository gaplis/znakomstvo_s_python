def read_file():
    print('Данные в файле: ')
    with open('log.csv', 'r') as file:
        for line in file:
            print(line)
    return

def read_numbers_file():
    print('Телефоны пользователей по ID: ')
    with open('numbers_log.csv', 'r') as file:
        for line in file:
            print(line)
    return