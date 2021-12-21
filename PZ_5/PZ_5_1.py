#Составьте функцию, которая выполнит суммирования числового ряда.
import random
def Sum():
    a = [random.randint(0, 20) for i in range(10)]
    b = sum(a)
    print(b)

Sum()