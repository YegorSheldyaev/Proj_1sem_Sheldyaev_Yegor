# . В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в
# 2 раза.
from random import randint

rows = int(input('Введите количество строк: '))
cols = int(input('Введите количество столбцов: '))

matrix = [[randint(0, 20) for j in range(cols)] for i in range(rows)]
print(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            matrix[i][j] = matrix[i][j]
        else:
            matrix[i][j] *= 2

print(matrix)
