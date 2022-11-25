import os.path
import os
import controller
from logger import LOG

def get_db():
    if check_file():
        if os.stat("student_data.csv").st_size != 0:
            with open('student_data.csv', 'r', encoding='utf-8') as file:
                result = []
                for i in file:
                    result.append(i.rstrip().split(','))
            return result
        else: 
            return True
    else: 
        return False

@LOG
def add_student(contact):
    """Добавлена запись"""
    with open('student_data.csv', 'a', encoding='utf-8') as file:
        if os.stat("student_data.csv").st_size == 0 or not check_file():
            file.write('id,First name,Last name,Second name,Date of birthday,Phone number,Class')
            file.write('\n')
        line = ','.join(contact)
        file.write(line)
        file.write('\n')

@LOG
def remove_student(id):
    """Удалена запись"""
    full_db = get_db()
    new_db = []
    for row in full_db:
        if row[0] != id:
            new_db.append(row)

    with open('student_data.csv', 'w', encoding='utf-8') as file:
        for i in new_db:
            file.write(','.join(i))
            file.write('\n')

def check_id(id):
    full_db = get_db()
    if check_file():
        if os.stat("student_data.csv").st_size != 0:
            for row in full_db:
                if row[0] == id:
                    return True
    else: 
        return id

def check_file():
    return os.path.isfile('student_data.csv')

# @LOG
def edit_student(id, edit):
    # """Изменена запись"""
    full_db = get_db()
    new_db = []
    id_not_found = False
    for row in full_db:
        if row[0] != id:
            new_db.append(row)
        elif row[0] == id:
            row[edit] = controller.enter_edit(edit)
            new_db.append(row)
            id_not_found = True

    with open('student_data.csv', 'w', encoding='utf-8') as file:
        for i in new_db:
            file.write(','.join(i))
            file.write('\n')
            
    return id_not_found