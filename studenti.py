from customtkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
import connection

def create_student_frame(parent_frame):
    # Funzione per popolare il treeview con i dati
    def populate_treeview(tree, data):
        for student in tree.get_children():
            tree.delete(student)

        for row in data:
            tree.insert("", "end", values=row)

    # Funzione per aggiungere uno studente
    def add():
        CF = CFEntry.get()
        name = nameEntry.get()
        surname = surnameEntry.get()
        address = addressEntry.get()
        phone = phoneEntry.get()
        date = dateEntry.get()
        
        try:
            # Prova ad aggiungere lo studente
            connection.addStudent(CF, name, surname, address, phone, date)
            
            # Dopo aver aggiunto, svuota i campi di inserimento
            CFEntry.delete(0, 'end')
            nameEntry.delete(0, 'end')
            surnameEntry.delete(0, 'end')
            addressEntry.delete(0, 'end')
            phoneEntry.delete(0, 'end')
            dateEntry.delete(0, 'end')
        
        except Exception as e:
            msg.showerror("Errore", f"Si è verificato un errore: {str(e)}")

        # Aggiorna i dati nel treeview
        data = connection.showStudent()
        populate_treeview(tree, data)

    # Creazione del frame per la gestione studenti
    student_frame = CTkFrame(parent_frame)
    student_frame.grid(row=0, column=0, sticky="nsew")

    # Configura il frame per espandersi con il genitore
    parent_frame.grid_rowconfigure(0, weight=1)
    parent_frame.grid_columnconfigure(0, weight=1)

    window_bg_color = student_frame.cget("fg_color")


    # Layout del frame studente
    leftFrame = CTkFrame(student_frame, fg_color=window_bg_color)
    leftFrame.grid(row=0, column=0, sticky="ns", padx=5, pady=5)

    rightData = CTkFrame(student_frame, fg_color=window_bg_color)  # Riduzione della larghezza del frame destro
    rightData.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

    # Configura i frame interni per espandersi
    student_frame.grid_rowconfigure(0, weight=1)
    student_frame.grid_columnconfigure(0, weight=0)  # Il frame di sinistra ha una dimensione fissa
    student_frame.grid_columnconfigure(1, weight=1)  # Il frame di destra si espande

    # Etichette e campi di input
    labels_entries = {
        "CF": (0, 0),
        "Name": (1, 0),
        "Cognome": (2, 0),
        "Indirizzo": (3, 0),
        "Recapito Telefonico": (4, 0),
        "Data di Nascita": (5, 0)
    }

    entries = {}
    for label, (row, col) in labels_entries.items():
        lbl = CTkLabel(leftFrame, text=label, font=('Arial', 15, 'bold'))  
        lbl.grid(row=row, column=col, padx=10, pady=5, sticky="w")
        entry = CTkEntry(leftFrame, width=150) 
        entry.grid(row=row, column=col+1, pady=5)
        entries[label] = entry

    CFEntry = entries["CF"]
    nameEntry = entries["Name"]
    surnameEntry = entries["Cognome"]
    addressEntry = entries["Indirizzo"]
    phoneEntry = entries["Recapito Telefonico"]
    dateEntry = entries["Data di Nascita"]

    addbtn = CTkButton(leftFrame, text='Aggiungi', cursor='hand2', command=add)
    addbtn.grid(row=len(labels_entries), column=0, columnspan=2, padx=5, pady=5)

    # Treeview per visualizzare gli studenti
    tree = ttk.Treeview(rightData, columns=('CF', 'Nome', 'Cognome', 'Indirizzo', 'Recapito Telefonico', 'Data di Nascita'), show='headings', height=8)

    # Definizione delle intestazioni delle colonne con larghezza ridotta
    tree.heading('CF', text='CF', anchor='center')
    tree.heading('Nome', text='Nome', anchor='center')
    tree.heading('Cognome', text='Cognome', anchor='center')
    tree.heading('Indirizzo', text='Indirizzo', anchor='center')
    tree.heading('Recapito Telefonico', text='Recapito', anchor='center')
    tree.heading('Data di Nascita', text='Data di Nascita', anchor='center')

    for col in tree["columns"]:
        tree.column(col, width=50, anchor="w") 

    # Configurazione per riempire lo spazio disponibile
    tree.pack(fill="both", expand=True)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Arial', 9, 'bold'))  # Font leggermente aumentato per le intestazioni

    # Popola il treeview con i dati iniziali
    data = connection.showStudent()
    populate_treeview(tree, data)

    # Configurazione per l'espansione automatica
    rightData.grid_rowconfigure(0, weight=1)
    rightData.grid_columnconfigure(0, weight=1)

    return student_frame
