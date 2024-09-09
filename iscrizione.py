from tkinter import ttk
from customtkinter import *
from datetime import datetime
import tkinter as tk
import connection

set_appearance_mode("light")  
set_default_color_theme("blue")

def on_select(event):
    # Ottiene l'indice dell'elemento selezionato
    selected_index = listbox.curselection()
    if selected_index:
        # Prende il valore dell'elemento selezionato
        selected_item = listbox.get(selected_index)
        count_guide = connection.showGuideMancanti(selected_item.split()[0])
        if count_guide!=None:
            label.configure(text=f"guide mancanti: {count_guide}")
        else:
            label.configure(text=f"Nessuna guida acquistata")


def add_iscrizione():
    CFStudente = studentchoosen.get().split()[2]
    CFTeorico = teoricochoosen.get().split()[2]
    CFPratico = praticochoosen.get().split()[2] 
    tipo = tipochoosen.get()

    try:
        connection.add_iscrizione(CFStudente, CFTeorico, CFPratico, date, tipo)
    except Exception as e:        
        tk.messagebox.showerror("Errore", f"Si è verificato un errore: {str(e)}")
    



window=CTk()
window.title('Menu Principale')
window.geometry('930x478')

window_bg_color = window.cget("fg_color")

    
leftFrame = CTkFrame(window, fg_color=window_bg_color)
leftFrame.grid(row=1, column=0, padx=20, pady=20)

rightFrame = CTkFrame(window, fg_color=window_bg_color)
rightFrame.grid(row=1, column=1, padx=20, pady=20)

topFrame = CTkFrame(window, fg_color=window_bg_color)
topFrame.grid(row=0, column=0, padx=20, pady=20)

CTkButton(topFrame, width=10, text='Back', bg_color='transparent').grid(row=0, column=0, padx=5)  
CTkLabel(rightFrame, text="Elenco iscritti").grid(row=0, column=0,padx=20, pady=20)

CTkLabel(leftFrame, text = "CF Studente :").grid(column = 0, row = 1, padx = 5, pady = 25) 

studentchoosen = ttk.Combobox(leftFrame, width = 20)
studentchoosen.grid(column=1, row=1, padx = 5, pady = 25)
string=[]

for student in connection.showStudent():
    string.append(student[2] + " " + student[1] + " " + student[0])

studentchoosen['values']=(string)


CTkLabel(leftFrame, text = "Tipologia patente :").grid(column = 0, row = 2, padx = 5, pady = 25) 

tipochoosen = ttk.Combobox(leftFrame, width = 20)
tipochoosen.grid(column=1, row=2, padx = 5, pady = 25)

patenti = connection.show_Patenti()
tipo_values = [p[0] for p in patenti]  # Estrai i nomi dalla lista di tuple
tipochoosen['values'] = tipo_values


CTkLabel(leftFrame, text="Data inizio :").grid(column = 0, row = 3, padx = 5, pady = 25)
date = f"{datetime.now().year}-{datetime.now().month:02}-{datetime.now().day:02}"
ttk.Label(leftFrame, text=date, background='white', border=2, relief="sunken", anchor="w", width=23).grid(column=1, row =3 , padx = 5, pady = 25)

CTkLabel(leftFrame, text="Costo :").grid(column = 0, row = 4, padx = 5, pady = 25)
ttk.Label(leftFrame, text="500", background='white', border=2, relief="sunken", anchor="w", width=23).grid(column=1, row =4 , padx = 5, pady = 25)

CTkLabel(leftFrame, text="Istruttore teorico :").grid(column = 0, row = 5, padx = 5, pady = 25)
teoricochoosen = ttk.Combobox(leftFrame, width = 20)
teoricochoosen.grid(column=1, row=5, padx = 5, pady = 25)

teorici = connection.show_Teorici()
teorico_values = [f"{t[2]} {t[1]} {t[0]}" for t in teorici]
teoricochoosen['values'] = teorico_values


CTkLabel(leftFrame, text="Istruttore pratico :").grid(column = 0, row = 6, padx = 5, pady = 25)
praticochoosen = ttk.Combobox(leftFrame, width = 20)
praticochoosen.grid(column=1, row=6, padx = 5, pady = 25)

pratici = connection.show_Pratici()
pratico_values = [f"{pratici[2]} {pratici[1]} {pratici[0]}"]
praticochoosen['values'] = pratico_values

CTkButton(leftFrame, text='Aggiungi iscrizione', cursor='hand2', command=add_iscrizione).grid(column=0, row=7, padx = 5, pady = 25)



listbox = tk.Listbox(rightFrame, selectmode=tk.SINGLE, width=100, height=20)
listbox.grid(row=1, column=0, padx=10, pady=10)

elements = connection.showIscritti()

for element in elements:
    str = element[0] + " " + element[1] + " " + element[2] +" " +element[3]
    listbox.insert(tk.END, str)

listbox.bind("<<ListboxSelect>>", on_select)

label = CTkLabel(rightFrame, text="Seleziona un elemento dalla lista")
label.grid(row=2, column=0, padx=20, pady=20)

window.mainloop()

