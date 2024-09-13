from tkinter import *
from tkinter import ttk
from connetion2 import *
import prenotazioneStudente
from customtkinter import *

def create_seleziona_studente(parent_frame):

    def openSelected(stud):
        if stud:
            window.destroy()
            prenotazioneStudente.create_prenotazione_frame(parent_frame, stud)
        else:
            msg.showerror('Error', 'Seleziona uno studente')
   

    def updateView():
        for stud in get_studenti_per_guide():
            list.insert('',END,values=stud)

    def on_select(event):
        selected_item = list.selection()
        if selected_item:
            item_values = list.item(selected_item[0], 'values')
            boxID.config(state='normal')
            boxID.delete(0, 'end')
            boxID.insert(0, item_values[0])
            boxID.config(state='readonly')

    window_bg_color = parent_frame.cget("fg_color")

    window = CTkFrame(parent_frame, fg_color=window_bg_color)
    window.grid(row=0, column=0, sticky="nsew")

    studentiFrame = Frame(window)
    studentiFrame.grid(row=0, column=1, sticky="nsew")

    list = ttk.Treeview(studentiFrame, columns=('ID', 'Nome', 'Cognome'), show="headings")
    list.pack(expand=True, fill='both')
    list.column('ID', width=100, anchor='center')
    list.column('Nome', width=100, anchor='center')
    list.column('Cognome', width=100, anchor='center')
    list.heading('ID', text='ID')
    list.heading('Nome', text='Nome')
    list.heading('Cognome', text='Cognome')

    addFrame = Frame(window, bg="lightgray")
    addFrame.grid(row=0, column=0, sticky="nsew")

    lblID = Label(addFrame, text="Seleziona uno studente", font=('times new roman', 15), bg='lightgray')
    lblID.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    boxID = Entry(addFrame, font=('times new roman', 12), bg="lightyellow", state='readonly')
    boxID.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    btnInvia = CTkButton(addFrame, text="Invio", font=('Arial', 15), command=lambda:openSelected(boxID.get()))
    btnInvia.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    list.bind('<<TreeviewSelect>>', on_select)
    updateView()

    return window