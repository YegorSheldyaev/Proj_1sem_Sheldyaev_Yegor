#Даны строки S и S0. Проверить, содержится ли строка S0 в строке S. Если содержится,
#то вывести TRUE, если не содержится, то вывести FALSE.

S = input ("Введите первую строку>>>")
S0 = input ("Введите вторую строку>>>")

a = S0 in S
print(a)