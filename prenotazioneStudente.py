import datetime
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from connetion2 import *
from customtkinter import *

def create_prenotazione_frame(parent_frame, idStud):
    idStudente = idStud
    CFistruttore = get_istruttore_pratico_studente(idStudente)[0][0]

    def clearTreeview():
        list.selection_remove(list.selection())
        for item in list.get_children():
            list.delete(item)

    def updateView():
        clearTreeview()
        for gu in get_guide_future(idStudente):
            list.insert('',END,values=gu)

    
    def seleziona_data_rip():
        def conferma_data():
            data_selezionata = cal.selection_get()
            giorno_settimana = data_selezionata.weekday()
            if giorno_settimana in (5, 6):
                msg.showerror("Errore", "Non puoi selezionare sabato o domenica!")
                return
            boxNewData.delete(0, END)
            boxNewData.insert(0, data_selezionata)
            aggiorna_orari_rip(data_selezionata)
            cal_finestra.destroy()

        cal_finestra = Toplevel(window)
        cal_finestra.grab_set()

        cal = Calendar(cal_finestra, selectmode='day', date_pattern='yyyy-mm-dd')
        cal.pack(pady=20)

        conferma_button = CTkButton(cal_finestra, text="Conferma", command=conferma_data)
        conferma_button.pack(pady=10)

    def seleziona_data_add():
        def conferma_data():
            data_selezionata = cal.selection_get()
            giorno_settimana = data_selezionata.weekday()
            if giorno_settimana in (5, 6):
                msg.showerror("Errore", "Non puoi selezionare sabato o domenica!")
                return
            boxDataGuida.delete(0, END)
            boxDataGuida.insert(0, data_selezionata)
            aggiorna_orari_add(data_selezionata)
            cal_finestra.destroy()

        cal_finestra = Toplevel(window)
        cal_finestra.grab_set()

        cal = Calendar(cal_finestra, selectmode='day', date_pattern='yyyy-mm-dd')
        cal.pack(pady=20)

        conferma_button = CTkButton(cal_finestra, text="Conferma", command=conferma_data)
        conferma_button.pack(pady=10)

    def aggiorna_orari_rip(data_selezionata):
        orari_disponibili = [i for i in range(9, 19) if i not in (12, 13)]
        orari_occupati = get_disponibilita_istruttore(data_selezionata, CFistruttore)
        orari_occupati = [ora[0].seconds // 3600 for ora in orari_occupati]
        orari_finali = [ora for ora in orari_disponibili if ora not in orari_occupati]
        comboNewOra['values'] = orari_finali


    def aggiorna_orari_add(data_selezionata):
        orari_disponibili = [i for i in range(9, 19) if i not in (12, 13)]
        orari_occupati = get_disponibilita_istruttore(data_selezionata, CFistruttore)
        orari_occupati = [ora[0].seconds // 3600 for ora in orari_occupati]
        orari_finali = [ora for ora in orari_disponibili if ora not in orari_occupati]
        comboOraGuida['values'] = orari_finali


    def on_select_list(event):
        selected_item = list.selection()
        if selected_item:
            item_values = list.item(selected_item[0], 'values')
            boxIDRip.configure(state='normal')
            boxIDRip.delete(0, 'end')
            boxIDRip.insert(0, item_values[0])
            boxIDRip.configure(state='readonly')


    def riprogramma():
        id = boxIDRip.get()
        data = boxNewData.get()
        ora = comboNewOra.get()
        if not id or not data or not ora:
            msg.showerror("Error", "Fill all attributes")
        else:
            data_obj = datetime.datetime.strptime(data, "%Y-%m-%d").date()
            if data_obj < datetime.datetime.now().date():
                msg.showerror("Error", "Invalid date")
            else:
                riprogramma_guida(id, data, ora)
                updateView()
                boxNewData.delete(0, END)
                comboNewOra.set('')
                boxIDRip.delete(0, END)

    def updateLabel():
        result = get_guide_rimaste(idStudente)
        if result:
            num = result[0][0]
        else:
            num = 0
        rimanenti = "Rimangono " + str(num) + " guide"
        lblRimanenti.configure(text=rimanenti)
        if num == 0:
            btnConferma.configure(state=DISABLED)
        else:
            btnConferma.configure(state=NORMAL)

    def addGuida():
        data = boxDataGuida.get()
        ora = comboOraGuida.get()
        targa = comboVeicolo.get()
        idPacchetto = get_id_pacchetto(idStudente)[0][0]
        if not data or not ora or not targa or not CFistruttore or not idPacchetto:
            msg.showerror("Error", "Fill all attributes")
        else:
            data_obj = datetime.datetime.strptime(data, "%Y-%m-%d").date()
            if data_obj < datetime.datetime.now().date():
                msg.showerror("Error", "Invalid date")
            else:
                if get_guide_rimaste(idStudente)[0][0] == 0:
                    msg.showerror("Error", "Le guide sono finite")
                else:
                    add_guida(data, ora, idPacchetto, targa, CFistruttore)
                    updateView()
                    updateLabel()
                    boxDataGuida.delete(0, END)
                    comboOraGuida.set('')
                    comboVeicolo.set('')

    window_bg_color = parent_frame.cget("fg_color")

    window = CTkFrame(parent_frame, fg_color=window_bg_color)
    window.grid(row=0, column=0, sticky="nsew")

    lblScritta = Label(window, text = "Guide future dello studente", font=('times new roman', 20))
    lblScritta.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
    guideFrame = Frame(window)
    guideFrame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    list = ttk.Treeview(guideFrame, columns=('ID', 'Data', 'Ora', 'Targa', 'Istruttore'), show="headings")
    list.pack(expand=True, fill='both')
    list.column('ID', width=20, anchor='center')
    list.column('Data', width=70, anchor='center')
    list.column('Ora', width=50, anchor='center')
    list.column('Targa', width=100, anchor='center')
    list.column('Istruttore', width=100, anchor='center')
    list.heading('ID', text='ID')
    list.heading('Data', text='Data')
    list.heading('Ora', text='Ora')
    list.heading('Targa', text='Targa')
    list.heading('Istruttore', text='Istruttore')

    lblRiprogrammazione = Label(window, text="Riprogramma", font=('times new roman', 15))
    lblRiprogrammazione.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    riprogrammaFrame = Frame(window, bg="lightgray")
    riprogrammaFrame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    lblIDRip = Label(riprogrammaFrame, text="Guida da riprogrammare:", font=('times new roman', 13), bg="lightgray")
    lblIDRip.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    boxIDRip= Entry(riprogrammaFrame, font=('times new roman', 12), width=12, state='readonly')
    boxIDRip.grid(row=0,column=1, padx=10, pady=10, sticky="w")

    lblNewData = Label(riprogrammaFrame, text="Nuova data:", font=('times new roman', 13), bg="lightgray")
    lblNewData.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    boxNewData = Entry(riprogrammaFrame, font=('times new roman', 12), width=12)
    boxNewData.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    calButton = CTkButton(riprogrammaFrame, text="Seleziona Data", command=seleziona_data_rip)
    calButton.grid(row=1, column=2, padx=10, pady=10, sticky="w")

    lblNewOra = Label(riprogrammaFrame, text="Nuovo orario:", font=('times new roman', 13), bg="lightgray")
    lblNewOra.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    comboNewOra = ttk.Combobox(riprogrammaFrame, state="readonly", width=10)
    comboNewOra.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    btnRip = CTkButton(riprogrammaFrame, text="Riprogramma", font=('times new roman', 13), command=lambda: riprogramma())
    btnRip.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    
    nuovaFrame = Frame(window, bg="lightgray")
    nuovaFrame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

    lblAggiungi = Label(nuovaFrame, text="Nuova guida", font=('times new roman', 15))
    lblAggiungi.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


    lblRimanenti = Label(nuovaFrame, text="", font=('times new roman', 12), bg="lightgray")
    lblRimanenti.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    lblDataGuida = Label(nuovaFrame, text="Data:", font=('times new roman', 13), bg="lightgray")
    lblDataGuida.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    boxDataGuida = Entry(nuovaFrame, font=('times new roman', 12), width=12)
    boxDataGuida.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    calButtonGuida = CTkButton(nuovaFrame, text="Seleziona Data", command=seleziona_data_add)
    calButtonGuida.grid(row=2, column=2, padx=10, pady=10, sticky="w")

    lblOraGuida = Label(nuovaFrame, text="Orario:", font=('times new roman', 13), bg="lightgray")
    lblOraGuida.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    comboOraGuida = ttk.Combobox(nuovaFrame, state="readonly", width=10)
    comboOraGuida.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    lblVeicoli = Label(nuovaFrame, text="Seleziona veicolo:", font=('times new roman', 13), bg="lightgray")
    lblVeicoli.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

    comboVeicolo = ttk.Combobox(nuovaFrame, state="readonly", width=10)
    comboVeicolo.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    veicoli = [veicolo[0] for veicolo in get_veicoli()]
    comboVeicolo['values'] = veicoli

    btnConferma = CTkButton(nuovaFrame, text="Conferma", font=('times new roman', 15), command=lambda: addGuida())
    btnConferma.grid(row=5, column=0,columnspan=3, padx=10, pady=10)

    updateLabel()

    updateView()
    list.bind('<<TreeviewSelect>>', on_select_list)

    return window
