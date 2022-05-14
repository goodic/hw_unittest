documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}
commands = ["p – поиск человека по номеру документа",
            "s – поиск полки по номеру документа",
            "l – вывести список документов",
            "a – добавить новый документ",
            "d - удалить документ",
            "m - переместить документ на другую полку",
            "as - добавить новую полку",
            "q - выход"]
commands.sort()


def print_help(commands):
    for command in commands:
        print(command)


def get_document(documents, doc_number):
    for document in documents:
        if doc_number == document["number"]:
            return document
    return None


def get_doc_owner(documents, doc_number=None):
    if doc_number is None:
        doc_number = input("Введите номер документа: ")
    document = get_document(documents, doc_number)
    if document is not None:
        return document["name"]
    else:
        return None


def get_shelf(directories, doc_number):
    for directory, documents in directories.items():
        if doc_number in documents:
            return directory
    return None


def get_doc_shelf(directories, doc_number=None):
    if doc_number is None:
        doc_number = input("Введите номер документа: ")
    shelf = get_shelf(directories, doc_number)
    if shelf is not None:
        return shelf
    else:
        return None


def get_list(documents):
    for document in documents:
        print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')


def add_document(documents, directories):
    doc_number = input("Введите номер документа: ")
    doc_type = input("Введите тип документа: ")
    owner_name = input("Введите имя владельца: ")
    shelf_number = input("Введите номер полки: ")
    if shelf_number not in directories.keys():
        return False
    documents.append({"type": doc_type, "number": doc_number, "name": owner_name})
    directories[shelf_number].append(doc_number)
    return True


def remove_from_shelf(directories, doc_number):
    shelf = get_shelf(directories, doc_number)
    directories[shelf].remove(doc_number)


def del_doc(documents):
    doc_number = input("Введите номер документа: ")
    document = get_document(documents, doc_number)
    if document is not None:
        documents.remove(document)
        remove_from_shelf(directories, doc_number)
        return True
    else:
        return False


def move_document(documents, directories):
    doc_number = input("Введите номер документа: ")
    if get_document(documents, doc_number) is None:
        return False
    shelf_number = input("Введите номер полки: ")
    if shelf_number not in directories.keys():
        return False
    remove_from_shelf(directories, doc_number)
    directories[shelf_number].append(doc_number)
    return True


def add_shelf(directories):
    shelf_number = input("Введите номер новой полки: ")
    if shelf_number in directories.keys():
        return False
    directories.update({shelf_number: []})
    return True


def secretary_program_start():
    print("Добро пожаловать в Секретарь-3000")
    while 1:
        command = input("Введите команду: ")
        if command == "p":
            owner = get_doc_owner(documents)
            print(f'Владелец документа {owner}')
        elif command == "s":
            shelf = get_doc_shelf(directories)
            print(f'Документ находится на полке {shelf}')
        elif command == "l":
            get_list(documents)
        elif command == "a":
            if add_document(documents, directories):
                print('Документ добавлен')
            else:
                print('При добавлении документа произошла ошибка')
        elif command == "d":
            if del_doc(documents):
                print('Документ удален')
            else:
                print('При удалении документа произошла ошибка')
        elif command == "m":
            if move_document(documents, directories):
                print('Документ перемещен')
            else:
                print('При перемещении документа произошла ошибка')
        elif command == "as":
            if add_shelf(directories):
                print('Полка добавлена')
            else:
                print('При добавлении полкий произошла ошибка')
        elif command == "q":
            break
        else:
            print("Команда не найдена")
            print_help(commands)


if __name__ == '__main__':
    secretary_program_start()
