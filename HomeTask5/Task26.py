#Задача 26: Напишите программу, которая на вход принимает
#два числа A и B, и возводит число А в целую степень B с
#помощью рекурсии.
number = int(input("Введите число: "))
degree = int(input("Введите его степень: "))
def exp(number, degree):
    if (degree == 1):
        return (number)
    if (degree != 1):
        return (number * exp(number, degree - 1))

print("Результат:", exp(number, degree))
