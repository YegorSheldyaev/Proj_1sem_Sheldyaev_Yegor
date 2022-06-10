# Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.
from random import randint

rows = int(input('Введите количество строк: '))
cols = int(input('Введите количество столбцов: '))

matrix = [[randint(0, 20) for j in range(cols)] for i in range(rows)]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > 10:
            matrix[i][j] = 0

print(matrix)
