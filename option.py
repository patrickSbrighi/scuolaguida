from tkinter import *
import admin
import tipologia
import veicoli
from customtkinter import *

def create_impostazioni_frame(parent_frame):    

    window_bg_color = parent_frame.cget("fg_color")

    window = CTkFrame(parent_frame, fg_color=window_bg_color)
    window.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
    window.grid_columnconfigure((0, 1, 2), weight=1)
    window.grid_rowconfigure(0, weight=1)

    
    btnVeicoli = CTkButton(window, text='Aggiungi \nveicolo', font=('Arial', 15), command=lambda: veicoli.create_veicoli_frame(parent_frame))
    btnVeicoli.grid(row=0, column=0, padx=5, pady=5)

    btnTipologia = CTkButton(window, text='Aggiungi \ntipologia', font=('Arial', 15), command=lambda: tipologia.create_tipologia_frame(parent_frame))
    btnTipologia.grid(row=0, column=1, padx=5, pady=5)

    btnAdmin = CTkButton(window, text='Aggiungi \nadmin', font=('Arial', 15), command= lambda: admin.create_admin_frame(parent_frame))
    btnAdmin.grid(row=0, column=2, padx=5, pady=5)
    

    return window
