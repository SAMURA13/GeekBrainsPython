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
    '4':"Редактировать пользователя"
}
while True:

    cmd = input("Ввведите команду( > h справка, > Q завершить,> 1 Вывести весь список, > 2 Добавить в список пользователя, > 3 Удалить пользователя , > 4 Редактировать пользователя в телефонном справочнике) \n> ")
    if cmd !="h" and cmd != "s" and cmd != "й" and cmd != "q" and cmd != "1"and cmd != "2"and cmd != "4":
        print("Введена не верная команда!")
    if cmd == "1":
        pprint(func.read("data.json"))
    if cmd == "2":
        func.add_person()
    if cmd == "3":
        func.delete_person_in_spravochnic()
    if cmd == "4":
        func.edit_person_in_spravochnic()
    if cmd == "h" or cmd == "H":
        pprint(person_help)
    if cmd == "q" or cmd == "й":
        print("Программа прекращает свою работу!")
        break