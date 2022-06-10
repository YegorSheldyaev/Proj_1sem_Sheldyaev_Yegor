#Составить генератор (yield), который преобразует все буквенные символы в
#заглавные.

a = input("Введите текст: ")


def text(c):
    yield c.upper()


a = list(text(a))
print("Новый текст: ", end='')
print(*a)
