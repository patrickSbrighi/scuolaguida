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
        for tip in get_tipologie():
            list.insert('',END,values=tip)

    def addTipologia():
        add_tipologia(boxNome.get(), boxEta.get())
        updateView()

    window=Tk()
    window.title('Tipologie')
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
    addFrame.place(x=250, y=75, width=200, height=175)

    lblNome = Label(addFrame, text="Inserisci la tipologia", font=('times new roman', 15), bg='lightgray')
    lblNome.place(x=18,y=2)
    boxNome = Entry(addFrame, font=('times new roman', 12), bg="lightyellow")
    boxNome.grid(row=0,column=1, padx=18, pady=30)

    lblEta = Label(addFrame, text="Inserisci l'età", font=('times new roman', 15), bg='lightgray')
    lblEta.place(x=18,y=55)
    boxEta = Entry(addFrame, font=('times new roman', 12), bg="lightyellow")
    boxEta.grid(row=1,column=1, padx=18)

    btnInvia = Button(addFrame, text="Invio", font=('Arial', 15), command=lambda: addTipologia())
    btnInvia.place(x=50, y=120, width=100)

    viewFrame = Frame(window)
    viewFrame.place(x=500, y=75, width=402, height=300)

    list = ttk.Treeview(viewFrame, columns=('Nome', 'Età'), show="headings")
    list.pack(expand=True, fill='both')
    list.column('Nome', width=130, anchor='center')
    list.column('Età', width=130, anchor='center')
    list.heading('Nome', text='Nome')
    list.heading('Età', text='Età')

    updateView()

    center_window(window)

    window.mainloop()
