import controller

def get_numbers():
        print('Введите номер телефона: ')
        data = controller.enter_data()
        return data

def get_comment():
        print('Введите комментарий: ')
        data = controller.enter_data()
        return data

def data_collection():
    return (get_numbers(), get_comment())