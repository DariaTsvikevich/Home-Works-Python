#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
#повторениями). Выдать без повторений в порядке возрастания все те числа, которые
#встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
#элементов второго множества. Затем пользователь вводит сами элементы множеств
n = (int(input("Введите число элементов N: ")))
list1=[]
for i in range(n):
    num = int(input("Введите num "))
    list1.append(num)
print(list1)

m = (int(input("Введите число элементов M: ")))
list2 = []
for i in range(m):
    num = int(input("Введите num "))
    list2.append(num)
print(list2)

list3 = list1 + list2

list3.sort()
print(list3)

for i in list3:
    while list3.count(i) > 1:
        list3.remove(i)
print (list3)