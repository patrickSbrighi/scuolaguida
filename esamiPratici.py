from tkinter import *
from tkinter import ttk
from connetion2 import *

def clearTreeview():
    for item in list.get_children():
        list.delete(item)

def updateView():
    clearTreeview()
    for stud in get_studenti_pratici():
        list.insert('',END,values=stud)

def addEsito():
    id = boxID.get()
    esito = boxEsito.get()
    data = boxData.get()
    esaminatore = boxEsaminatore.get()
    if not id or not esito or not data or not esaminatore:
        msg.showerror("Error", "Fill all attribute")
    else:
        add_esame_pratico(id,esito,data)

def on_select_list(event):
    selected_item = list.selection()[0]
    item_values = list.item(selected_item, 'values')
    boxID.delete(0, 'end')
    boxID.insert(0, item_values[0])

def on_select_esmainatori(event):
    selected_item = esamintoriTree.selection()[0]
    item_values = esamintoriTree.item(selected_item, 'values')
    boxEsaminatore.delete(0, 'end')
    boxEsaminatore.insert(0, item_values[0])

def viewEsaminatori():
    for esam in get_esaminatori():
        esamintoriTree.insert('',END,values=esam)

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
addFrame.place(x=250, y=75, width=200, height=300)

lblID = Label(addFrame, text="Seleziona uno studente", font=('times new roman', 15), bg='lightgray')
lblID.place(x=8,y=2)
boxID = Entry(addFrame, font=('times new roman', 12), bg="lightyellow")
boxID.grid(row=0,column=1, padx=8, pady=25)

lblEsito = Label(addFrame, text="Esito:", font=('times new roman', 15), bg='lightgray')
lblEsito.place(x=8,y=50)
lblInserti = Label(addFrame, text="(1 = promosso, 0 = bocciato)", font=('times new roman', 10), bg='lightgray')
lblInserti.place(x=8,y=70)
boxEsito = Entry(addFrame, font=('times new roman', 12), bg="lightyellow")
boxEsito.grid(row=1,column=1, padx=8, pady=20)

lblEsaminatore = Label(addFrame, text="Seleziona esaminatore", font=('times new roman', 15), bg='lightgray')
lblEsaminatore.place(x=8,y=120)
boxEsaminatore = Entry(addFrame, font=('times new roman', 12), bg="lightyellow")
boxEsaminatore.grid(row=2,column=1, padx=8, pady=10)

lblData = Label(addFrame, text="Data (aaaa/mm/dd):", font=('times new roman', 15), bg='lightgray')
lblData.place(x=8,y=170)
boxData = Entry(addFrame, font=('times new roman', 12), bg="lightyellow")
boxData.grid(row=3,column=1, padx=8, pady=15)

btnInvia = Button(addFrame, text="Invio", font=('Arial', 15), command=lambda:addEsito())
btnInvia.place(x=50, y=235, width=100)

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


window.mainloop()