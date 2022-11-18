import controller

def get_id():
    with open('log.csv', 'r') as file: 
        data = sum(1 for line in file) + 1
    return data

def get_name():
    print('Введите имя: ')
    data = controller.enter_data()
    return data

def get_family():
    print('Введите фамилию: ')
    data = controller.enter_data()
    return data

def get_birthday():
    print('Введите день рождения: ')
    data = controller.enter_data()
    return data

def get_place_work():
    print('Введите место работы: ')
    data = controller.enter_data()
    return data

def data_collection():
    return (get_id(), get_name(), get_family(), get_birthday(), get_place_work())