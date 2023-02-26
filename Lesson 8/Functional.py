import json
import random
from pprint import pprint

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

def add_person():
    person = {}
    person['id']=random.randint(1,1000)
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
    print(person)
    edit_person(person)
    write_new_person(person,"data.json")
    return person

def edit_person(person):
    while True:
        confirmation = input("Данные верны? (да/нет): ")
        if confirmation.lower() == "да":
            break
        elif confirmation.lower() == "нет":
            field = input("Какое поле нужно изменить (Фамилия/Имя/рабочий телефон/личный телефон/личная почта/рабочая почта): ")
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
    return person

filename = "data.json"

def edit_person_in_spravochnic():
    print("Список контактов")
    with open(filename, "r", encoding="utf-8") as file:
        existing_data = json.load(file)

    person_index = input("Введите id пользователя: ")
    for person in existing_data:
        if person['id'] == int(person_index):
            print(person)
            updated_person = edit_person(person)
            confirmation = input("Вы уверены, что хотите изменить данные пользователя? (да/нет): ")
            if confirmation.lower() == "да":
                person.update(updated_person)
                with open(filename, "w", encoding="utf-8") as file:
                    json.dump(existing_data, file, indent=3, ensure_ascii=False)
                    print("Данные пользователя обновлены")
            elif confirmation.lower() == "нет":
                print("Данные пользователя не обновлены")
            else:
                print("Некорректный ввод")
            break
    else:
        print("Пользователь с таким id не найден.")

def delete_person_in_spravochnic():
    print("Список контактов")
    with open(filename, "r", encoding="utf-8") as file:
        existing_data = json.load(file)

    person_index = input("Введите id пользователя: ")
    for i, person in enumerate(existing_data):
        if person['id'] == int(person_index):
            print(person)
            confirmation = input("Вы уверены, что хотите удалить данные пользователя? (да/нет): ")
            if confirmation.lower() == "да":
                existing_data.pop(i)
                with open(filename, "w", encoding="utf-8") as file:
                    json.dump(existing_data, file, indent=3, ensure_ascii=False)
                    print("Данные пользователя удалены")
            elif confirmation.lower() == "нет":
                print("Данные пользователя не удалены")
            else:
                print("Некорректный ввод")
            break
    else:
        print("Пользователь с таким id не найден.")