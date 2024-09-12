from tkcalendar import Calendar
from tkinter import *
from tkinter import ttk
from connetion2 import *
import esamiPratici
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
            boxIstruttore.config(state='normal')
            boxIstruttore.delete(0, END)
            boxIstruttore.config(state='readonly')
            comboOra.set('')
            boxData.delete(0, END)


    def riempi_combobox():
        valori = [i for i in range(9, 19) if i not in (12, 13)]
        comboOra['values'] = valori

    def center_window(win, width=930, height=478):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        win.geometry(f'{width}x{height}+{x}+{y}')

    def on_select_list(event):
        selected_item = list.selection()
        if selected_item:
            item_values = list.item(selected_item[0], 'values')
            boxIstruttore.config(state='normal')
            boxIstruttore.delete(0, 'end')
            boxIstruttore.insert(0, item_values[0])
            boxIstruttore.config(state='readonly')
    
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
    window.title('Veicoli')
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

    addFrame = Frame(window, bg="lightgray")
    addFrame.place(x=250, y=75, width=200, height=215)

    lblData = Label(addFrame, text="Inserisci la data", font=('times new roman', 15), bg='lightgray')
    lblData.place(x=18,y=2)
    boxData = Entry(addFrame, font=('times new roman', 12), bg="lightyellow", width=10)
    boxData.place(x=10, y=30)
    calButton = Button(addFrame, text="Seleziona Data", command=seleziona_data)
    calButton.place(x=100, y=30, height=25)

    lblOra = Label(addFrame, text="Orario:", font=('times new roman', 15), bg='lightgray')
    lblOra.place(x=18,y=55)
    comboOra = ttk.Combobox(addFrame, state="readonly", width=10)
    comboOra.place(x=100, y=60)

    lblEsaminatore = Label(addFrame, text="Seleziona istruttore", font=('times new roman', 15), bg='lightgray')
    lblEsaminatore.place(x=18, y=90)
    boxIstruttore = Entry(addFrame, font=('times new roman', 12), state='readonly')
    boxIstruttore.place(x=18,y=115)


    btnInvia = Button(addFrame, text="Invio", font=('Arial', 15), command=lambda:addLezione())
    btnInvia.place(x=50, y=155, width=100)

    viewFrame = Frame(window)
    viewFrame.place(x=500, y=75, width=400, height=300)

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

    center_window(window)
    list.bind('<<TreeviewSelect>>', on_select_list)

    window.mainloop()

create()