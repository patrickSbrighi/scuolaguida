from tkinter import ttk
from customtkinter import *
from datetime import datetime
import tkinter as tk
import connection

def create_iscrizioni_frame(parent_frame):
    # Funzione per gestire la selezione della listbox
    def on_select(event):
        selected_index = listbox.curselection()
        if selected_index:
            selected_item = listbox.get(selected_index)
            count_guide = connection.showGuideMancanti(selected_item.split()[0])
            if count_guide is not None:
                label.configure(text=f"Guide mancanti: {count_guide}")
            else:
                label.configure(text="Nessuna guida acquistata")

    def updatedView():
        listbox.delete(0, tk.END)
        elements = connection.showIscritti()
        for element in elements:
            str_element = f"{element[0]} {element[1]} {element[2]} {element[3]}"
            listbox.insert(tk.END, str_element)

    # Funzione per aggiungere l'iscrizione
    def add_iscrizione():
        iva = 22
        try:
            CFStudente = studentchoosen.get().split()[2]
            CFTeorico = teoricochoosen.get().split()[2]
            CFPratico = praticochoosen.get().split()[2]
            costoSel = costiChoosen.get()
            tipo = tipochoosen.get()
        except:
            tk.messagebox.showerror("Errore", "Fill all attributes")

        if not CFStudente or not CFTeorico or not CFPratico or not date or not tipo or not costoSel or not iva:
            tk.messagebox.showerror("Errore", "Fill all attributes")
        else:
            try:
                print(costoSel)
                print(date)
                print(iva)
                connection.addIscrizione(CFStudente, CFTeorico, CFPratico, date, tipo, costoSel, iva)
                updatedView()
            except Exception as e:
                tk.messagebox.showerror("Errore", f"Si è verificato un errore: {str(e)}")

    # Creazione del frame
    iscrizione_frame = CTkFrame(parent_frame)
    iscrizione_frame.grid(row=0, column=0, sticky="nsew")

    # Configura il frame per espandersi con il genitore
    parent_frame.grid_rowconfigure(0, weight=1)
    parent_frame.grid_columnconfigure(0, weight=1)

    # Colore di sfondo
    window_bg_color = iscrizione_frame.cget("fg_color")

    # Frame per la disposizione dei widget
    leftFrame = CTkFrame(iscrizione_frame, fg_color=window_bg_color)
    leftFrame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

    rightFrame = CTkFrame(iscrizione_frame, fg_color=window_bg_color)
    rightFrame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

    # Etichette e combobox nel frame sinistro
    font_style = ("arial", 15, 'bold')

    # Larghezza dei combobox uguale alle etichette
    combobox_width = 15  # Imposta la larghezza per combobox

    CTkLabel(leftFrame, text="CF Studente:", font=font_style).grid(column=0, row=1, padx=5, pady=10, sticky="w")

    studentchoosen = ttk.Combobox(leftFrame, width=combobox_width, font=("arial", 10))
    studentchoosen.grid(column=1, row=1, padx=5, pady=10, sticky='w')

    string = [f"{student[2]} {student[1]} {student[0]}" for student in connection.showStudent()]
    studentchoosen['values'] = string

    CTkLabel(leftFrame, text="Tipologia patente:", font=font_style).grid(column=0, row=2, padx=5, pady=10, sticky="w")

    tipochoosen = ttk.Combobox(leftFrame, width=combobox_width, font=("arial", 10))
    tipochoosen.grid(column=1, row=2, padx=5, pady=10, sticky="w")

    patenti = connection.showPatenti()
    tipo_values = [p[0] for p in patenti]
    tipochoosen['values'] = tipo_values

    CTkLabel(leftFrame, text="Data inizio:", font=font_style).grid(column=0, row=3, padx=5, pady=10, sticky="w")

    date = f"{datetime.now().year}-{datetime.now().month:02}-{datetime.now().day:02}"
    ttk.Label(leftFrame, text=date, background='white', border=2, relief="sunken", anchor="w", width=18, font=("arial", 10)).grid(column=1, row=3, padx=5, pady=10, sticky="w")

    CTkLabel(leftFrame, text="Costo:", font=font_style).grid(column=0, row=4, padx=5, pady=10, sticky="w")

    costiChoosen = ttk.Combobox(leftFrame, width=combobox_width, font=("arial", 10))
    costiChoosen.grid(column=1, row=4, padx=5, pady=10, sticky="w")

    costi_values = ["500", "350", "200"]
    costiChoosen['values'] = costi_values

    CTkLabel(leftFrame, text="Istruttore teorico:", font=font_style).grid(column=0, row=5, padx=5, pady=10, sticky="w")

    teoricochoosen = ttk.Combobox(leftFrame, width=combobox_width, font=("arial", 10))
    teoricochoosen.grid(column=1, row=5, padx=5, pady=10, sticky="w")

    teorici = connection.showTeorici()
    teorico_values = [f"{t[2]} {t[1]} {t[0]}" for t in teorici]
    teoricochoosen['values'] = teorico_values

    CTkLabel(leftFrame, text="Istruttore pratico:", font=font_style).grid(column=0, row=6, padx=5, pady=10, sticky="w")

    praticochoosen = ttk.Combobox(leftFrame, width=combobox_width, font=("arial", 10))
    praticochoosen.grid(column=1, row=6, padx=5, pady=10, sticky="w")

    pratici = connection.showPratici()
    pratico_values = [f"{p[2]} {p[1]} {p[0]}" for p in pratici]
    praticochoosen['values'] = pratico_values

    addbtn = CTkButton(leftFrame, text='Aggiungi', cursor='hand2', command=add_iscrizione)
    addbtn.grid(row=7, column=0, columnspan=2, padx=5, pady=5)


    # Listbox e label nel frame destro
    CTkLabel(rightFrame, text='Seleziona un iscritto', font=('arial', 15)).grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    listbox = tk.Listbox(rightFrame, selectmode=tk.SINGLE, font=("arial", 10))
    listbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    updatedView()

    listbox.bind("<<ListboxSelect>>", on_select)

    label = CTkLabel(rightFrame, text='', font=("arial", 15))
    label.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    # Configurazione del grid layout per i frame
    leftFrame.columnconfigure(0, weight=1)
    leftFrame.columnconfigure(1, weight=2)  # Maggiore peso per la seconda colonna per l'espansione
    leftFrame.rowconfigure(7, weight=1)

    rightFrame.columnconfigure(0, weight=1)
    rightFrame.rowconfigure(0, weight=1)  # Righe e colonne devono essere configurate per l'espansione
    rightFrame.rowconfigure(1, weight=2)
    rightFrame.rowconfigure(2, weight=1)

    # Configurazione per espandere listbox
    rightFrame.columnconfigure(0, weight=1)
    rightFrame.rowconfigure(1, weight=1)  # La Listbox occupa tutto lo spazio rimanente

    # Configura le proporzioni di spazio tra leftFrame e rightFrame
    iscrizione_frame.columnconfigure(0, weight=1)  # Peso più basso per leftFrame
    iscrizione_frame.columnconfigure(1, weight=2)  # Peso maggiore per rightFrame


    return iscrizione_frame
