# 1. Открыть файл <
# 2. Сохранить файл 
# 3. Показать ТК <
# 4. Добавить контакт <
# 5. Изменить контакт <
# 6. Удалить контакт <
# 7. Найти контакт <
# 8. Выход <

PATH = 'C:/Users/acer/Desktop/ПитонСеминары/8-ой семинар/tk.txt'

def main():
    print('Здравствуйте')
    while (True):
        com = input('Выберите команду и нажмите Enter\n'
                       '1 - Показать телефонную книгу\n'
                       '2 - Добавить контакт\n'
                       '3 - Найти контакт\n'
                       '4 - Изменить контакт\n'
                       '5 - Удалить контакт\n'
                       '8 - Выйти\n')
        if com == '1':
            show_tk()
            input("Нажмите Enter чтобы продолжить")
        elif com == '2':
            add_contact()
            input("Контакт добавлен, нажмите Enter чтобы продолжить")
        elif com == '3':
            find_contact()
            input("Нажмите Enter чтобы продолжить")
        elif com == '4':
            change_contact()
            input("Контакт изменен, нажмите Enter чтобы продолжить")
        elif com == '5':
            delete_contact()
            input("Контакт удален, нажмите Enter чтобы продолжить")
        elif com == '8':
            print('До свидания')
            break

def add_contact():
    data = open(PATH, 'a', encoding='UTF-8')
    name = input('Введите имя: ') 
    middlename = input('Введите фамилию: ') 
    lastname = input('Введите отчетсво: ')
    phone = input('Введите номер телефона: ')
    data.write(f"{name} {middlename} {lastname} - {phone}\n")
    data.close()

def show_tk():
    data = open(PATH, 'r', encoding='UTF-8')
    print(data.read())
    data.close()

def find_contact():
    flag = True
    data = open(PATH, 'r', encoding='UTF-8')
    contacts = data.readlines()
    search = input('Введите имя или телефон контакта: ')
    for item in contacts:
        if search in item:
            flag = False
            print(item)
    if(flag): print('Такого контакта не было найдено')
    data.close()

def change_contact():
    flag = True
    data = open(PATH, 'r', encoding='UTF-8')
    contacts = data.readlines()
    search = input('Введите имя или телефон контакта, который вы хотите изменить: ')
    for item in contacts:
        if search in item:
            flag = False
            print(item)
            new = input('Введите новые данные для контакта: ') + ('\n')
            data.close()
            with open(PATH, 'r', encoding='UTF-8') as file:
                file = file.read()
                changes = file.replace(item, new)
            with open(PATH, 'w', encoding='UTF-8') as file:
                file.write(changes)
    if(flag): 
        print('Такого контакта нет')
        data.close()

def delete_contact():
    flag = True
    data = open(PATH, 'r', encoding='UTF-8')
    contacts = data.readlines()
    search = input('Введите имя или телефон контакта, который вы хотите удалить: ')
    for item in contacts:
        if search in item:
            flag = False
            print(item)
            data.close()
            with open(PATH, 'r', encoding='UTF-8') as file:
                file = file.read()
                delete = file.replace(item, '')
            with open(PATH, 'w', encoding='UTF-8') as file:
                file.write(delete)
    if(flag): 
        print('Такого контакта нет')
        data.close()

main()