# Вариант 30
# Приложение СДАЧА В АРЕНДУ ТОРГОВЫХ ПЛОЩАДЕЙ для некоторой организации.
# БД должна содержать таблицу Торговая точка со следующей структурой записи:
# этаж, площадь, наличие кондиционера и стоимость аренды в день.
# БД должна обеспечивать получение информации по стоимости аренды.

from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#a0dea0', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="add.png")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить запись', command=self.open_dialog, bg='#5da130', bd=0,
                                         compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="edit.png")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#5da130',
                                    bd=0, compound=tk.TOP, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="delete.png")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#5da130',
                               bd=0, compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="search.png")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#5da130',
                               bd=0, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="refresh.png")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#5da130',
                                bd=0, compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('user_id', 'floor', 'area', 'conditioner', 'price'), height=17,
                                 show='headings')

        self.tree.column('user_id', width=50, anchor=tk.CENTER)
        self.tree.column('floor', width=150, anchor=tk.CENTER)
        self.tree.column('area', width=150, anchor=tk.CENTER)
        self.tree.column('conditioner', width=150, anchor=tk.CENTER)
        self.tree.column('price', width=150, anchor=tk.CENTER)

        self.tree.heading('user_id', text='ID')
        self.tree.heading('floor', text='Этаж')
        self.tree.heading('area', text='Площадь')
        self.tree.heading('conditioner', text='Наличие кондиционера')
        self.tree.heading('price', text='Стоимость аренды')

        self.tree.pack()

    def records(self, floor, area, conditioner, price):
        self.db.insert_data(floor, area, conditioner, price)
        self.view_records()

    def update_record(self, floor, area, conditioner, price):
        self.db.cur.execute("""UPDATE trade SET floor=?, area=?, conditioner=?, price=? WHERE user_id=?""",
                            (floor, area, conditioner, price, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM trade""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM trade WHERE user_id=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, price):
        price = (price,)
        self.db.cur.execute("""SELECT * FROM trade WHERE price>=?""", price)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить запись')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_floor = tk.Label(self, text='Этаж')
        label_floor.place(x=15, y=25)
        self.entry_floor = ttk.Entry(self)
        self.entry_floor.place(x=130, y=25)

        label_area = tk.Label(self, text='Площадь')
        label_area.place(x=15, y=50)
        self.entry_area = ttk.Entry(self)
        self.entry_area.place(x=130, y=50)

        label_conditioner = tk.Label(self, text='Наличие\nкондиционера', justify=LEFT)
        label_conditioner.place(x=15, y=77)
        self.combobox = ttk.Combobox(self, values=[u'Есть', u'Нет'], state="readonly")
        self.combobox.current(0)
        self.combobox.place(x=130, y=85)

        label_price = tk.Label(self, text='Стоимость\nаренды', justify=LEFT)
        label_price.place(x=15, y=115)
        self.entry_price = ttk.Entry(self)
        self.entry_price.place(x=130, y=125)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_floor.get(),
                                                                       self.entry_area.get(),
                                                                       self.combobox.get(),
                                                                       self.entry_price.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_floor.get(),
                                                                          self.entry_area.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_price.get()))
        self.btn_ok.destroy()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск по стоимости")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        with sq.connect('TradePoint.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS trade (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                floor INTEGER,
                area INTEGER,
                conditioner INTEGER DEFAULT 1,
                price INTEGER
                )""")

    def insert_data(self, floor, area, conditioner, price):
        self.cur.execute("""INSERT INTO trade(floor, area, conditioner, price) VALUES (?, ?, ?, ?)""",
                         (floor, area, conditioner, price))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Сдача в аренду торговых площадей")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
