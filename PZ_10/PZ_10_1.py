#Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Элементы первого и второго файлов:
#Количество элементов первого и второго файлов:
#Индекс первого минимально элемента первого файла:
#Индекс последнего максимального элемента второго файла:
#Элементы кратные 4 первого и второго файлов:

f = open("text1.txt")
f1= open("text2.txt")
text_output = open("text_output.txt", "w+")
data_1 = [line.rstrip(",") for line in open("text1.txt")]
data_2 = [line.rstrip(",") for line in open("text2.txt")]
data_1 = data_1[0].split(",")
data_2 = data_2[0].split(",")
len_1 = len(data_1)
len_2 = len(data_2)
min_1 = data_1.index(min(data_1, key=lambda i: int(i)))
max_2 = data_2.index(max(data_2, key=lambda i: int(i)))
mult_4 = []
for i in data_1:
    if int(i) % 4 == 0:
        mult_4.append(i)
for j in data_2:
    if int(j) % 4 == 0:
        mult_4.append(j)
for element in data_1:
    text_output.write(element)
    text_output.write(" ")
text_output.write("\n")
for element in data_2:
    text_output.write(element)
    text_output.write(" ")
text_output.write("\n")
text_output.write(str(len_1))
text_output.write("\n")
text_output.write(str(len_2))
text_output.write("\n")
text_output.write(str(min_1))
text_output.write("\n")
text_output.write(str(max_2))
text_output.write("\n")
for element in mult_4:
    text_output.write(element)
    text_output.write(" ")
f.close()
f1.close()
text_output.close()
