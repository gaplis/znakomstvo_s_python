import view
import model

def run():
    running = True
    while running:
        view.menu()
        user_choice = ''
        while not user_choice:
            user_choice = input('\nВыберите действие: ').lower()
            match user_choice:
                case 'r':
                    db = model.get_db()
                    view.show_database(db)
                case 'w':
                    id = ''
                    while True:
                        id = input('Введите id ученика: ')
                        if model.check_id(id) == True:
                            view.id_here()
                        else: 
                            break 
                    f_name = input('Введите имя ученика: ')
                    l_name = input('Введите фамилию ученика: ')
                    s_name = input('Введите отчество ученика: ')
                    date_birth = input('Введите дату рождения: ')
                    phone = input('Введите телефон: ')
                    class_num = input('Введите номер класса: ')
                    contact = [id, f_name, l_name, s_name, date_birth, phone, class_num]
                    model.add_student(contact)
                case 'd':
                    remove_id = input('Введите id ученика для удаления: ')
                    model.remove_student(remove_id)
                case 'e':
                    edit_id = input('\nВведите id ученика для редактирования: ')
                    edit_work = choice_edit()
                    if edit_work == False:
                        break
                    else:
                        if model.edit_student(edit_id, edit_work) == False:
                            view.id_not_found()
                case 'q':
                    running = False

def choice_edit():
    choise = True
    while choise:
        view.edit_menu()
        user_edit_choice = ''
        while not user_edit_choice:
            user_edit_choice = input('\nВыберите действие: ').lower()
            match user_edit_choice:
                case '1':
                    return 5
                case '2':
                    return 6
                case 'q':
                    choise = False
                    return False

def enter_edit(edit):
    if edit == 5:
        return input('Введите телефон: ')
    elif edit == 6:
        return input('Введите номер класса: ')