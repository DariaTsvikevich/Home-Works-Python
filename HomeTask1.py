# Задача 2: Найдите сумму цифр трехзначного числа
""""
n = input("Введите трехзначное число: ")
n = int(n)
d1 = n % 10
d2 = n % 100 // 10
d3 = n // 100
print("Сумма цифр числа:", d1 + d2 + d3)
"""

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
"""
s = int(input("Введите общее количество журавликов: "))
print((s//6), ((s//6)*4), (s//6))
"""

# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
"""n = str(input("Введите номер билета: "))
s1 = n[0] + n[1] + n[2]
s2 = n[3] + n[4] + n[5]
if (s1 == s2): print ("Билет счастливый!")
else: print ("Билет не счастливый.")
"""

#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку 
# на два прямоугольника).
"""n = int(input("Введите n: "))
m = int(input("Введите m: "))
k = int(input("Введите k: "))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print("Можно")
else:
    print("Нельзя")
"""