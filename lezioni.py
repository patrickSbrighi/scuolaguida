from tkcalendar import Calendar
from tkinter import *
from tkinter import ttk
from connetion2 import *
from customtkinter import *

def create_lezioni_frame(parent_Frame):
    def clearTreeview():
        for item in list.get_children():
            list.delete(item)

    def updateView():
        clearTreeview()
        for ist in get_istruttori_teorici():
            list.insert('',END,values=ist)

    def addLezione():
        data = boxData.get()
        ora = comboOra.get()
        cf = boxIstruttore.get()
        if not data or not ora or not cf:
            msg.showerror('Error', 'Fill all attributes')
        else:
            add_lezione(data, ora, cf)
            boxIstruttore.configure(state='normal')
            boxIstruttore.delete(0, END)
            boxIstruttore.configure(state='readonly')
            comboOra.set('')
            boxData.delete(0, END)


    def riempi_combobox():
        valori = [i for i in range(9, 19) if i not in (12, 13)]
        comboOra['values'] = valori


    def on_select_list(event):
        selected_item = list.selection()
        if selected_item:
            item_values = list.item(selected_item[0], 'values')
            boxIstruttore.configure(state='normal')
            boxIstruttore.delete(0, 'end')
            boxIstruttore.insert(0, item_values[0])
            boxIstruttore.configure(state='readonly')
    
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
    
    window_bg_color = parent_Frame.cget("fg_color")

    window = CTkFrame(parent_Frame, bg_color=window_bg_color)
    window.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    addFrame = Frame(window, bg="lightgray")
    addFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    lblData = Label(addFrame, text="Inserisci la data", font=('times new roman', 15), bg='lightgray')
    lblData.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    boxData = Entry(addFrame, font=('times new roman', 12), bg="lightyellow", width=10)
    boxData.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    calButton = CTkButton(addFrame, text="Seleziona Data", command=seleziona_data)
    calButton.grid(row=0, column=2, padx=10, pady=10, sticky="w")


    lblOra = Label(addFrame, text="Orario:", font=('times new roman', 15), bg='lightgray')
    lblOra.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    comboOra = ttk.Combobox(addFrame, state="readonly", width=10)
    comboOra.grid(row=1, column=1, padx=10, pady=10, sticky="w")


    lblEsaminatore = Label(addFrame, text="Seleziona istruttore", font=('times new roman', 15), bg='lightgray')
    lblEsaminatore.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    boxIstruttore = Entry(addFrame, font=('times new roman', 12), state='readonly')
    boxIstruttore.grid(row=2, column=1, padx=10, pady=10, sticky="w")


    btnInvia = CTkButton(addFrame, text="Invio", font=('Arial', 15), command=lambda:addLezione())
    btnInvia.grid(row=3, column=0, padx=10, pady=10, columnspan=3)

    viewFrame = Frame(window)
    viewFrame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    list = ttk.Treeview(viewFrame, columns=('CF', 'Nome', 'Cognome'), show="headings")
    list.pack(expand=True, fill='both')
    list.column('CF', width=100, anchor='center')
    list.column('Nome', width=100, anchor='center')
    list.column('Cognome', width=100, anchor='center')
    list.heading('CF', text='CF')
    list.heading('Nome', text='Nome')
    list.heading('Cognome', text='Cognome')

    updateView()
    riempi_combobox()

    list.bind('<<TreeviewSelect>>', on_select_list)

    return window