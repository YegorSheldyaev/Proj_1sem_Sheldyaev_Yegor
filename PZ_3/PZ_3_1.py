#Даны целые числа a, b, c, являющиеся сторонами некоторого треугольника.
# Проверьте истинность высказывания:"Треугольник со сторонами a, b, c, является равносторонним".

a = input("Введите целое число для стороны a")

while type(a) != int:#Проверка
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите целое число для стороны a")

b = input("Введите целое число для стороны b")

while type(b) != int:#Проверка
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите целое число для стороны b")

c = input("Введите целое число для стороны c")

while type(c) != int:#Проверка
    try:
        c = int(c)
    except ValueError:
        print("Неправильно ввели!")
        c = input("Введите целое число для стороны c")

if a == b == c:
    print("Треугольник равносторонний")
else:
    print("Треугольник не равносторонний")