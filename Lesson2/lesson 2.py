# Задача №9. Общее обсуждение
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

# n = int(input(" Vvedite chislo: "))
#
# i = 1
# sum = 1
#
# while i <= n:
#     sum *= i
#     i += 1
#
# print(sum)

# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# a = int(input("Vvedite A: "))
# n1 = 0
# n2 = 1
# i = 2
#
# while n2 <= a:
#     if n2 == a:
#         print(i)
#         break
#     n1, n2 =n2, n1+n2
#     i += 1
# else:
#         print("-1")

# Задача №13. Решение в группах
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

# import random
#
# try:
#     flag = True
#     number = int(input("Ввведите число: "))
#     while flag:
#         if number < 1 or number > 100:
#             print("Вы ввели не правильное число!")
#             number = int(input("Введите число: "))
#         else:
#             flag = False
#             print("Это число подходит!")
# except:
#     print("Вы ввели не коректные данные!")
#
#
# array = [0] * number
#
# for i in range(number):
#     array[i] = random.randint(-50, 50)
# print(array)

# count = max = 0
#
#
# for i in array:
#     if i > 0:
#         count += 1
#         if max<count:
#             max=count
#     else:
#         count = 0
# print("-")
# print(max)



