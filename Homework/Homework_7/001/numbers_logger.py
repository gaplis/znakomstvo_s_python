import data_provider as dt

def numbers_data(data):
    phone, comment = data
    with open('numbers_log.csv', 'a') as file:
        file.write('{}; {}; {}; \n'
                    .format(dt.get_id() - 1, phone, comment))