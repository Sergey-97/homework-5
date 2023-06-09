""" Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.  """

def sum(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    elif a > b:
        return sum(a+1, b-1)
    else:
        return sum(a-1, b+1)
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print("Сумма чисел равна:", sum(a, b))

# def sum(a, b):
#     if b == 0:
#         return a
#     elif a == 0:
#         return b
#     elif a > b:
#         return sum(a-b, b+a)
#     else:
#         return sum(a+b, b-a)
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# print("Сумма чисел равна:", sum(a, b))