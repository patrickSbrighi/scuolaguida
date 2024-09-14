import datetime
from tkcalendar import Calendar
from tkinter import *
from tkinter import ttk
from customtkinter import CTkFrame, CTkButton
from connection import *

def create_esamipratici_frame(parent_frame):

    def get_esito_value():
        return '1' if boxEsito.get() == "Promosso" else '0'

    def clearTreeview():
        for item in list.get_children():
            list.delete(item)

    def updateView():
        clearTreeview()
        for stud in get_studenti_pratici():
            list.insert('', END, values=stud)

    def addEsito():
        id = boxID.get()
        esito = get_esito_value()
        data = boxData.get()
        esaminatore = boxEsaminatore.get()
        if not id or not esito or not data or not esaminatore:
            msg.showerror("Error", "Fill all attributes")
        else:
            data_obj = datetime.datetime.strptime(data, "%Y-%m-%d").date()
            if data_obj > datetime.datetime.now().date():
                msg.showerror("Error", "Invalid date")
            else:
                add_esame_pratico(id, esito, data, esaminatore)
                chiudi_iscirzione_pratico()
                updateView()
                boxID.configure(state='normal')
                boxID.delete(0, END)
                boxID.configure(state='readonly')
                boxEsaminatore.configure(state='normal')
                boxEsaminatore.delete(0, END)
                boxEsaminatore.configure(state='readonly')
                boxData.delete(0, END)
                boxEsito.set('')

    def on_select_list(event):
        selected_item = list.selection()
        if selected_item:
            item_values = list.item(selected_item[0], 'values')
            boxID.configure(state='normal')
            boxID.delete(0, 'end')
            boxID.insert(0, item_values[0])
            boxID.configure(state='readonly')

    def on_select_esaminatori(event):
        selected_item = esamintoriTree.selection()
        if selected_item:
            item_values = esamintoriTree.item(selected_item[0], 'values')
            boxEsaminatore.configure(state='normal')
            boxEsaminatore.delete(0, 'end')
            boxEsaminatore.insert(0, item_values[0])
            boxEsaminatore.configure(state='readonly')

    def viewEsaminatori():
        for esam in get_esaminatori():
            esamintoriTree.insert('', END, values=esam)

    def seleziona_data():
        def conferma_data():
            data_selezionata = cal.selection_get()
            giorno_settimana = data_selezionata.weekday()
            if giorno_settimana in (5, 6):
                msg.showerror("Errore", "Non puoi selezionare sabato o domenica!")
                return
            boxData.delete(0, END)
            boxData.insert(0, data_selezionata.strftime("%Y-%m-%d"))
            cal_finestra.destroy()

        cal_finestra = Toplevel(parent_frame)
        cal_finestra.grab_set()

        cal = Calendar(cal_finestra, selectmode='day', date_pattern='yyyy-mm-dd')
        cal.grid(row=0, column=0, pady=20)

        conferma_button = Button(cal_finestra, text="Conferma", command=conferma_data)
        conferma_button.grid(row=1, column=0, pady=10, sticky="w")

    
    window_bg_color = parent_frame.cget("fg_color")

    esamiPraticiFrame = CTkFrame(parent_frame, fg_color=window_bg_color)
    esamiPraticiFrame.grid(row=0, column=0, sticky="nsew")

    esaminatoriFrame = CTkFrame(esamiPraticiFrame, fg_color=window_bg_color)
    esaminatoriFrame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
    studentiFrame = CTkFrame(esamiPraticiFrame,  fg_color=window_bg_color)
    studentiFrame.grid(row=1, column=2, padx=10, pady=10, sticky="nsew" )
    addFrame = CTkFrame(esamiPraticiFrame, fg_color="lightgray")
    addFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    

    list = ttk.Treeview(studentiFrame, columns=('ID', 'Nome', 'Cognome'), show="headings")
    
    list.column('ID', width=100, anchor='center')
    list.column('Nome', width=100, anchor='center')
    list.column('Cognome', width=100, anchor='center')
    list.heading('ID', text='ID')
    list.heading('Nome', text='Nome')
    list.heading('Cognome', text='Cognome')
    list.pack(fill="both", expand=True)

    updateView()
    list.bind('<<TreeviewSelect>>', on_select_list)

   

    lblID = Label(addFrame, text="Seleziona uno studente", font=('times new roman', 15), bg='lightgray')
    lblID.grid(row=0, column=0, sticky="ew")
    boxID = Entry(addFrame, font=('times new roman', 12), state='readonly')
    boxID.grid(row=0, column=1, pady=25, sticky="ew")

    lblEsito = Label(addFrame, text="Esito:", font=('times new roman', 15), bg='lightgray')
    lblEsito.grid(row=1, column=0, sticky="ew")
    boxEsito = ttk.Combobox(addFrame, font=('times new roman', 12), values=["Promosso", "Bocciato"], state="readonly")
    boxEsito.grid(row=1, column=1, padx=8, sticky="ew")

    lblEsaminatore = Label(addFrame, text="Seleziona esaminatore", font=('times new roman', 15), bg='lightgray')
    lblEsaminatore.grid(row=2, column=0, sticky="ew")
    boxEsaminatore = Entry(addFrame, font=('times new roman', 12), state='readonly')
    boxEsaminatore.grid(row=2, column=1, pady=25, sticky="ew")

    lblData = Label(addFrame, text="Data:", font=('times new roman', 15), bg='lightgray')
    lblData.grid(row=3, column=0, sticky="ew")
    boxData = Entry(addFrame, font=('times new roman', 12), width=12)
    boxData.grid(row=3, column=1, padx=8, pady=2, sticky='ew')
    calButtonGuida = CTkButton(addFrame, text="Seleziona", command=seleziona_data)
    calButtonGuida.grid(row=3, column=2, pady=10, sticky="ew")

    btnInvia = CTkButton(addFrame, text="Invio", font=('Arial', 15), command=lambda: addEsito())
    btnInvia.grid(row=5, column=1, pady=10, columnspan=3)

    esamintoriTree = ttk.Treeview(esaminatoriFrame, columns=('CF', 'Nome', 'Cognome'), show="headings")
    esamintoriTree.column('CF', width=100, anchor='center')
    esamintoriTree.column('Nome', width=100, anchor='center')
    esamintoriTree.column('Cognome', width=100, anchor='center')
    esamintoriTree.heading('CF', text='CF')
    esamintoriTree.heading('Nome', text='Nome')
    esamintoriTree.heading('Cognome', text='Cognome')
    esamintoriTree.pack(fill="both", expand=True)

    viewEsaminatori()
    esamintoriTree.bind('<<TreeviewSelect>>', on_select_esaminatori)

    return esamiPraticiFrame
