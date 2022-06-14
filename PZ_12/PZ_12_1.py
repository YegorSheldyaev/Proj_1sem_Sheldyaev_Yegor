# Вариант 30

import tkinter.scrolledtext
from tkinter import *

root = Tk()
root.title("Library")
root.geometry("625x580")
root["bg"] = "pink"

fr1 = Frame(root, bg="white", bd=100, height='32', width='576', highlightthickness='1', highlightbackground='black')
fr1.place(x=24, y=484)
fr2 = Frame(root, bg="white", bd=100, height='26', width='570', highlightthickness='1', highlightbackground='black')
fr2.place(x=27, y=487)

label1 = Label(text='Регистрационная страница электронной библиотеки', bg='pink', fg='black', font=('arial black', 10),
               justify=LEFT)
label1.place(x=10, y=5)
label2 = Label(text='Заполнив анкету, вы сможете пользоваться нашей электронной библиотекой', bg='pink', fg='black',
               font=('arial', 10), justify=LEFT)
label2.place(x=10, y=40)
label3 = Label(text='Введите регистрационное имя', bg='pink', fg='black', font=('arial', 10), justify=LEFT)
label3.place(x=10, y=75)
label4 = Label(text="Введите пароль", bg='pink', fg='black', font=('arial', 10), justify=LEFT)
label4.place(x=10, y=100)
label5 = Label(text='Подтвердите пароль', bg='pink', fg='black', font=('arial', 10), justify=LEFT)
label5.place(x=10, y=125)
label6 = Label(text='Ваш возраст', bg='pink', fg='black', font=('arial', 10), justify=LEFT)
label6.place(x=10, y=160)
label7 = Label(text='На каких языках читаете:', bg='pink', fg='black', font=('arial', 10), justify=LEFT)
label7.place(x=10, y=195)
label8 = Label(text='Какой формат данных является для вас предпочтительным?', bg='pink', fg='black', font=('arial', 10),
               justify=LEFT)
label8.place(x=10, y=230)
label9 = Label(text="Ваши любимые авторы:", bg='pink', fg='black', font=('arial', 10), justify=LEFT)
label9.place(x=10, y=315)
label10 = Label(text="Проверка PHP Лабораторные по базам данных", bg='pink', fg='black', font=('arial', 10),
                justify=LEFT)
label10.place(x=10, y=450)
label11 = Label(text="Лабораторные по базам данных", height=1, width=70, bg='white', fg='black', font=('arial', 10),
                justify=CENTER)
label11.place(x=30, y=490)
label12 = Label(text="Сегодня замечательный день.", bg='pink', fg='black', font=('arial', 10), justify=CENTER)
label12.place(x=235, y=520)
label13 = Label(text="Я сделал свою первую интернет страничку.", bg='pink', fg='black', font=('arial', 10),
                justify=CENTER)
label13.place(x=200, y=540)
label14 = Label(text="Я буду богатым и свободным человеком!", bg='pink', fg='purple', font=('arial', 10),
                justify=CENTER)
label14.place(x=210, y=560)

entry1 = Entry(width=17, font=('arial', 10))
entry1.place(x=200, y=75)
entry2 = Entry(width=17, font=('arial', 10))
entry2.place(x=200, y=100)
entry3 = Entry(width=17, font=('arial', 10))
entry3.place(x=200, y=125)

var = IntVar()

rbutton1 = Radiobutton(root, text='До 20', variable=var, value=1, bg='pink', fg='black', font=('arial', 10),
                       justify=LEFT)
rbutton1.place(x=100, y=160)
rbutton2 = Radiobutton(root, text='20-30', variable=var, value=2, bg='pink', fg='black', font=('arial', 10),
                       justify=LEFT)
rbutton2.place(x=160, y=160)
rbutton3 = Radiobutton(root, text='30-50', variable=var, value=3, bg='pink', fg='black', font=('arial', 10),
                       justify=LEFT)
rbutton3.place(x=220, y=160)
rbutton4 = Radiobutton(root, text='старше 50', variable=var, value=4, bg='pink', fg='black', font=('arial', 10),
                       justify=LEFT)
rbutton4.place(x=280, y=160)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

check1 = Checkbutton(root, text=u"русский", variable=var1, onvalue=1, offvalue=0, bg='pink', fg='black',
                     font=('arial', 10), justify=LEFT)
check1.place(x=170, y=195)
check2 = Checkbutton(root, text=u"английский", variable=var2, onvalue=1, offvalue=0, bg='pink', fg='black',
                     font=('arial', 10), justify=LEFT)
check2.place(x=250, y=195)
check3 = Checkbutton(root, text=u"французский", variable=var3, onvalue=1, offvalue=0, bg='pink', fg='black',
                     font=('arial', 10), justify=LEFT)
check3.place(x=350, y=195)
check4 = Checkbutton(root, text=u"немецкий", variable=var4, onvalue=1, offvalue=0, bg='pink', fg='black',
                     font=('arial', 10), justify=LEFT)
check4.place(x=460, y=195)

listbox = Listbox(root, height=2, width=10, selectmode=SINGLE, bg='white', fg='black', font=('arial', 10), justify=LEFT)
lst = [u"HTML", u"Plain text"]
for i in lst:
    listbox.insert(END, i)
listbox.place(x=10, y=265)

text = tkinter.scrolledtext.ScrolledText(root, undo=True, height=3, width=35, bg='white', fg='black',
                                         font=('arial', 10))
text.place(x=10, y=350)

button1 = Button(root, text='ОК', height=1, width=5, bg='white', fg='black', font=('arial', 10), justify=CENTER)
button1.place(x=10, y=402)
button1 = Button(root, text='Отменить', height=1, width=8, bg='white', fg='black', font=('arial', 10), justify=CENTER,
                 command=quit)
button1.place(x=70, y=402)

root.mainloop()