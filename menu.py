from tkinter import *
import iscrizione
import studenti

def show_iscrizione():
    iscrizione.new_window(window)

window=Tk()
window.title('Menu Principale')
window.geometry('930x478')
window.resizable(True, True)

titleLable=Label(window, text='Scuola guida', font=('Arial', 30, 'bold'), bg='black', fg='white')
titleLable.place(x=0, y=0, relwidth=1)

logoutButton = Button(window, text='Logout', font=('arial', 10, 'bold'), bg='white')
logoutButton.place(x=850, y=13)


leftFrame = Frame(window, bg='lightblue')
leftFrame.place(x=0, y=52, width=200, height=426)

menuLable=Label(leftFrame, text='Menu', font=('Arial', 15))
menuLable.pack(fill=X)

studentsButton = Button(leftFrame, text='Studenti', font=('Arial', 15), command=studenti.new_window)
studentsButton.pack(fill=X)

iscrizioneButton = Button(leftFrame, text='Iscrizioni', font=('Arial', 15), command=lambda: show_iscrizione())
iscrizioneButton.pack(fill=X)

istruttoreButton = Button(leftFrame, text='Istruttori', font=('Arial', 15))
istruttoreButton.pack(fill=X)

SalesButton = Button(leftFrame, text='Acquisti', font=('Arial', 15))
SalesButton.pack(fill=X)

pacchettiButton = Button(leftFrame, text='Pacchetti', font=('Arial', 15))
pacchettiButton.pack(fill=X)

teoriaButton = Button(leftFrame, text='Esami teorici', font=('Arial', 15))
teoriaButton.pack(fill=X)

praticaButton = Button(leftFrame, text='Esami pratici', font=('Arial', 15))
praticaButton.pack(fill=X)





window.mainloop()