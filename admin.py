from tkinter import *
from tkinter import ttk
from connection import *
from customtkinter import *

def create_admin_frame(parent_frame):
    def clearTreeview():
        for item in list.get_children():
            list.delete(item)

    def updateView():
        clearTreeview()
        for admin in get_admins():
            list.insert('',END,values=admin)

    def addAdmin():
        add_admin(boxUsername.get(), boxPassword.get())
        updateView()

    window_bg_color = parent_frame.cget("fg_color")

    window = CTkFrame(parent_frame, fg_color=window_bg_color)
    window.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    addFrame = Frame(window, bg="lightgray")
    addFrame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    lblUsername = Label(addFrame, text="Inserisci l'username", font=('times new roman', 15), bg='lightgray')
    lblUsername.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    boxUsername = Entry(addFrame, font=('times new roman', 12), bg="lightyellow")
    boxUsername.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    lblPassword = Label(addFrame, text="Inserisci password", font=('times new roman', 15), bg='lightgray')
    lblPassword.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    boxPassword = Entry(addFrame, font=('times new roman', 12), bg="lightyellow")
    boxPassword.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

    btnInvia = CTkButton(addFrame, text="Invio", font=('Arial', 15), command=lambda: addAdmin())
    btnInvia.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

    viewFrame = Frame(window)
    viewFrame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

    list = ttk.Treeview(viewFrame, columns=('Admins'), show="headings")
    list.pack(expand=True, fill='both')
    list.column('Admins', width=190, anchor='center')
    list.heading('Admins', text='Admins')
    updateView()

    return window