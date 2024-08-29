from customtkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
import connection

def populate_treeview(tree, data):
    for student in tree.get_children():
        tree.delete(student)

    for row in data:
        tree.insert("", "end", values=row)


def add():
    CF = CFEntry.get()
    name = nameEntry.get()
    surname = surnameEntry.get()
    address = addressEntry.get()
    phone = phoneEntry.get()
    date = dateEntry.get()
    
    connection.addPerson(CF, name, surname, address, phone, date)
    data=connection.show_Person()
    populate_treeview(tree, data)




win = CTk()
win.geometry('930x478')
win.resizable(True,True)
win.title('Manage Students')

leftFrame = CTkFrame(win)
leftFrame.grid(row = 0, column = 0, sticky="ns")

rightData = CTkFrame(win)
rightData.grid(row=0, column=1, sticky="nsew")


CFLable = CTkLabel(leftFrame, text="CF", font=('arial', 15, 'bold'))
CFLable.grid(row=0, column=0, padx=20, pady=10)
CFEntry = CTkEntry(leftFrame)
CFEntry.grid(row=0, column=1, pady=10)

nameLable = CTkLabel(leftFrame, text="name", font=('arial', 15, 'bold'))
nameLable.grid(row=1, column=0, padx=20, pady=10)
nameEntry = CTkEntry(leftFrame)
nameEntry.grid(row=1, column=1, pady=10)

surnameLable = CTkLabel(leftFrame, text="surname", font=('arial', 15, 'bold'))
surnameLable.grid(row=2, column=0, padx=20, pady=10)
surnameEntry = CTkEntry(leftFrame)
surnameEntry.grid(row=2, column=1, pady=10)

addressLable = CTkLabel(leftFrame, text="address", font=('arial', 15, 'bold'))
addressLable.grid(row=3, column=0, padx=20, pady=10)
addressEntry = CTkEntry(leftFrame)
addressEntry.grid(row=3, column=1, pady=10)

phoneLable = CTkLabel(leftFrame, text="telephone number", font=('arial', 15, 'bold'))
phoneLable.grid(row=4, column=0, padx=20, pady=10)
phoneEntry = CTkEntry(leftFrame)
phoneEntry.grid(row=4, column=1, pady=10)

dateLable = CTkLabel(leftFrame, text="date of born", font=('arial', 15, 'bold'))
dateLable.grid(row=5, column=0, padx=20, pady=10)
dateEntry = CTkEntry(leftFrame)
dateEntry.grid(row=5, column=1, pady=10)


addbtn = CTkButton(leftFrame, text='Add Student', cursor='hand2', command=add)
addbtn.grid(row=6, column=0, padx=10, pady=10)


tree = ttk.Treeview(rightData, columns=('CF', 'name', 'surname', 'address', 'telephone number', 'date of born'), show='headings')

tree.heading('CF', text='CF', anchor='center')
tree.heading('name', text='Name', anchor='center')
tree.heading('surname', text='Surname', anchor='center')
tree.heading('address', text='Address', anchor='center')
tree.heading('telephone number', text='Telephone', anchor='center')
tree.heading('date of born', text='Date of Born', anchor='center')


tree.column('CF', stretch=True, width=100,anchor="w")
tree.column('name', stretch=True, width=100, anchor="w")
tree.column('surname', stretch=True, width=100, anchor="w")
tree.column('address', stretch=True, width=100, anchor="w")
tree.column('telephone number', stretch=True, width=100, anchor="w")
tree.column('date of born', stretch=True, width=100, anchor="w")

tree.pack(fill="both", expand=True)

style=ttk.Style()
style.configure("Treeview.Heading", font=('Arial', 10, 'bold'))

data=connection.show_Person()
populate_treeview(tree, data)

#ridimensiona oggetti 
win.grid_columnconfigure(1,weight=1)
win.grid_rowconfigure(0,weight=1)
rightData.grid_rowconfigure(0, weight=1)

win.mainloop()