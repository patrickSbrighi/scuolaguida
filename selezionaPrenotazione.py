from tkinter import *
from tkinter import ttk
from connetion2 import *

def updateView():
    for stud in get_studenti_per_guide():
        list.insert('',END,values=stud)

def changePage():
    print("implementami")

def on_select(event):
    selected_item = list.selection()[0]
    item_values = list.item(selected_item, 'values')
    boxID.delete(0, 'end')
    boxID.insert(0, item_values[0])

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

lblTitolo = Label(window, text="Seleziona uno studente", font=('times new roman', 15))
lblTitolo.place(x=215, y=65)

studentiFrame = Frame(window)
studentiFrame.place(x=215, y=90, width=400, height=375)

list = ttk.Treeview(studentiFrame, columns=('ID', 'Nome', 'Cognome'), show="headings")
list.pack(expand=True, fill='both')
list.column('ID', width=100, anchor='center')
list.column('Nome', width=100, anchor='center')
list.column('Cognome', width=100, anchor='center')
list.heading('ID', text='ID')
list.heading('Nome', text='Nome')
list.heading('Cognome', text='Cognome')

addFrame = Frame(window, bg="lightgray")
addFrame.place(x=675, y=175, width=200, height=125)

lblID = Label(addFrame, text="Seleziona uno studente", font=('times new roman', 15), bg='lightgray')
lblID.place(x=8,y=5)
boxID = Entry(addFrame, font=('times new roman', 12), bg="lightyellow")
boxID.grid(row=0,column=1, padx=8, pady=30)

btnInvia = Button(addFrame, text="Invio", font=('Arial', 15), command=lambda:changePage())
btnInvia.place(x=50, y=65, width=100)

list.bind('<<TreeviewSelect>>', on_select)
updateView()

window.mainloop()