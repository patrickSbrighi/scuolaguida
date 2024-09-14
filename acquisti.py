from tkinter import *
from tkinter import ttk
from customtkinter import *
import connection
from tkinter import messagebox

def create_acquisti_frame(parent_frame):
    def addPacchetto(item, pacco):
        connection.addAcquistoPacchetti(item, pacco)
        viewPacchetti()

    def addTeorico(item):
        costo = 100
        connection.addAcquistoTeorico(item, costo)
        viewStudentTeorico()

    def addPratico(item):
        costo = 200
        connection.addAcquistoPratico(item, costo)
        viewStudentPratico()

    def clear_frames():
        # Nasconde tutti i widget quando non necessari
        listbox.grid_forget()
        selected_label.grid_forget()
        pacchetti_label.grid_forget()
        pacchettichoosen.grid_forget()
        btnAcquista.grid_forget()
        for widget in under_frame.winfo_children():
            widget.grid_forget()

    def viewStudentTeorico():
        clear_frames()
        listbox.grid(row=0, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

        def on_select(event):
            selected_index = listbox.curselection()
            if selected_index:
                selected_item = listbox.get(selected_index)
                selected_label.configure(text=f"Desidera acquistare un esame per lo studente: {selected_item.split()[1]} {selected_item.split()[2]}")
                selected_label.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
                btnAcquista.configure(command=lambda: addTeorico(selected_item.split()[0]))
                btnAcquista.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
                pacchetti_label.grid_forget()
                pacchettichoosen.grid_forget()

        elements = connection.showIscrittiTeorico()
        listbox.delete(0, END)
        for element in elements:
            str_elem = f"{element[0]} {element[1]} {element[2]} {element[3]}"
            listbox.insert(END, str_elem)

        listbox.bind("<<ListboxSelect>>", on_select)

    def viewStudentPratico():
        clear_frames()
        listbox.grid(row=0, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

        def on_select(event):
            selected_index = listbox.curselection()
            if selected_index:
                selected_item = listbox.get(selected_index)
                selected_label.configure(text=f"Desidera acquistare un esame per lo studente: {selected_item.split()[1]} {selected_item.split()[2]}")
                selected_label.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
                btnAcquista.configure(command=lambda: addPratico(selected_item.split()[0]))
                btnAcquista.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
                pacchetti_label.grid_forget()
                pacchettichoosen.grid_forget()

        elements = connection.showIscrittiPratico()
        listbox.delete(0, END)
        for element in elements:
            str_elem = f"{element[0]} {element[1]} {element[2]} numero guide {element[3]}"
            listbox.insert(END, str_elem)

        listbox.bind("<<ListboxSelect>>", on_select)

    def viewPacchetti():
        clear_frames()
        listbox.grid(row=0, column=0, columnspan=3, padx=20, pady=10, sticky="ew")
        
        pacchetti = ['Pacchetto 1 guida', 'Pacchetto 5 guide', 'Pacchetto 10 guide', 'Pacchetto 15 guide']
        pacchettichoosen['values'] = pacchetti
        
        # Nascondi gli elementi che non sono immediatamente necessari
        selected_label.grid_forget()
        btnAcquista.grid_forget()
        pacchetti_label.grid_forget()
        pacchettichoosen.grid_forget()

        # Variabile per tenere traccia della selezione dell'elemento
        selected_item = [None]

        def on_listbox_select(event):
            selected_index = listbox.curselection()
            if selected_index:
                selected_item[0] = listbox.get(selected_index)
                selected_label.configure(text=f"Desidera acquistare un pacchetto per lo studente: {selected_item[0].split()[1]} {selected_item[0].split()[2]}")
                selected_label.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
                
                pacchetti_label.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
                pacchettichoosen.grid(row=1, column=1)
                
                # Assicurati che il pulsante Acquista sia nascosto fino a quando non è selezionato un pacchetto
                btnAcquista.grid_forget()

        def on_pacchetto_select(event):
            if selected_item[0]:
                selected_pacchetto = pacchettichoosen.get()
                if not selected_pacchetto:
                    messagebox.showerror("Errore", "Selezionare un pacchetto dalla lista.")
                    return
                
                selected_label.configure(text=f"Desidera acquistare un pacchetto per lo studente: {selected_item[0].split()[1]} {selected_item[0].split()[2]}")
                btnAcquista.configure(command=lambda: addPacchetto(selected_item[0].split()[0], selected_pacchetto.split()[1]))
                btnAcquista.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
            else:
                messagebox.showerror("Errore", "Selezionare prima un elemento dalla listbox.")

        # Configura gli eventi di selezione
        listbox.bind("<<ListboxSelect>>", on_listbox_select)
        pacchettichoosen.bind("<<ComboboxSelected>>", on_pacchetto_select)

        # Carica gli elementi nella Listbox
        elements = connection.showIscrittiPacchetti()
        listbox.delete(0, END)
        for element in elements:
            str_elem = f"{element[0]} {element[1]} {element[2]}"
            listbox.insert(END, str_elem)




    # Crea il frame principale per le acquisizioni
    acquisti_frame = CTkFrame(parent_frame, corner_radius=15, fg_color=parent_frame.cget("fg_color"))
    acquisti_frame.grid(row=0, column=0, sticky="nsew")

    # Configura l'espansione del frame principale
    parent_frame.grid_rowconfigure(0, weight=1)
    parent_frame.grid_columnconfigure(0, weight=1)
    acquisti_frame.grid_rowconfigure(1, weight=1)
    acquisti_frame.grid_columnconfigure(0, weight=1)

    window_bg_color = acquisti_frame.cget("fg_color")

    # Frame per la parte superiore (bottone e label)
    topframe = CTkFrame(acquisti_frame, fg_color=window_bg_color)
    topframe.grid(row=0, column=0, sticky="ew", padx=20, pady=20)
    topframe.grid_columnconfigure(0, weight=1)
    topframe.grid_columnconfigure(1, weight=1)
    topframe.grid_columnconfigure(2, weight=1)
    topframe.grid_columnconfigure(3, weight=1)


    # Frame centrale
    center_frame = CTkFrame(acquisti_frame, fg_color=window_bg_color)
    center_frame.grid(row=1, column=0, sticky="ew")
    center_frame.grid_rowconfigure(0, weight=1)
    center_frame.grid_columnconfigure(0, weight=1)

    under_frame = CTkFrame(acquisti_frame, fg_color=window_bg_color)
    under_frame.grid(row=2, column=0, sticky="ew")

    under_frame.grid_columnconfigure(0, weight=1)
    under_frame.grid_columnconfigure(1, weight=1)

    label = CTkLabel(topframe, text="Seleziona acquisto")
    label.grid(row=0, column=0, padx=10, pady=10)

    btnpratico = CTkButton(topframe, text='Esame Pratico', command=viewStudentPratico)
    btnpratico.grid(row=0, column=1, padx=10, pady=10)
    btnteorico = CTkButton(topframe, text='Esame Teorico', command=viewStudentTeorico)
    btnteorico.grid(row=0, column=2, padx=10, pady=10)
    btnpacchetti = CTkButton(topframe, text='Pacchetto guide', command=viewPacchetti)
    btnpacchetti.grid(row=0, column=3, padx=10, pady=10)

    # Creazione della Listbox e degli altri widget persistenti
    listbox = Listbox(center_frame, selectmode=SINGLE, width=100, height=20)

    selected_label = CTkLabel(center_frame, text="")

    pacchetti_label = CTkLabel(under_frame, text="Seleziona pacchetto:")
    pacchettichoosen = ttk.Combobox(under_frame, width=20)

    btnAcquista = CTkButton(under_frame, text="Acquista")



    return acquisti_frame
