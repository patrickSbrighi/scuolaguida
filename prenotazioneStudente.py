import datetime
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from connetion2 import *
import esamiPratici
import esamiTeorici
import option
import selezionaPrenotazione
import statistiche

def create(idStud):
    idStudente = idStud
    CFistruttore = get_istruttore_pratico_studente(idStudente)[0][0]

    def openPrenotazione():
        window.destroy()
        selezionaPrenotazione.create()

    def openEsamiTeorici():
        window.destroy()
        esamiTeorici.create()

    def openEsamiPratici():
        window.destroy()
        esamiPratici.create()

    def openStatistiche():
        window.destroy()
        statistiche.create()

    def openOption():
        window.destroy()
        option.create()

    def clearTreeview():
        list.selection_remove(list.selection())
        for item in list.get_children():
            list.delete(item)

    def updateView():
        clearTreeview()
        for gu in get_guide_future():
            list.insert('',END,values=gu)

    def center_window(win, width=930, height=478):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        win.geometry(f'{width}x{height}+{x}+{y}')

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

        conferma_button = Button(cal_finestra, text="Conferma", command=conferma_data)
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

        conferma_button = Button(cal_finestra, text="Conferma", command=conferma_data)
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
        selected_items = list.selection()
        if not selected_items:
            return
        selected_item = selected_items[0]
        item_values = list.item(selected_item, 'values')
        boxIDRip.delete(0, 'end')
        boxIDRip.insert(0, item_values[0])


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
        lblRimanenti.config(text=rimanenti)
        if num == 0:
            btnConferma.config(state=DISABLED)
        else:
            btnConferma.config(state=NORMAL)

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

    window=Tk()
    window.title('Prenotazione')
    window.geometry('930x478')
    window.resizable(True, True)

    titleLable=Label(window, text='Scuola guida', font=('Arial', 30, 'bold'), bg='black', fg='white')
    titleLable.place(x=0, y=0, relwidth=1)

    logoutButton = Button(window, text='Logout', font=('arial', 10, 'bold'), bg='white')
    logoutButton.place(x=850, y=13)

    leftFrame = Frame(window, bg='lightgray')
    leftFrame.place(x=0, y=52, width=200, relheight=1)

    iscrizioneButton = Button(leftFrame, text='Iscrizioni', font=('Arial', 15))
    iscrizioneButton.pack(fill=X)

    acquistiButton = Button(leftFrame, text='Acquisti', font=('Arial', 15))
    acquistiButton.pack(fill=X)

    prenotazioneButton = Button(leftFrame, text='Prenotazione', font=('Arial', 15), command= lambda:openPrenotazione())
    prenotazioneButton.pack(fill=X)

    teoriaButton = Button(leftFrame, text='Esami teorici', font=('Arial', 15), command=lambda:openEsamiTeorici())
    teoriaButton.pack(fill=X)

    praticaButton = Button(leftFrame, text='Esami pratici', font=('Arial', 15), command=lambda:openEsamiPratici())
    praticaButton.pack(fill=X)

    statisticheButton = Button(leftFrame, text='Statistiche', font=('Arial', 15), command=lambda:openStatistiche())
    statisticheButton.pack(fill=X)

    impostazioniButton = Button(leftFrame, text='Impostazioni', font=('Arial', 15), command=lambda:openOption())
    impostazioniButton.pack(fill=X)

    lblScritta = Label(window, text = "Guide future dello studente", font=('times new roman', 20))
    lblScritta.place(x=215, y=60)

    guideFrame = Frame(window)
    guideFrame.place(x=215, y=90, width=400, height=375)

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
    lblRiprogrammazione.place(x=625, y=80)

    riprogrammaFrame = Frame(window, bg="lightgray")
    riprogrammaFrame.place(x = 625, y = 110, width=295, height=135)

    lblIDRip = Label(riprogrammaFrame, text="Guida da riprogrammare:", font=('times new roman', 13), bg="lightgray")
    lblIDRip.place(x=2, y=2)
    boxIDRip= Entry(riprogrammaFrame, font=('times new roman', 12), width=12)
    boxIDRip.grid(row=0,column=1, pady=2, padx=175)

    lblNewData = Label(riprogrammaFrame, text="Nuova data:", font=('times new roman', 13), bg="lightgray")
    lblNewData.place(x=2, y=30)

    boxNewData = Entry(riprogrammaFrame, font=('times new roman', 12), width=12)
    boxNewData.place(x=90, y=30)

    calButton = Button(riprogrammaFrame, text="Seleziona Data", command=seleziona_data_rip)
    calButton.place(x=200, y=30, height=25)

    lblNewOra = Label(riprogrammaFrame, text="Nuovo orario:", font=('times new roman', 13), bg="lightgray")
    lblNewOra.place(x=2, y=60)

    comboNewOra = ttk.Combobox(riprogrammaFrame, state="readonly", width=10)
    comboNewOra.place(x=115, y=60)

    btnRip = Button(riprogrammaFrame, text="Riprogramma", font=('times new roman', 13), command=lambda: riprogramma())
    btnRip.place(x=100, y=90)

    lblAggiungi = Label(window, text="Nuova guida", font=('times new roman', 15))
    lblAggiungi.place(x=625, y=255)

    nuovaFrame = Frame(window, bg="lightgray")
    nuovaFrame.place(x = 625, y = 285, width=295, height=180)

    lblRimanenti = Label(nuovaFrame, text="", font=('times new roman', 12), bg="lightgray")
    lblRimanenti.place(x=2, y=2)

    lblDataGuida = Label(nuovaFrame, text="Data:", font=('times new roman', 13), bg="lightgray")
    lblDataGuida.place(x=2, y=30)

    boxDataGuida = Entry(nuovaFrame, font=('times new roman', 12), width=12)
    boxDataGuida.place(x=90, y=30)

    calButtonGuida = Button(nuovaFrame, text="Seleziona Data", command=seleziona_data_add)
    calButtonGuida.place(x=200, y=30, height=25)

    lblOraGuida = Label(nuovaFrame, text="Orario:", font=('times new roman', 13), bg="lightgray")
    lblOraGuida.place(x=2, y=60)

    comboOraGuida = ttk.Combobox(nuovaFrame, state="readonly", width=10)
    comboOraGuida.place(x=115, y=60)

    lblVeicoli = Label(nuovaFrame, text="Seleziona veicolo:", font=('times new roman', 13), bg="lightgray")
    lblVeicoli.place(x=2, y= 90)

    comboVeicolo = ttk.Combobox(nuovaFrame, state="readonly", width=10)
    comboVeicolo.place(x=150, y=90)

    veicoli = [veicolo[0] for veicolo in get_veicoli()]
    comboVeicolo['values'] = veicoli

    btnConferma = Button(nuovaFrame, text="Conferma", font=('times new roman', 15), command=lambda: addGuida())
    btnConferma.place(x=100, y=125)

    updateLabel()

    updateView()
    list.bind('<<TreeviewSelect>>', on_select_list)

    center_window(window)

    window.mainloop()
