from tkinter import *
from tkinter import ttk
from connetion2 import *
from customtkinter import *

def create_veicoli_frame(parent_frame):
    def clearTreeview():
        for item in list.get_children():
            list.delete(item)

    def updateView():
        clearTreeview()
        for vec in get_veicoli():
            list.insert('',END,values=vec)

    def addVeicolo():
        add_veicolo(boxTarga.get(), boxModello.get())
        updateView()

    window_bg_color = parent_frame.cget("fg_color")

    window = CTkFrame(parent_frame, fg_color=window_bg_color)
    window.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    addFrame = Frame(window, bg="lightgray")
    addFrame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    lblTarga = Label(addFrame, text="Inserisci la targa", font=('times new roman', 15), bg='lightgray')
    lblTarga.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    boxTarga = Entry(addFrame, font=('times new roman', 12), bg="lightyellow")
    boxTarga.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    lblModello = Label(addFrame, text="Inserisci il modello", font=('times new roman', 15), bg='lightgray')
    lblModello.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    boxModello = Entry(addFrame, font=('times new roman', 12), bg="lightyellow")
    boxModello.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    btnInvia = CTkButton(addFrame, text="Invio", font=('Arial', 15), command=lambda:addVeicolo())
    btnInvia.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

    viewFrame = Frame(window)
    viewFrame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

    list = ttk.Treeview(viewFrame, columns=('Targa', 'Modello'), show="headings")
    list.pack(expand=True, fill='both')
    list.column('Targa', width=150, anchor='center')
    list.column('Modello', width=150, anchor='center')
    list.heading('Targa', text='Targa')
    list.heading('Modello', text='Modello')

    updateView()

    return window