from tkinter import *
from tkinter import ttk
from customtkinter import *
import connection


set_appearance_mode("light")  
set_default_color_theme("blue")

def clear_frame(frame):
    # Cancella tutti i widget figli del frame
    for widget in frame.winfo_children():
        widget.destroy()

def viewStudentTeorico():

    clear_frame(center_frame)
    clear_frame(center_frame_top)


    def on_select(event):
    # Ottiene l'indice dell'elemento selezionato
        selected_index = listbox.curselection()
        if selected_index:
            # Prende il valore dell'elemento selezionato
            selected_item = listbox.get(selected_index)
            selected = CTkLabel(center_frame, text=f"Desidera acquistare un esame per lo studente: {selected_item.split()[1]} {selected_item.split()[2]}")
            selected.pack(side=TOP, padx=10, pady=10)
            btnAcquista = CTkButton(center_frame, text="Acquista", command=connection.addAcquisto(selected_item.split()[0], 100))
            btnAcquista.pack(side=BOTTOM, padx=10, pady=10)
    

    listbox.delete(0,END)

    elements = connection.showIscrittiTeorico()

    for element in elements:
        str = element[0] + " " + element[1] + " " + element[2] +" " +element[3]
        listbox.insert(END, str)

    listbox.bind("<<ListboxSelect>>", on_select)
    

def viewStudentPratico():

    clear_frame(center_frame)
    clear_frame(center_frame_top)

    def on_select(event):
    # Ottiene l'indice dell'elemento selezionato
        selected_index = listbox.curselection()
        if selected_index:
            # Prende il valore dell'elemento selezionato
            selected_item = listbox.get(selected_index)
            selected= CTkLabel(center_frame, text=f"Desidera acquistare un esame per lo studente: {selected_item.split()[1]} {selected_item.split()[2]}")
            selected.pack(side=TOP, padx=10, pady=10)
            btnAcquista = CTkButton(center_frame, text="Acquista", command=connection.addAcquisto(selected_item.split()[0], 100))
            btnAcquista.pack(side=BOTTOM, padx=10, pady=10)
    

    listbox.delete(0,END)

    elements = connection.showIscrittiPratico()

    for element in elements:
        str = f"{element[0]} {element[1]} {element[2]} numero guide {element[3]}"
        listbox.insert(END, str)

    listbox.bind("<<ListboxSelect>>", on_select)
    
def viewPacchetti():

    clear_frame(center_frame)
    clear_frame(center_frame_top)

    def on_select(event):
        # Ottiene l'indice dell'elemento selezionato
        selected_index = listbox.curselection()
        if selected_index:
            # Prende il valore dell'elemento selezionato
            selected_item = listbox.get(selected_index)
            selected =CTkLabel(center_frame, text=f"Desidera acquistare un pacchetto per lo studente: {selected_item.split()[1]} {selected_item.split()[2]}")
            selected.pack(side=TOP, padx=10, pady=10)
            
            btnAcquista = CTkButton(center_frame, text="Acquista", command=lambda: connection.addAcquistoPacchetti(selected_item.split()[0], pacchettichoosen.get().split()[1]))
            btnAcquista.pack(side=BOTTOM, padx=10, pady=10)
    

    listbox.delete(0,END)
    

    elements = connection.showIscrittiPacchetti()

    for element in elements:
        str = f"{element[0]} {element[1]} {element[2]} guide mancanti {element[3]}"
        listbox.insert(END, str)

    CTkLabel(center_frame_top, text="seleziona pacchetto :").pack(side=LEFT, padx=10, pady=10)
    
    pacchettichoosen = ttk.Combobox(center_frame_top, width = 20)
    pacchettichoosen.pack(side=LEFT, padx=10, pady=10)

    pacchetti = ['Pacchetto 1 guida', 'Pacchetto 5 guide', 'Pacchetto 10 guide', 'Pacchetto 15 guide']
    pacchettichoosen['values'] = pacchetti

    listbox.bind("<<ListboxSelect>>", on_select)



window = CTk()
window.title('Acquisti')
window.geometry('970x478')
window.resizable(True,True)

window_bg_color = window.cget("fg_color")

topframe = CTkFrame(window,fg_color=window_bg_color)
topframe.pack(side=TOP, fill=X, padx=20, pady=20)

center_frame = CTkFrame(window, fg_color=window_bg_color)
center_frame.pack(side=BOTTOM, expand=True)

center_frame_top = CTkFrame(window, fg_color=window_bg_color)
center_frame_top.pack(side=BOTTOM, expand=True)

label = CTkLabel(topframe, text="Seleziona acquisto")
label.pack(side=TOP, pady=10)

btnpratico = CTkButton(topframe, text='Esame Pratico',command=viewStudentPratico)
btnpratico.pack(side=LEFT, padx=10, pady=10, expand=True, fill=BOTH)
btnteorico = CTkButton(topframe, text='Esame Teorico', command=viewStudentTeorico)
btnteorico.pack(side=LEFT, padx=10, pady=10, expand=True, fill=BOTH)
btnpacchetti = CTkButton(topframe, text='Pacchetto guide', command=viewPacchetti)
btnpacchetti.pack(side=LEFT, padx=10, pady=10, expand=True, fill=BOTH)


listbox = Listbox(window, selectmode=SINGLE, width=100, height=20)
listbox.pack(side=TOP, padx=20, pady=10, expand=True)



window.mainloop()