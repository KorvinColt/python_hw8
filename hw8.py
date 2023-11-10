import os

def print_data():
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        phonebook_str = file.read()
    print(phonebook_str)
    print()

def input_name():
    return input("Введите имя контакта: ").title()

def input_surname():
    return input("Введите фамилию контакта: ").title()

def input_patronymic():
    return input("Введите отчество контакта: ").title()

def input_phone():
    return input("Введите номер телефона контакта: ")

def input_address():
    return input("Введите адрес контакта: ").title()

def input_data():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    my_sep = " "
    return f"{surname}{my_sep}{name}{my_sep}{patronymic}{my_sep}{phone}\n{address}\n\n"

def add_contact():
    new_contact_str = input_data()
    with open("phonebook.txt", "a", encoding="utf-8") as file:
        file.write(new_contact_str)

def search_contact():
    print("Варианты поиска:\n"
        "1. По фамилии\n"
        "2. По имени\n"
        "3. По отчеству\n"
        "4. По телефону\n"
        "5. По адресу\n"
        "6. Изменить контакт\n"
        "7. Удалить контакт\n")
    command = input("Выберите вариант: ")
      
    while command not in ("1", "2", "3", "4", "5", "6", "7"):
        print("Некорректный ввод, повторите запрос")
        command = input("Выберите вариант: ")
    
    i_search = int(command)-1
    search = input("Введите данные для поиска: ").lower()
    print()
    
    with open("phonebook.txt","r", encoding="utf-8") as file:
        contacts_list = file.read().rstrip().split("\n\n")
    
    check_cont = False
    for index, contact_str in reversed(list(enumerate(contacts_list))):
        lst_contact = contact_str.lower().replace("\n", " ").split()
        if len(lst_contact) > i_search and search in lst_contact[i_search]:
            print(contact_str)
            print()
            check_cont = True

            if command in ("6", "7"):
                if command == "6":  # Изменить контакт
                    new_contact_str = input_data()
                    contacts_list[index] = new_contact_str
                elif command == "7":  # Удалить контакт
                    del contacts_list[index]

    if not check_cont:
        print("Такого контакта нет")

    # Перезаписываем обновленные данные в файл
    with open("phonebook.txt", "w", encoding="utf-8") as file:
        file.write("\n\n".join(contacts_list))

def interface():
    with open("phonebook.txt", "a", encoding="utf-8"):
        pass
    command = ""
    os.system("cls")
    while command != "4":
        print(
            "Меню пользователя:\n"
            "1. Ввод данных на экран\n"
            "2. Добавить контакт\n"
            "3. Поиск контактов\n"
            "4. Выход\n"
        )
        command = input("Выберите пункт меню: ")
      
        while command not in ("1", "2", "3", "4"):
            print("Некорректный ввод, повторите запрос")
            command = input("Выберите пункт меню: ")

        match command:
            case "1":
                print_data()
            case "2":
                add_contact()
            case "3":
                search_contact()
            case "4":
                print("Завершение программы")
        print()

if __name__ == "__main__":
    interface()