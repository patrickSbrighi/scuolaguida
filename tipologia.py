from tkinter import *
from tkinter import ttk
from connection import *
from customtkinter import * 

def create_tipologia_frame(parent_frame):
    def clearTreeview():
        for item in list.get_children():
            list.delete(item)

    def updateView():
        clearTreeview()
        for tip in get_tipologie():
            list.insert('',END,values=tip)

    def addTipologia():
        add_tipologia(boxNome.get(), boxEta.get())
        updateView()

    window_bg_color = parent_frame.cget("fg_color")

    window = CTkFrame(parent_frame, fg_color=window_bg_color)
    window.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    
    addFrame = Frame(window, bg="lightgray")
    addFrame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    lblNome = Label(addFrame, text="Inserisci la tipologia", font=('times new roman', 15), bg='lightgray')
    lblNome.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    boxNome = Entry(addFrame, font=('times new roman', 12), bg="lightyellow")
    boxNome.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    lblEta = Label(addFrame, text="Inserisci l'età", font=('times new roman', 15), bg='lightgray')
    lblEta.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    boxEta = Entry(addFrame, font=('times new roman', 12), bg="lightyellow")
    boxEta.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    btnInvia = CTkButton(addFrame, text="Invio", font=('Arial', 15), command=lambda: addTipologia())
    btnInvia.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

    viewFrame = Frame(window)
    viewFrame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

    list = ttk.Treeview(viewFrame, columns=('Nome', 'Età'), show="headings")
    list.pack(expand=True, fill='both')
    list.column('Nome', width=130, anchor='center')
    list.column('Età', width=130, anchor='center')
    list.heading('Nome', text='Nome')
    list.heading('Età', text='Età')

    updateView()

    return window
