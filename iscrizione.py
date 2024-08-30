from tkinter import ttk
from customtkinter import *
from datetime import datetime
import tkinter.messagebox as msg
import connection

def add_iscrizione():
    if studentchoosen.get() == "" or teoricochoosen.get() == "" or praticochoosen.get() == "":
        return msg.showerror("Errore", "Inserire tutti i campi")

    CFStudente = studentchoosen.get().split()[2]
    CFTeorico = teoricochoosen.get().split()[2]
    CFPratico = praticochoosen.get().split()[2]
    tipo = tipochoosen.get()
    connection.add_iscrizione(CFStudente, CFTeorico, CFPratico, date, tipo)
    

window = CTk()
window.geometry('930x478')
window.resizable(True,True)
window.title('Iscrizioni')

  
ttk.Label(window, text = "CF Studente :", font=('arial', 10, 'bold')).grid(column = 0, row = 1, padx = 10, pady = 25) 
  
studentchoosen = ttk.Combobox(window, width = 20)
studentchoosen.grid(column=1, row=1, padx = 10, pady = 25)
str=[]

for student in connection.show_Student():
    str.append(student[2] + " " + student[1] + " " + student[0])

studentchoosen['values']=(str)


ttk.Label(window, text = "Tipologia patente :", font=('arial', 10, 'bold')).grid(column = 0, row = 2, padx = 10, pady = 25) 

tipochoosen = ttk.Combobox(window, width = 20)
tipochoosen.grid(column=1, row=2, padx = 10, pady = 25)

patenti = connection.show_Patenti()
tipo_values = [p[0] for p in patenti]  # Estrai i nomi dalla lista di tuple
tipochoosen['values'] = tipo_values


ttk.Label(window, text="Data inizio :", font=('arial', 10, 'bold')).grid(column = 0, row = 3, padx = 10, pady = 25)
date = f"{datetime.now().year}-{datetime.now().month:02}-{datetime.now().day:02}"
ttk.Label(window, text=date, background='white', border=2, relief="sunken", anchor="w", width=23).grid(column=1, row =3 , padx = 10, pady = 25)

ttk.Label(window, text="Costo :", font=('arial', 10, 'bold')).grid(column = 0, row = 4, padx = 10, pady = 25)
ttk.Label(window, text="500", background='white', border=2, relief="sunken", anchor="w", width=23).grid(column=1, row =4 , padx = 10, pady = 25)

ttk.Label(window, text="Istruttore teorico :", font=('arial', 10, 'bold')).grid(column = 0, row = 5, padx = 10, pady = 25)
teoricochoosen = ttk.Combobox(window, width = 20)
teoricochoosen.grid(column=1, row=5, padx = 10, pady = 25)

teorici = connection.show_Teorici()
teorico_values = [f"{t[2]} {t[1]} {t[0]}" for t in teorici]
teoricochoosen['values'] = teorico_values


ttk.Label(window, text="Istruttore pratico :", font=('arial', 10, 'bold')).grid(column = 0, row = 6, padx = 10, pady = 25)
praticochoosen = ttk.Combobox(window, width = 20)
praticochoosen.grid(column=1, row=6, padx = 10, pady = 25)

pratici = connection.show_Pratici()
pratico_values = [f"{p[2]} {p[1]} {p[0]}" for p in pratici]
praticochoosen['values'] = pratico_values

CTkButton(window, text='Aggiungi iscrizione', cursor='hand2', command=add_iscrizione).grid(column=1, row=7, padx = 10, pady = 25)



window.mainloop()