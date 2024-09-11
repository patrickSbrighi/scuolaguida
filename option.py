from tkinter import *
import admin
import esamiPratici
import esamiTeorici
import selezionaPrenotazione
import statistiche
import tipologia
import veicoli

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

    def openTipologia():
        window.destroy()
        tipologia.create()

    def openAdmin():
        window.destroy()
        admin.create()

    def openVeicoli():
        window.destroy()
        veicoli.create()

    def center_window(win, width=930, height=478):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        win.geometry(f'{width}x{height}+{x}+{y}')

    window=Tk()
    window.title('Option')
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

    impostazioniButton = Button(leftFrame, text='Impostazioni', font=('Arial', 15))
    impostazioniButton.pack(fill=X)

    veicoliFrame = Frame(window, bg='lightblue')
    veicoliFrame.place(x=250, y=75, width=150, height=150)
    btnVeicoli = Button(veicoliFrame, text='Aggiungi \nveicolo', font=('Arial', 15), command=lambda: openVeicoli())
    btnVeicoli.pack(fill='both', expand=True)

    tipologiaFrame = Frame(window, bg='lightblue')
    tipologiaFrame.place(x=475, y=75, width=150, height=150)
    btnTipologia = Button(tipologiaFrame, text='Aggiungi \ntipologia', font=('Arial', 15), command=lambda: openTipologia())
    btnTipologia.pack(fill='both', expand=True)

    adminFrame = Frame(window, bg='lightblue')
    adminFrame.place(x=700, y=75, width=150, height=150)
    btnAdmin = Button(adminFrame, text='Aggiungi \nadmin', font=('Arial', 15), command=lambda: openAdmin())
    btnAdmin.pack(fill='both', expand=True)

    istruttoriFrame = Frame(window, bg='lightblue')
    istruttoriFrame.place(x=360, y=275, width=150, height=150)
    btnIstruttori = Button(istruttoriFrame, text='Aggiungi \nistruttori', font=('Arial', 15))
    btnIstruttori.pack(fill='both', expand=True)

    esaminatoriFrame = Frame(window, bg='lightblue')
    esaminatoriFrame.place(x=600, y=275, width=150, height=150)
    btnEsaminatori = Button(esaminatoriFrame, text='Aggiungi \nesaminatori', font=('Arial', 15))
    btnEsaminatori.pack(fill='both', expand=True)

    center_window(window)

    window.mainloop()
