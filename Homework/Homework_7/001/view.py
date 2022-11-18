import controller
import read_data as read
import data_provider as dt

def start():
    print('Выбор операции:')
    while True: 
        print('w - запись;')
        print('r - чтение;')
        print('q - выход;')
        change = controller.enter_operation()
        if change == 'w' or change == 'ц':
            print(f'ID нового пользователя: {dt.get_id()}')
            controller.user_data()
        elif change == 'r' or change == 'к':
            read.read_file()
            read.read_numbers_file()
        elif change == 'q' or change == 'й':
            quit()
        else: print('Повторите попытку.')