from tkinter import *
from backend import Database

database = Database("books.db")

class frontend:
    def __init__(self):
        self

    def get_selected_row(self,event):
        try:
            global selected_tuple
            index=list1.curselection()[0]
            selected_tuple=list1.get(index)
            e1.delete(0,END)
            e1.insert(END,selected_tuple[1])
            e2.delete(0,END)
            e2.insert(END,selected_tuple[2])
            e3.delete(0,END)
            e3.insert(END,selected_tuple[3])
            e4.delete(0,END)
            e4.insert(END,selected_tuple[4])
        except IndexError:
            pass


    def view_command(self):
        list1.delete(0,END)
        for row in database.view():
            list1.insert(END, row)        #END enter the element at the end of the list

    def search_command(self):
        list1.delete(0,END)
        for row in database.search(title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get()):
            list1.insert(END, row)

    def add_command(self):
        database.insert(title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get())
        list1.delete(0,END)
        list1.insert(END,(title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get()))

    def update_command(self):
        database.update(selected_tuple[0],title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get())
        # print(selected_tuple[0],title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get()

    def delete_command(self):
        database.delete(selected_tuple[0])

ft = frontend()

window = Tk()
window.wm_title("Book Store")

l1 = Label(window, text = "Title")
l1.grid(row=0, column=0)

l2= Label(window, text = "Author")
l2.grid(row=0, column=2)

l3 = Label(window, text = "Year")
l3.grid(row=1, column=0)

l4 = Label(window, text = "ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable= title_text)
e1.grid(row=0, column=1)

Author_text = StringVar()
e2 = Entry(window, textvariable= Author_text)
e2.grid(row=0, column=3)

Year_text = StringVar()
e3 = Entry(window, textvariable= Year_text)
e3.grid(row=1, column=1)

ISBN_text = StringVar()
e4 = Entry(window, textvariable= ISBN_text)
e4.grid(row=1, column=3)

list1 =Listbox(window, height = 6, width = 35)
list1.grid(row=2,column=0, rowspan =6, columnspan=2)

sb1= Scrollbar(window)
sb1.grid(row=2,column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',ft.get_selected_row)

b1 = Button(window, text = "View all", width=12,command=ft.view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text = "Seach Entry", width=12, command=ft.search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text = "Add entry", width=12, command= ft.add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text = "Update Selected", width=12, command=ft.update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text = "Delete Selected", width=12, command=ft.delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text = "Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
