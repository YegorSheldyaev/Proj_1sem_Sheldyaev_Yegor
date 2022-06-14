# Даны целые числа a, b, c, являющиеся сторонами некоторого треугольника.
# Проверьте истинность высказывания:"Треугольник со сторонами a, b, c, является равносторонним".

from tkinter import *

root = Tk()
root.title("PZ_4_2")
root.geometry('360x200')
root["bg"] = "gray40"

label1 = Label(text='Введите число A:', bg='gray40', fg='gray85', font=('arial black', 14), justify=LEFT)
label1.place(x=10, y=5)
label2 = Label(text='Введите число B:', bg='gray40', fg='gray85', font=('arial black', 14), justify=LEFT)
label2.place(x=10, y=40)
label3 = Label(text='Введите число C:', bg='gray40', fg='gray85', font=('arial black', 14), justify=LEFT)
label3.place(x=10, y=75)
label4 = Label(text='', bg='gray40', fg='white', font=('arial black', 13), justify=LEFT)
label4.place(x=10, y=140)

entry1 = Entry(width=13, font=('arial black', 10))
entry1.place(x=220, y=12)
entry2 = Entry(width=13, font=('arial black', 10))
entry2.place(x=220, y=47)
entry3 = Entry(width=13, font=('arial black', 10))
entry3.place(x=220, y=82)


def b1_clicked():
    try:
        a = int(entry1.get())
        b = int(entry2.get())
        c = int(entry3.get())

        if a == b == c:
            res = "Треугольник равносторонний"
            label4.config(fg='white', text=f'Результат:\n{res}')
        else:
            res = "Треугольник не равносторонний"
            label4.config(fg='white', text=f'Результат:\n{res}')
    except:
        res = "ОШИБКА!"
        label4.config(fg='black', text=res)


b1 = Button(root, text='Вычислить', width=10, bg='gray60', fg='white', font=('arial', 14), command=b1_clicked)
b1.place(x=222, y=120)
root.mainloop()