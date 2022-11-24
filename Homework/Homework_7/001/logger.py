def user_data(data):
    id, n, f, db, pw = data
    with open('log.csv', 'a') as file:
        file.write('{}; {}; {}; {}; {} \n'
                    .format(id, n, f, db, pw))