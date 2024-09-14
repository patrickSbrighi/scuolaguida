from tkcalendar import Calendar
from tkinter import *
from tkinter import ttk
from connection import *
from customtkinter import *

def create_esamiteorici_frame(parent_frame):

    def clearTreeview():
        for item in list.get_children():
            list.delete(item)

    def updateView():
        clearTreeview()
        for stud in get_studenti_teorici():
            list.insert('',END,values=stud)

    def addEsito():
        id = boxID.get()
        errori = boxErrori.get()
        data = boxData.get()
        if not id or not errori or not data:
            msg.showerror("Error", "Fill all attribute")
        else:
            add_esame_teorico(id,errori,data)
            chiudi_iscirzione_teorico()
            updateView()
            boxID.delete(0,END)
            boxData.delete(0,END)
            boxErrori.delete(0,END)

    def on_select(event):
        selected_item = list.selection()
        if selected_item:
            item_values = list.item(selected_item[0], 'values')
            boxID.config(state='normal')
            boxID.delete(0, 'end')
            boxID.insert(0, item_values[0])
            boxID.config(state='readonly')

    def seleziona_data():
        def conferma_data():
            data_selezionata = cal.selection_get()
            giorno_settimana = data_selezionata.weekday()
            if giorno_settimana in (5, 6):
                msg.showerror("Errore", "Non puoi selezionare sabato o domenica!")
                return
            boxData.delete(0, END)
            boxData.insert(0, data_selezionata)
            cal_finestra.destroy()

        cal_finestra = Toplevel(window)
        cal_finestra.grab_set()

        cal = Calendar(cal_finestra, selectmode='day', date_pattern='yyyy-mm-dd')
        cal.pack(pady=20)

        conferma_button = Button(cal_finestra, text="Conferma", command=conferma_data)
        conferma_button.pack(pady=10)

    window_bg_color = parent_frame.cget("fg_color")

    window = CTkFrame(parent_frame, fg_color=window_bg_color)
    window.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    studentiFrame = Frame(window)
    studentiFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    list = ttk.Treeview(studentiFrame, columns=('ID', 'Nome', 'Cognome'), show="headings")
    list.pack(expand=True, fill='both')
    list.column('ID', width=100, anchor='center')
    list.column('Nome', width=100, anchor='center')
    list.column('Cognome', width=100, anchor='center')
    list.heading('ID', text='ID')
    list.heading('Nome', text='Nome')
    list.heading('Cognome', text='Cognome')

    addFrame = Frame(window, bg="lightgray")
    addFrame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    lblID = Label(addFrame, text="Seleziona uno studente", font=('times new roman', 15), bg='lightgray')
    lblID.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    boxID = Entry(addFrame, font=('times new roman', 12), bg="lightyellow", state='readonly')
    boxID.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    lblNumErrori = Label(addFrame, text="Numero errori:", font=('times new roman', 15), bg='lightgray')
    lblNumErrori.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    boxErrori = Entry(addFrame, font=('times new roman', 12), bg="lightyellow")
    boxErrori.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    lblData = Label(addFrame, text="Data:", font=('times new roman', 15), bg='lightgray')
    lblData.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    boxData = Entry(addFrame, font=('times new roman', 12), bg="lightyellow", width=12)
    boxData.grid(row=2, column=1, padx=10, pady=10, sticky='w')
    calButtonGuida = CTkButton(addFrame, text="Seleziona", command=seleziona_data)
    calButtonGuida.grid(row=2, column=2, padx=10, pady=10)

    btnInvia = CTkButton(addFrame, text="Invio", font=('Arial', 15), command=lambda:addEsito())
    btnInvia.grid(row=3, column=0, padx=10, pady=10, columnspan=3)

    updateView()
    list.bind('<<TreeviewSelect>>', on_select)

    return window