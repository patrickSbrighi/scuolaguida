from customtkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
import connection

def new_window():

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
        
        try:
            connection.addStudent(CF, name, surname, address, phone, date)
        except Exception as e:
            msg.showerror("Errore", f"Si è verificato un errore: {str(e)}")

        data=connection.showStudent()
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

    nameLable = CTkLabel(leftFrame, text="Name", font=('arial', 15, 'bold'))
    nameLable.grid(row=1, column=0, padx=20, pady=10)
    nameEntry = CTkEntry(leftFrame)
    nameEntry.grid(row=1, column=1, pady=10)

    surnameLable = CTkLabel(leftFrame, text="Cognome", font=('arial', 15, 'bold'))
    surnameLable.grid(row=2, column=0, padx=20, pady=10)
    surnameEntry = CTkEntry(leftFrame)
    surnameEntry.grid(row=2, column=1, pady=10)

    addressLable = CTkLabel(leftFrame, text="Indirizzo", font=('arial', 15, 'bold'))
    addressLable.grid(row=3, column=0, padx=20, pady=10)
    addressEntry = CTkEntry(leftFrame)
    addressEntry.grid(row=3, column=1, pady=10)

    phoneLable = CTkLabel(leftFrame, text="Recapito Telefonico", font=('arial', 15, 'bold'))
    phoneLable.grid(row=4, column=0, padx=20, pady=10)
    phoneEntry = CTkEntry(leftFrame)
    phoneEntry.grid(row=4, column=1, pady=10)

    dateLable = CTkLabel(leftFrame, text="Data di Nascita", font=('arial', 15, 'bold'))
    dateLable.grid(row=5, column=0, padx=20, pady=10)
    dateEntry = CTkEntry(leftFrame)
    dateEntry.grid(row=5, column=1, pady=10)


    addbtn = CTkButton(leftFrame, text='Aggiungi', cursor='hand2', command=add)
    addbtn.grid(row=6, column=0, padx=10, pady=10)


    tree = ttk.Treeview(rightData, columns=('CF', 'Nome', 'Cognome', 'Indirizzo', 'Recapito Telefonico', 'Data di Nascita'), show='headings')

    tree.heading('CF', text='CF', anchor='center')
    tree.heading('Nome', text='None', anchor='center')
    tree.heading('Cognome', text='Cognome', anchor='center')
    tree.heading('Indirizzo', text='Indirizzo', anchor='center')
    tree.heading('Recapito Telefonico', text='Recapito Telefonico', anchor='center')
    tree.heading('Data di Nascita', text='Data di Nascita', anchor='center')


    tree.column('CF', stretch=True, width=100,anchor="w")
    tree.column('Nome', stretch=True, width=100, anchor="w")
    tree.column('Cognome', stretch=True, width=100, anchor="w")
    tree.column('Indirizzo', stretch=True, width=100, anchor="w")
    tree.column('Recapito Telefonico', stretch=True, width=100, anchor="w")
    tree.column('Data di Nascita', stretch=True, width=100, anchor="w")

    tree.pack(fill="both", expand=True)

    style=ttk.Style()
    style.configure("Treeview.Heading", font=('Arial', 10, 'bold'))

    data=connection.showStudent()
    populate_treeview(tree, data)

    #ridimensiona oggetti 
    win.grid_columnconfigure(1,weight=1)
    win.grid_rowconfigure(0,weight=1)
    rightData.grid_rowconfigure(0, weight=1)

    win.mainloop()