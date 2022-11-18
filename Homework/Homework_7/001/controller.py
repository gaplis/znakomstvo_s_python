import data_provider as dt
import logger as log
import numbers_data as nd
import numbers_logger as num_log

def enter_operation():
    enter = input('Какая вам необходима?: ').lower()
    return enter

def enter_data():
    enter = input()
    return enter

def user_data():
    data = dt.data_collection()
    log.user_data(data)
    while True:
        ask = input('Есть ещё номера? (y/n): ').lower()
        if ask == 'y' or ask == 'n' or ask == 'н' or ask == 'т':
            if ask == 'y' or ask == 'н':
                num_data = nd.data_collection()
                num_log.numbers_data(num_data)
            else: 
                break
        else: print('Попробуйте ещё.')
    return