#Описать функцию Minmax(X, Y), записывающую в переменную X минимальное
# из значений X и Y, а в переменную Y — максимальное из этих значений
# (X и Y — вещественные параметры, являющиеся одновременно входными и выходными).
# Используя четыре вызова этой функции, найти минимальное
# и максимальное из данных чисел A, B, C, D.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

m = []
n = []

def MinMax(x, y):
    x = min(x, y)
    y = max(x, y)
    n.append(x)
    m.append(y)

MinMax(a,b)
MinMax(c,d)

print(min(n), max(m))
