import datetime
from tkcalendar import Calendar
from tkinter import *
from tkinter import ttk
from connetion2 import *
import esamiTeorici
import option
import selezionaPrenotazione
import statistiche

def create():
    def openPrenotazione():
        window.destroy()
        selezionaPrenotazione.create()

    def openEsamiTeorici():
        window.destroy()
        esamiTeorici.create()

    def openStatistiche():
        window.destroy()
        statistiche.create()
    
    def openOption():
        window.destroy()
        option.create()

    def get_esito_value():
        return '1' if boxEsito.get() == "Promosso" else '0'

    def center_window(win, width=930, height=478):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        win.geometry(f'{width}x{height}+{x}+{y}')

    def clearTreeview():
        for item in list.get_children():
            list.delete(item)

    def updateView():
        clearTreeview()
        for stud in get_studenti_pratici():
            list.insert('',END,values=stud)

    def addEsito():
        id = boxID.get()
        esito = get_esito_value()
        data = boxData.get()
        esaminatore = boxEsaminatore.get()
        if not id or not esito or not data or not esaminatore:
            msg.showerror("Error", "Fill all attribute")
        else:
            data_obj = datetime.datetime.strptime(data, "%Y-%m-%d").date()
            if data_obj > datetime.datetime.now().date():
                msg.showerror("Error", "Invalid date")
            else:
                add_esame_pratico(id,esito,data, esaminatore)
                chiudi_iscirzione_pratico()
                updateView()
                boxID.config(state='normal')
                boxID.delete(0,END)
                boxID.config(state='readonly')
                boxEsaminatore.config(state='normal')
                boxEsaminatore.delete(0,END)
                boxEsaminatore.config(state='readonly')
                boxData.delete(0,END)
                boxEsito.set('')

    def on_select_list(event):
        selected_item = list.selection()
        if selected_item:
            item_values = list.item(selected_item[0], 'values')
            boxID.config(state='normal')
            boxID.delete(0, 'end')
            boxID.insert(0, item_values[0])
            boxID.config(state='readonly')

    def on_select_esmainatori(event):
        selected_item = esamintoriTree.selection()
        if selected_item:
            item_values = esamintoriTree.item(selected_item[0], 'values')
            boxEsaminatore.config(state='normal')
            boxEsaminatore.delete(0, 'end')
            boxEsaminatore.insert(0, item_values[0])
            boxEsaminatore.config(state='readonly')

    def viewEsaminatori():
        for esam in get_esaminatori():
            esamintoriTree.insert('',END,values=esam)

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

    window=Tk()
    window.title('Esami Pratici')
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

    prenotazioneButton = Button(leftFrame, text='Prenotazione', font=('Arial', 15), command= lambda: openPrenotazione())
    prenotazioneButton.pack(fill=X)

    teoriaButton = Button(leftFrame, text='Esami teorici', font=('Arial', 15), command= lambda: openEsamiTeorici())
    teoriaButton.pack(fill=X)

    praticaButton = Button(leftFrame, text='Esami pratici', font=('Arial', 15))
    praticaButton.pack(fill=X)

    statisticheButton = Button(leftFrame, text='Statistiche', font=('Arial', 15), command= lambda: openStatistiche())
    statisticheButton.pack(fill=X)

    impostazioniButton = Button(leftFrame, text='Impostazioni', font=('Arial', 15), command=lambda: openOption())
    impostazioniButton.pack(fill=X)

    studentiFrame = Frame(window)
    studentiFrame.place(x=500, y=75, width=400, height=180)

    list = ttk.Treeview(studentiFrame, columns=('ID', 'Nome', 'Cognome'), show="headings")
    list.pack(expand=True, fill='both')
    list.column('ID', width=100, anchor='center')
    list.column('Nome', width=100, anchor='center')
    list.column('Cognome', width=100, anchor='center')
    list.heading('ID', text='ID')
    list.heading('Nome', text='Nome')
    list.heading('Cognome', text='Cognome')

    addFrame = Frame(window, bg="lightgray")
    addFrame.place(x=250, y=75, width=200, height=275)

    lblID = Label(addFrame, text="Seleziona uno studente", font=('times new roman', 15), bg='lightgray')
    lblID.place(x=8, y=2)
    boxID = Entry(addFrame, font=('times new roman', 12), state='readonly')
    boxID.grid(row=0, column=1, pady=25)

    lblEsito = Label(addFrame, text="Esito:", font=('times new roman', 15), bg='lightgray')
    lblEsito.place(x=8, y=50)
    boxEsito = ttk.Combobox(addFrame, font=('times new roman', 12), values=["Promosso", "Bocciato"], state="readonly")
    boxEsito.grid(row=1, column=1, padx=8)

    lblEsaminatore = Label(addFrame, text="Seleziona esaminatore", font=('times new roman', 15), bg='lightgray')
    lblEsaminatore.place(x=8, y=100)
    boxEsaminatore = Entry(addFrame, font=('times new roman', 12), state='readonly')
    boxEsaminatore.grid(row=2, column=1, pady=25)

    lblData = Label(addFrame, text="Data:", font=('times new roman', 15), bg='lightgray')
    lblData.place(x=8, y=150)
    boxData = Entry(addFrame, font=('times new roman', 12), width=12)
    boxData.grid(row=3, column=1, padx=8, pady=2,sticky='w')
    calButtonGuida = Button(addFrame, text="Seleziona", command=seleziona_data)
    calButtonGuida.place(x=120, y=172, height=25)

    btnInvia = Button(addFrame, text="Invio", font=('Arial', 15), command=lambda: addEsito())
    btnInvia.place(x=50, y=215, width=100)

    esaminatoriFrame = Frame(window)
    esaminatoriFrame.place(x=500, y=275, width=400, height=185)

    esamintoriTree = ttk.Treeview(esaminatoriFrame, columns=('CF', 'Nome', 'Cognome'), show="headings")
    esamintoriTree.pack(expand=True, fill='both')
    esamintoriTree.column('CF', width=100, anchor='center')
    esamintoriTree.column('Nome', width=100, anchor='center')
    esamintoriTree.column('Cognome', width=100, anchor='center')
    esamintoriTree.heading('CF', text='CF')
    esamintoriTree.heading('Nome', text='Nome')
    esamintoriTree.heading('Cognome', text='Cognome')

    updateView()
    list.bind('<<TreeviewSelect>>', on_select_list)

    viewEsaminatori()
    esamintoriTree.bind('<<TreeviewSelect>>', on_select_esmainatori)

    center_window(window)
    window.mainloop()