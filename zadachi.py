# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list = [6, 15, 2, 8, 7, 26, 49]
# sum = 0
# for i in range(len(list)):
#     if i %2 != 0:
#         sum += list[i]
# print(sum)

# 2. 2.Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# list = [2, 3, 4, 5, 6]
# result = []
# for i in range((len(list)+1)//2):
#     result.append(list[i]*list[len(list)-1-i])
# print(result)

#  3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list = [1.1, 1.2, 3.1, 5, 10.01]
# max, min = 0, 1
# for i in list:
#     if (divmod(i, 1))[1] > max:
#         max = divmod(i, 1)[1]
#     elif (divmod(i, 1))[1] < min and (divmod(i, 1))[1] != 0:
#         min = (divmod(i, 1))[1]
# print(round(max - min, 2))

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# n = int(input('Введите число: '))
# number = ''
# while n > 0:
#     number = number + str(n % 2)
#     n = n // 2
# print(number)


#  5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# #- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input('Введите число: '))
def fibonachi(num):
    fibo = []
    n1, n2 = 1, 1
    for _ in range(num):
        fibo.append(n1)
        n1, n2 = n2, n1 + n2
    n1, n2 = 0, 1
    for _ in range(num+1):
        fibo.insert(0, n1)
        n1, n2 = n2, n1 - n2
    return fibo
print(fibonachi(number))
# 