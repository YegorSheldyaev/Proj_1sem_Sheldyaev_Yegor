# Даны средние значения температур за каждый месяц в году. Найти минимальное
# и максимальное значения температур за год. Вывести значения температур по временам
# года.

import random


def MN(t):
    n = 3
    s = []
    for i in range(n):
        x = random.randint(10, 40)
        s.append(x)
        t.append(x)
    return s


t = []

print("Температуры зимой")
output = MN(t)
print(output)

print("Температуры весной")
output = MN(t)
print(output)

print("Температуры летом")
output = MN(t)
print(output)

print("Температуры осенью")
output = MN(t)
print(output)

print(f'Минимальная температура за год: {min(t)}\nМаксимальная температура за год: {max(t)}')
