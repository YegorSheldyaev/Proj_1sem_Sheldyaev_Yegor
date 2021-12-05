#Дана строка, состоящая из русских слов, набранных заглавными буквами и
#разделенных пробелами (одним или несколькими). Найти количество слов, которые
#начинаются и заканчиваются одной и той же буквой.

a = input("введите строку")

list_lines = a.split()
count_word = 0

for count in range(0, len(list_lines)):
    b = list_lines[count]
    if ord(b[0]) == ord(b[len(b) - 1]):
        count_word += 1
print(count_word)
