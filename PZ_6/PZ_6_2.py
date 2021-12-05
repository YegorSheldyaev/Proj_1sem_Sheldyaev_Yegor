#2. Дан список A размера N. Сформировать новый список B того же размера по следующему правилу:
# элемент BK равен сумме элементов списка A с номерами от 1 до K.

import random

A = []
i = 0
b = random.randint(0, 20)

while i < b:
    A.append(random.randint(0, 20))
    i += 1
print(A)
a = len(A)
B = []
z = 0
l = 1

while z <= a - 1:
    B.append(sum(A[0: l]))
    z += 1
    l += 1
print(B)