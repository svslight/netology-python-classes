# Домашнее задание из лекции 1.4 «Функции — использование встроенных и создание собственных»
# Задача №1
# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца
#      и номер полки, на котором он будет храниться.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название,
# передающие её действие.

# Задача №2
# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;

# Список. Каталог документов
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
# Словарь. Перечень полок, на которых находятся документы
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

print('\nРабота с архивом!')


# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
def people_document(arg_number):
    for doc_number in documents:
        if doc_number["number"] == arg_number:
            print(' Владелец документа: ', doc_number["name"])
            break
    else:
        print('  Внимание! Такого документа - нет в архиве.')


# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
def list_documents():
    for document in documents:
        print('{} "{}" "{}"'.format(document['type'], document['number'], document['name']))


# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
def shelf_number(arg_number):
    shelf_break = False
    for shelf_directory in directories.items():
        for doc_number in shelf_directory[1]:
            if doc_number == arg_number:
                print('Данный документ находится на полке - ', shelf_directory[0])
                shelf_break = True
                break
        if shelf_break == True:
            break
    else:
        print('  Внимание! Документа нет на полке.')


# a – add – команда, которая добавит новый документ в каталог и в перечень полок,
# спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
def add_new_document(agr_type, arg_number, arg_name, arg_dir_number):
    if int(arg_dir_number) == 1 or int(arg_dir_number) == 2 or int(arg_dir_number) == 3:
        documents.append({"type": agr_type, "number": arg_number, "name": arg_name})
        directories[arg_dir_number].append(arg_number)
        print('\n  Ваш документ добавлен в Архив!')
    else:
        print('\n  Внимание! Такой полки не существует.')


# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
def del_document(arg_number):
    break_p = False
    for document in documents:
        if document['number'] == arg_number:
            document['number'] = 'Удален'
            for directory_value in directories.values():
                if arg_number in directory_value:
                    directory_value.remove(arg_number)
                    print('\n  Номер документа удален из каталога и полки!')
                    break_p = True
                    break
            if break_p == True:
                break
    else:
        print('\n  Внимание! Такого документа - нет.')


# m – move – команда, которая спросит номер документа и целевую полку
# и переместит его с текущей полки на целевую; values
def move_document(arg_number, arg_another_shelf):
    for directory_value in directories.values():
        if arg_number in directory_value:
            directory_value.remove(arg_number)
            directories[arg_another_shelf].append(arg_number)
            print('\n  Документ перемещён на указанную полку!')
            break
    else:
        print('\n  Внимание! Такого документа - нет, введите номер правильно.')


# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;
def add_shelf_num(arg_new_shelf):
    if int(arg_new_shelf) == 1 or int(arg_new_shelf) == 2 or int(arg_new_shelf) == 3:
        print('Такая полка уже есть!')
    else:
        new_dict = {arg_new_shelf: []}
        directories.update(new_dict)
        print('\n  Полка добавлена.')


# Вывести имена всех владельцев документов.
# С помощью исключения KeyError проверить, есть ли поле "name" и "number".
def print_name(arg_key):
    for document in documents:
        try:
            if arg_key == 'name' and document[arg_key]:
                print(' {} - "{}" '.format(document[arg_key], document["number"]))
            elif arg_key == 'number' and document[arg_key]:
                print(' {} - "{}" '.format(document['name'], document[arg_key]))
            else:
                print(' {} '.format(document[arg_key]))
        except KeyError:
            print('Внимание!!! Введенный Ключ не наден.')


# Печать архива
def print_document_from_archive():
    print('\nКаталог документов.')
    for document in documents:
        print('  {0} "{1}" "{2}"'.format(document['type'], document['number'], document['name']))

    print('\nПеречень полок, на которых находятся документы.')
    for num_shelf, doc_num in directories.items():
        print('  Полка №', num_shelf, doc_num)


# Основное меню для запуска команд
def main_menu():
    while True:
        command = input('\n \
    Выберете одну из команд: p, l, s, a, d, m, as, pn \n \
    Для выхода наберите: exit или q \n \
    Для вызова справки наберите: help или h \n \
    Введите команду: ')
        if command == 'p':
            people_document(input('\nВведите номер документа:'))
        elif command == 'l':
            list_documents()
        elif command == 's':
            shelf_number(input('\nВведите номер документа:'))
        elif command == 'a':
            add_new_document(input('\nВведите тип документа (passport,invoice,insurance...):'),
                             input('Введите номер документа: '), input('Введите имя: '),
                             input('Введите номер полки (1, 2, 3): '))
            print_document_from_archive()
        elif command == 'd':
            del_document(input('\nВведите номер документа:'))
            print_document_from_archive()
        elif command == 'm':
            move_document(input('\nВведите номер документа:'),
                          input('Введите номер полки, куда перенести документ: '))
            print_document_from_archive()
        elif command == 'as':
            add_shelf_num(input('\nДобавить новую полку. Введите номер:'))
            print_document_from_archive()
        elif command == 'pn':
            print_name(input('\nВведите ключ документа, чтобы вывести имена всех владельцев документов: '))
        elif command == 'exit' or command == 'q':
            break
        elif command == 'help' or command == 'h':
            print('\n \
    p – команда, которая по номеру документа выведет имя, владельца;\n \
    l – команда, которая выведет список всех документов;\n \
    s – команда, которая по номеру документа выведет номер полки, на которой он находится;\n \
    a – команда, которая добавит новый документ в архив;\n \
    d - команда, которая по номеру документа удалит его из каталога и из перечня полок;\n \
    m - команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;\n \
    as - команда, которая спросит номер новой полки и добавит ее в перечень;\n \
    pn - команда, которая по ключу выведет имена всех владельцев документов.')
        else:
            print('Вы ввели команду не корректно, повторите ввод.')


main_menu()
