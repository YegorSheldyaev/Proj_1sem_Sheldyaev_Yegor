#Из предложенного текстового файла (text18-30.txt) вывести на экран его содержимое,
#количество знаков препинания. Сформировать новый файл, в который поместить текст в
#стихотворной форме предварительно поставив после последней строки автора и название
#произведения.

f = open("text18-30.txt", "r", encoding="utf-8")
s = f.read()
print(s)
print()
f.close()

f = open("text18-30.txt", "r", encoding="utf-8")
i = 1
b = str()
znaki = [",", ":", ".", "!"]
while i < 20:
    t = f.readline()
    b += t
    i += 1
j = 0
for d in range(0, len(b)):
    if b[d] in znaki:
        j += 1
print("Количество знаков препинания: ", j)
f.close()

f1 = open("file18-30-2.txt", "w", encoding="utf-8")
f = open("text18-30.txt", "r", encoding="utf-8")
l = f.readlines()
f1.write(l[0])
st = 1
while st < 7:
    f1.write(l[st])
    st += 1
f1.write("\n")
f1.write("\n")
f1.write("Михаил Лермонтов>>>Бородино")
print()
f1.close()
f.close()
