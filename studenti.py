from tkcalendar import Calendar
from customtkinter import *
from tkinter import Button, Toplevel, ttk
import tkinter.messagebox as msg
import connection

def create_student_frame(parent_frame):
    def populate_treeview(tree, data):
        for student in tree.get_children():
            tree.delete(student)

        for row in data:
            tree.insert("", "end", values=row)

    def seleziona_data():
        def conferma_data():
            data_selezionata = cal.selection_get()
            giorno_settimana = data_selezionata.weekday()
            if giorno_settimana in (5, 6):
                msg.showerror("Errore", "Non puoi selezionare sabato o domenica!")
                return
            dateEntry.delete(0, END)
            dateEntry.insert(0, data_selezionata.strftime("%Y-%m-%d"))
            cal_finestra.destroy()

        cal_finestra = Toplevel(parent_frame)
        cal_finestra.grab_set()

        cal = Calendar(cal_finestra, selectmode='day', date_pattern='yyyy-mm-dd')
        cal.grid(row=0, column=0, pady=20)

        conferma_button = Button(cal_finestra, text="Conferma", command=conferma_data)
        conferma_button.grid(row=1, column=0, pady=10, sticky="w")


    def add():
        CF = CFEntry.get()
        name = nameEntry.get()
        surname = surnameEntry.get()
        address = addressEntry.get()
        phone = phoneEntry.get()
        date = dateEntry.get()
        
        if not CF or not name or not surname or not address or not phone or not date:
            msg.showerror('Error', "Fill all attributes")
        else:
            try:

                connection.addStudent(CF, name, surname, address, phone, date)
                

                CFEntry.delete(0, 'end')
                nameEntry.delete(0, 'end')
                surnameEntry.delete(0, 'end')
                addressEntry.delete(0, 'end')
                phoneEntry.delete(0, 'end')
                dateEntry.delete(0, 'end')
            
            except Exception as e:
                msg.showerror("Errore", f"Si è verificato un errore: {str(e)}")

            data = connection.showStudent()
            populate_treeview(tree, data)

    student_frame = CTkFrame(parent_frame)
    student_frame.grid(row=0, column=0, sticky="nsew")


    parent_frame.grid_rowconfigure(0, weight=1)
    parent_frame.grid_columnconfigure(0, weight=1)

    window_bg_color = student_frame.cget("fg_color")



    leftFrame = CTkFrame(student_frame, fg_color=window_bg_color)
    leftFrame.grid(row=0, column=0, sticky="ns", padx=5, pady=5)

    rightData = CTkFrame(student_frame, fg_color=window_bg_color) 
    rightData.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)


    student_frame.grid_rowconfigure(0, weight=1)
    student_frame.grid_columnconfigure(0, weight=0)  
    student_frame.grid_columnconfigure(1, weight=1)  


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

    calButtonGuida = CTkButton(leftFrame, text="Seleziona", command=lambda:seleziona_data())
    calButtonGuida.grid(row=5, column=2, pady=10, sticky="ew")


    addbtn = CTkButton(leftFrame, text='Aggiungi', cursor='hand2', command=add)
    addbtn.grid(row=len(labels_entries), column=0, columnspan=2, padx=5, pady=5)


    tree = ttk.Treeview(rightData, columns=('CF', 'Nome', 'Cognome', 'Indirizzo', 'Recapito Telefonico', 'Data di Nascita'), show='headings', height=8)


    tree.heading('CF', text='CF', anchor='center')
    tree.heading('Nome', text='Nome', anchor='center')
    tree.heading('Cognome', text='Cognome', anchor='center')
    tree.heading('Indirizzo', text='Indirizzo', anchor='center')
    tree.heading('Recapito Telefonico', text='Recapito', anchor='center')
    tree.heading('Data di Nascita', text='Data di Nascita', anchor='center')

    for col in tree["columns"]:
        tree.column(col, width=50, anchor="w") 


    tree.pack(fill="both", expand=True)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Arial', 12, 'bold'))  
    style.configure("Treeview",font=('Arial', 12))


    data = connection.showStudent()
    populate_treeview(tree, data)

    rightData.grid_rowconfigure(0, weight=1)
    rightData.grid_columnconfigure(0, weight=1)

    return student_frame
