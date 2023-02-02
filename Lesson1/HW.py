# Задача 2: Найдите сумму цифр трехзначного числа.

# try:
#     input_number = int(input("Введите трехначное число: "))
#     result = int(input_number/100)
#     result2 = int((input_number/10)%10)
#     result3 = int(input_number%10)
# except:
#     print("Вы ввели не коректнные данные!")
#
# print(result+result2+result3)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
try:
    input_number = int(input("Введите общее количество журавликов: "))
    x = input_number // 6

    k = (x + x) * 2

    print("Петя сделал: " , x," журавликов, Катя сделала :" , k," журавликов, а Петя сделал :", x,"журавликов")

except:
    print("Вы ввели не коректнные данные!")

# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# number = str(input('введите номер билета: '))
# ticket = [int(x) for x in number]
# middle = len(ticket) // 2
#
# if sum(ticket[0:middle]) == sum(ticket[middle:]):
#     print('Билет счасливый!')
# else:
#     print('Сумма цифр на нем конечно не сходятся(но по секрету скажу каждый билет счасливый)')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один
# разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# n = int(input("Введите n: "))
# m = int(input("Веддите m: "))
# k = int(input("Введите к: "))
# if k < n * m and ((k % n == 0) or (k % m == 0)):
#     print('Можно ')
# else:
#     print('Нельзя')

# Задача 2: - HARD необязательная, идет за 3 обязательных Найдите сумму цифр любого вещественного или целого числа.
# Можно использовать decimal. Через строку решать нельзя.
# try:
#     input_number = float(input("Введите трехначное число: "))
# except:
#     print("Вы ввели не коректнные данные!")
#
# if(input_number<10):
#     input_number= input_number * 1000
#     result = float(input_number//1000)
#     result2 = float((input_number//100)%10)
#     result3 = float((input_number//10)%10)
#     print(input_number,result,result2,result3)
#     print(round(result + result2 + result3))
# elif(input_number>10 and input_number<99):
#     input_number = input_number * 100
#     result = float(input_number // 1000)
#     result2 = float((input_number // 100) % 10)
#     result3 = float((input_number // 10) % 10)
#     print(input_number, result, result2, result3)
#     print(round(result + result2 + result3))
# elif(input_number>100):
#     input_number = input_number
#     result = float(input_number // 100)
#     result2 = float((input_number // 10) % 10)
#     result3 = float(input_number % 10)
#     print(input_number, result, result2, result3)
#     print(round(result + result2 + result3))
