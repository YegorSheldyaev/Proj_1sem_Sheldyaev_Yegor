#Даны четыре целых числa, одно из которых отлично от трех других,
#равных между собой. Определить порядковый номер числа,
#отличного от остальных.

print("Данная программа найдет какое число по порядку отлично от других")

a = input("Введите первое целое число")

while type (a) != int:#Проверка
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели число!")
        a = input("Введите первое целое число")

b = input("Введите второе целое число")

while type (b) != int:#Проверка
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели число!")
        b = input("Введите второе целое число")

c = input("Введите третье целое число")

while type (c) != int:#Проверка
    try:
        c = int(c)
    except ValueError:
        print("Неправильно ввели число!")
        c = input("Введите третье целое число")

d = input("Введите четвертое целое число")

while type (d) != int:#Проверка
    try:
        d = int(d)
    except ValueError:
        print("Неправильно ввели число!")
        d = input("Введите четвертое целое число")

if a != b == c == d:
    print ("Первое число отличается от остальных")
elif b!= a == c == d:
    print("Второе число отличается от остальных")
elif c != a == b == d:
    print("Третье число отличается от остальных")
elif d != a == b == c:
    print("Четвертое число отличается от остальных")
elif d == a == b == c:
    print("Числа равны")
else:
    print("Более чем одно число отличается от других")