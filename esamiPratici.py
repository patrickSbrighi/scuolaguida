from tkinter import *
from tkinter import ttk
from connetion2 import *

def clearTreeview():
    for item in list.get_children():
        list.delete(item)

def updateView():
    clearTreeview()
    for stud in get_studenti_teorici():
        list.insert('',END,values=stud)

def addEsito():
    print("implementami")

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

prenotazioneButton = Button(leftFrame, text='Prenotazione', font=('Arial', 15))
prenotazioneButton.pack(fill=X)

teoriaButton = Button(leftFrame, text='Esami teorici', font=('Arial', 15))
teoriaButton.pack(fill=X)

praticaButton = Button(leftFrame, text='Esami pratici', font=('Arial', 15))
praticaButton.pack(fill=X)

statisticheButton = Button(leftFrame, text='Statistiche', font=('Arial', 15))
statisticheButton.pack(fill=X)

impostazioniButton = Button(leftFrame, text='Impostazioni', font=('Arial', 15))
impostazioniButton.pack(fill=X)

studentiFrame = Frame(window)
studentiFrame.place(x=500, y=75, width=400, height=375)

list = ttk.Treeview(studentiFrame, columns=('ID', 'Nome', 'Cognome'), show="headings")
list.pack(expand=True, fill='both')
list.column('ID', width=100, anchor='center')
list.column('Nome', width=100, anchor='center')
list.column('Cognome', width=100, anchor='center')
list.heading('ID', text='ID')
list.heading('Nome', text='Nome')
list.heading('Cognome', text='Cognome')

addFrame = Frame(window, bg="lightgray")
addFrame.place(x=250, y=75, width=200, height=250)

lblID = Label(addFrame, text="Seleziona uno studente", font=('times new roman', 15), bg='lightgray')
lblID.place(x=8,y=2)
boxID = Entry(addFrame, font=('times new roman', 12), bg="lightyellow")
boxID.grid(row=0,column=1, padx=8, pady=25)

lblNumErrori = Label(addFrame, text="Numero errori:", font=('times new roman', 15), bg='lightgray')
lblNumErrori.place(x=8,y=50)
boxErrori = Entry(addFrame, font=('times new roman', 12), bg="lightyellow")
boxErrori.grid(row=1,column=1, padx=8)

lblData = Label(addFrame, text="Data (aaaa/mm/dd):", font=('times new roman', 15), bg='lightgray')
lblData.place(x=8,y=100)
boxData = Entry(addFrame, font=('times new roman', 12), bg="lightyellow")
boxData.grid(row=2,column=1, padx=8, pady=30)

btnInvia = Button(addFrame, text="Invio", font=('Arial', 15), command=lambda:addEsito())
btnInvia.place(x=50, y=175, width=100)

updateView()

window.mainloop()