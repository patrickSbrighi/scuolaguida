from tkinter import *
from tkinter import ttk
from connetion2 import *

def clearTreeview():
    for item in list.get_children():
        list.delete(item)

def updateView():
    clearTreeview()
    for admin in get_admins():
        list.insert('',END,values=admin)

def addAdmin():
    add_admin(boxUsername.get(), boxPassword.get())
    updateView()

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

addFrame = Frame(window, bg="lightgray")
addFrame.place(x=250, y=75, width=200, height=175)

lblUsername = Label(addFrame, text="Inserisci l'username", font=('times new roman', 15), bg='lightgray')
lblUsername.place(x=18,y=2)
boxUsername = Entry(addFrame, font=('times new roman', 12), bg="lightyellow")
boxUsername.grid(row=0,column=1, padx=18, pady=30)

lblPassword = Label(addFrame, text="Inserisci password", font=('times new roman', 15), bg='lightgray')
lblPassword.place(x=18,y=55)
boxPassword = Entry(addFrame, font=('times new roman', 12), bg="lightyellow")
boxPassword.grid(row=1,column=1, padx=18)

btnInvia = Button(addFrame, text="Invio", font=('Arial', 15), command=lambda: addAdmin())
btnInvia.place(x=50, y=120, width=100)

viewFrame = Frame(window)
viewFrame.place(x=600, y=75, width=200, height=300)

list = ttk.Treeview(viewFrame, columns=('Admins'), show="headings")
list.pack(expand=True, fill='both')
list.column('Admins', width=190, anchor='center')
list.heading('Admins', text='Admins')
updateView()

window.mainloop()
