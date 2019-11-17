"""Программа для учета вещей,
хранит данные в словаре(key - название, value - количество)
Содержит 2 поля ввода и 5 кнопок: 1 поле ввода - для ввода названия,
2 поле ввода - для ввода количества.
кнопка add/change -   при нажатии добавляет введенные данные в словарь,
если key  с таким названием уже есть - перезаписывает
кнопка - show - выводит все данные из словаря в виде строки key:value
кнопка delete - удаляет введенное название из словаря
кнопка clear - очищает поля ввода
Перед выходом надо нажать кнопку save - сохранит словарь(перезапишет).
При первом запуске считывается пустой словарь из файла data.json
и сохраняется в переменную dict_.
В него добавляются данные, их сразу же можно просмтреть, отредактировать...
При сохранении словарь перезаписывается.
При следующих вызовах словарь считывается с сохраненными данными"""

import help
from tkinter import Button
from tkinter import END
from tkinter import Entry
from tkinter import Label
from tkinter import Menu
from tkinter import messagebox
from tkinter import Tk


def clear():
    name_entry.delete(0, END)
    quantity_entry.delete(0, END)


def show():
    data = help.show_all(dict_)
    messagebox.showinfo('Things', data)


def add():
    dict_[name_entry.get()] = quantity_entry.get()


def delete():
    try:
        del dict_[name_entry.get()]
    except KeyError:
        messagebox.showinfo('Error', 'Thing not found')
    else:
        messagebox.showinfo('Done', 'Done')


def save_dict():
    help.save_dict(dict_)
    messagebox.showinfo('Done', 'Saved')


root = Tk()
root.title('Accounting')
root.geometry('300x300+500+100')

name_label = Label(text='Thing:')
quantity_label = Label(text='Quantity:')

name_label.grid(row=0, column=0, sticky='w')
quantity_label.grid(row=1, column=0, sticky='w')

name_entry = Entry()
quantity_entry = Entry()

name_entry.grid(row=0, column=1)
quantity_entry.grid(row=1, column=1)

name_entry.insert(1, 'Bolt')
quantity_entry.insert(1, '1')

clear_button = Button(text='Clear', command=clear)
add_button = Button(text='Add/Change', command=add)
show_button = Button(text='Show', command=show)
del_button = Button(text='Delete', command=delete)

clear_button.grid(row=2, column=1, sticky='e')
del_button.grid(row=2, column=2, sticky='w')
add_button.grid(row=2, column=0, sticky='e')
show_button.grid(row=2, column=1, sticky='w')

main_menu = Menu()
main_menu.add_cascade(label='Save', command=save_dict)

if __name__ == '__main__':
    help.create_outfile()
    dict_ = help.rd_dict()
    root.config(menu=main_menu)
    root.mainloop()
