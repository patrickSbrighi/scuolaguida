from tkinter import *
from connetion2 import *

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

studentsButton = Button(leftFrame, text='Iscrizioni', font=('Arial', 15))
studentsButton.pack(fill=X)

istruttoreButton = Button(leftFrame, text='Acquisti', font=('Arial', 15))
istruttoreButton.pack(fill=X)

SalesButton = Button(leftFrame, text='Prenotazione', font=('Arial', 15))
SalesButton.pack(fill=X)

pacchettiButton = Button(leftFrame, text='Esami teorici', font=('Arial', 15))
pacchettiButton.pack(fill=X)

teoriaButton = Button(leftFrame, text='Esami pratici', font=('Arial', 15))
teoriaButton.pack(fill=X)

praticaButton = Button(leftFrame, text='Statistiche', font=('Arial', 15))
praticaButton.pack(fill=X)

praticaButton = Button(leftFrame, text='Impostazioni', font=('Arial', 15))
praticaButton.pack(fill=X)

window.mainloop()