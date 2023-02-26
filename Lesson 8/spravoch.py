import json
import Functional as func
from pprint import pprint
print("Телефонный справочник")

person_help={
    'h':"Справка",
    'Q':"Выход",
    '1':"Вывести весь список",
    '2':"Добавить в список пользователя",
    '3':"Удалить пользователя",
}

def read(filename):
    # читаем существующие данные из файла
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def write_new_person(data, filename):
    with open(filename, "r", encoding="utf-8") as file:
        # читаем существующие данные из файла
        existing_data = json.load(file)

    # добавляем нового человека к существующим данным
    existing_data.append(data)

    with open(filename, "w", encoding="utf-8") as file:
        # записываем обновленные данные в файл
        json.dump(existing_data, file, indent=3, ensure_ascii=False)

def redaction_person(data,filename):
    # читаем существующие данные из файла
    with open("data.json", "r", encoding="utf-8") as file:
        existing_data = json.load(file)

while True:

    cmd = input("Ввведите команду( > h справка, > Q завершить,> 1 Вывести весь список, > 2 Добавить в список пользователя, > 3 Удалить пользователя)\n> ")
    if cmd !="h" and cmd != "s" and cmd != "q" and cmd != "Q" and cmd != "1"and cmd != "2":
        print("Введена не верная команда!")
    if cmd == "1":
        pprint(read("data.json"))
    if cmd == "2":
        person = {}

        person['Фамилия'] = input("Введите фамилию: ")
        person['Имя'] = input("Введите имя: ")

        phones = {}
        phones['рабочий телефон'] = input("Введите рабочий телефон: ")
        phones['личный телефон'] = input("Введите личный телефон: ")
        person['телефоны'] = phones

        emails = {}
        emails['личная почта'] = input("Введите личный адрес электронной почты: ")
        emails['рабочая почта'] = input("Введите рабочий адрес электронной почты: ")
        person['почта'] = emails

        print("Данные внесены в словарь:")
        print(person)
        while True:
            confirmation = input("Данные верны? (да/нет): ")
            if confirmation.lower() == "да":
                break
            elif confirmation.lower() == "нет":
                field = input(
                    "Какое поле нужно изменить (Фамилия/Имя/рабочий телефон/личный телефон/личная почта/рабочая почта): ")
                if field.lower() == "фамилия":
                    person['Фамилия'] = input("Введите фамилию: ")
                    print(person)
                elif field.lower() == "имя":
                    person['Имя'] = input("Введите имя: ")
                    print(person)
                elif field.lower() == "рабочий телефон":
                    person['телефоны']['рабочий телефон'] = input("Введите рабочий телефон: ")
                    print(person)
                elif field.lower() == "личный телефон":
                    person['телефоны']['личный телефон'] = input("Введите личный телефон: ")
                    print(person)
                elif field.lower() == "личная почта":
                    person['почта']['личная почта'] = input("Введите личный адрес электронной почты: ")
                    print(person)
                elif field.lower() == "рабочая почта":
                    person['почта']['рабочая почта'] = input("Введите рабочий адрес электронной почты: ")
                    print(person)
                else:
                    print("Некорректное поле")
            else:
                print("Введите 'да' или 'нет'")

        print("Данные внесены в словарь:")
        write_new_person(person,"data.json")
        print(person)
    if cmd == "h" or cmd == "H":
        pprint(person_help)
    if cmd == "Q" or cmd == "q":
        print("Программа прекращает свою работу!")
        break





