from tkinter import *
from tkinter import ttk
from connetion2 import *
import esamiPratici
import esamiTeorici
import option
import selezionaPrenotazione

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

    def openOption():
        window.destroy()
        option.create()

    def center_window(win, width=930, height=478):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        win.geometry(f'{width}x{height}+{x}+{y}')

    def clearEsaminatori():
        for item in treeEsamnatori.get_children():
            treeEsamnatori.delete(item)

    def updateEsaminatori():
        clearEsaminatori()
        for ex in get_perc_esaminatori():
            treeEsamnatori.insert('',END,values=ex)

    def clearIstruttoriPratici():
        for item in treeIstruttoriPratici.get_children():
            treeIstruttoriPratici.delete(item)

    def updateIstruttoriPratici():
        clearIstruttoriPratici()
        for ist in get_classifica_istruttori():
            treeIstruttoriPratici.insert('',END,values=ist)

    def clearIstruttoriTeorici():
        for item in treeIstruttoriTeorici.get_children():
            treeIstruttoriTeorici(item)

    def updateIstruttoriTeorici():
        clearIstruttoriTeorici()
        for ist in get_media_errori():
            treeIstruttoriTeorici.insert('',END,values=ist)

    window=Tk()
    window.title('Statistiche')
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

    prenotazioneButton = Button(leftFrame, text='Prenotazione', font=('Arial', 15))
    prenotazioneButton.pack(fill=X)

    teoriaButton = Button(leftFrame, text='Esami teorici', font=('Arial', 15), command=lambda:openEsamiTeorici())
    teoriaButton.pack(fill=X)

    praticaButton = Button(leftFrame, text='Esami pratici', font=('Arial', 15), command=lambda:openEsamiPratici())
    praticaButton.pack(fill=X)

    statisticheButton = Button(leftFrame, text='Statistiche', font=('Arial', 15))
    statisticheButton.pack(fill=X)

    impostazioniButton = Button(leftFrame, text='Impostazioni', font=('Arial', 15), command=lambda:openOption())
    impostazioniButton.pack(fill=X)

    statisticsFrame = Frame(window)
    statisticsFrame.place(x=205, y=57, width=715, height=415)

    lblEsaminatori = Label(statisticsFrame, text='Bocciature per esaminatore:', font=('Arial', 12))
    lblEsaminatori.place(x = 15, y = 10)

    treeEsamnatori = ttk.Treeview(statisticsFrame, columns=('Nome', 'Cognome', '%'), show="headings")
    treeEsamnatori.place(x=15, y=35, height=100)
    treeEsamnatori.column('Nome', width=100, anchor='center')
    treeEsamnatori.column('Cognome', width=100, anchor='center')
    treeEsamnatori.column('%', width=100, anchor='center')
    treeEsamnatori.heading('Nome', text='Nome')
    treeEsamnatori.heading('Cognome', text='Cognome')
    treeEsamnatori.heading('%', text='%')

    scrittaScadenze = 'Percentuale scadenze iscrizioni: ' + str(get_perc_scadenze()[0][0]) + '%'
    lblScadenze = Label(statisticsFrame, text=scrittaScadenze, font=('Arial', 12))
    lblScadenze.place(x = 15, y = 150)

    lblIstruttoriPratici = Label(statisticsFrame, text='Classifica istruttori pratici:', font=('Arial', 12))
    lblIstruttoriPratici.place(x = 400, y = 10)

    treeIstruttoriPratici = ttk.Treeview(statisticsFrame, columns=('Nome', 'Cognome', 'Passati'), show="headings")
    treeIstruttoriPratici.place(x=400, y=35, height=100)
    treeIstruttoriPratici.column('Nome', width=100, anchor='center')
    treeIstruttoriPratici.column('Cognome', width=100, anchor='center')
    treeIstruttoriPratici.column('Passati', width=100, anchor='center')
    treeIstruttoriPratici.heading('Nome', text='Nome')
    treeIstruttoriPratici.heading('Cognome', text='Cognome')
    treeIstruttoriPratici.heading('Passati', text='Promossi')

    scrittaPrimoColpo = 'Percentuale studenti che passano gli esami al primo tentativo: ' + str(get_perc_primo_tentativo()[0][0]) + '%'
    lblPrimoColpo = Label(statisticsFrame, text=scrittaPrimoColpo, font=('Arial', 12))
    lblPrimoColpo.place(x = 15, y = 300)

    lblIstruttoriTeorici = Label(statisticsFrame, text='Media degli errori per ogni istruttore teorico:', font=('Arial', 12))
    lblIstruttoriTeorici.place(x = 400, y = 150)

    treeIstruttoriTeorici = ttk.Treeview(statisticsFrame, columns=('Nome', 'Cognome', 'Errori'), show="headings")
    treeIstruttoriTeorici.place(x=400, y=175, height=100)
    treeIstruttoriTeorici.column('Nome', width=100, anchor='center')
    treeIstruttoriTeorici.column('Cognome', width=100, anchor='center')
    treeIstruttoriTeorici.column('Errori', width=100, anchor='center')
    treeIstruttoriTeorici.heading('Nome', text='Nome')
    treeIstruttoriTeorici.heading('Cognome', text='Cognome')
    treeIstruttoriTeorici.heading('Errori', text='Errori')

    scrittaTempoMedioPatente = 'Tempo medio di presa della patente: ' + str(get_tempo_medio_patente()[0][0]) + ' mesi'
    lblTempoMedioPatente = Label(statisticsFrame, text=scrittaTempoMedioPatente, font=('Arial', 12))
    lblTempoMedioPatente.place(x = 15, y = 200)

    scrittaTempoMedioTeorico = 'Tempo medio promozione esame teorico: ' + str(get_tempo_medio_patente()[0][0]) + ' mesi'
    lblTempoMedioTeorico = Label(statisticsFrame, text=scrittaTempoMedioTeorico, font=('Arial', 12))
    lblTempoMedioTeorico.place(x = 15, y = 250)

    updateEsaminatori()
    updateIstruttoriPratici()
    updateIstruttoriTeorici()

    center_window(window)

    window.mainloop()