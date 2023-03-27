"""  Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.   """

# def numberA(a):
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return "нет"
#     return "да"
# print(numberA(int(input("число A = "))))

def power(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return power(a, b/2) * power(a, b/2)
    else:
        return a * power(a, b-1)

a = int(input("Введите число A: "))
b = int(input("Введите степень B: "))
print(power(a, b))