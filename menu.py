from customtkinter import *
import studenti  # Assicurati che questo modulo esista e sia corretto
import iscrizione
import acquisti
import connection
import login
import esamiPratici

def create_menu_window():
    # Impostazioni del tema e dell'aspetto
    set_appearance_mode("white")  
    set_default_color_theme("blue") 

    
    # Creazione della finestra principale
    window = CTk()
    window.title('Menu Principale')
    window.geometry('930x478')
    window.resizable(True, True)

    window_bg_color = window.cget("fg_color")

    connection.delete_iscrizioni_scadute()


    # Configurazione delle righe e colonne per l'espansione
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    # Frame principale
    main_frame = CTkFrame(window, corner_radius=15, fg_color=window_bg_color)
    main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Configurazione delle righe e colonne nel frame principale
    main_frame.grid_rowconfigure(0, weight=0)
    main_frame.grid_rowconfigure(1, weight=1)
    main_frame.grid_columnconfigure(0, weight=0)
    main_frame.grid_columnconfigure(1, weight=1)

    # Titolo principale
    titleLabel = CTkLabel(main_frame, text='Scuola guida', font=('Arial', 30, 'bold'))
    titleLabel.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(10, 0))

    def logout():
        window.destroy()
        login_window = login.create_login_window()  # Crea una nuova finestra di login
        login_window.mainloop()

    # Bottone Logout posizionato nell'angolo in alto a destra
    logoutButton = CTkButton(main_frame, text='Logout', font=('Arial', 15), command=logout)
    logoutButton.grid(row=0, column=1, sticky="ne", padx=(0, 10), pady=(10, 0))

    # Frame sinistro per il menu
    leftFrame = CTkFrame(main_frame, width=200, corner_radius=10, fg_color=window_bg_color)
    leftFrame.grid(row=1, column=0, sticky="ns", padx=(10, 0), pady=(10, 10))

    # Configurazione dell'espansione per il frame sinistro
    leftFrame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)

    # Frame destro per visualizzare i contenuti
    rightFrame = CTkFrame(main_frame)
    rightFrame.grid(row=1, column=1, sticky="nsew", padx=(10, 10), pady=(10, 10))

    # Funzione per mostrare il frame degli studenti
    def show_student_frame():
        # Cancella eventuali frame esistenti nel rightFrame
        for widget in rightFrame.winfo_children():
            widget.destroy()
        
        # Crea e visualizza il frame degli studenti
        student_frame = studenti.create_student_frame(rightFrame)
        student_frame.grid(row=0, column=0, sticky="nsew")

    def show_iscrizioni_frame():
        # Cancella eventuali frame esistenti nel rightFrame
        for widget in rightFrame.winfo_children():
            widget.destroy()
        
        # Crea e visualizza il frame degli studenti
        student_frame = iscrizione.create_iscrizioni_frame(rightFrame)
        student_frame.grid(row=0, column=0, sticky="nsew")

    def show_acquisti_frame():
        # Cancella eventuali frame esistenti nel rightFrame
        for widget in rightFrame.winfo_children():
            widget.destroy()
        
        # Crea e visualizza il frame degli studenti
        student_frame = acquisti.create_acquisti_frame(rightFrame)
        student_frame.grid(row=0, column=0, sticky="nsew")

    def show_esamipratici_frame():
        # Cancella eventuali frame esistenti nel rightFrame
        for widget in rightFrame.winfo_children():
            widget.destroy()
        
        # Crea e visualizza il frame degli studenti
        esamiPratici_frame = esamiPratici.create_esamipratici_frame(rightFrame)
        esamiPratici_frame.grid(row=0, column=0, sticky="nsew")


    # Etichetta del Menu
    menuLabel = CTkLabel(leftFrame, text='Menu', font=('Arial', 15))
    menuLabel.grid(row=0, column=0, sticky="ew", pady=5)

    # Bottoni di navigazione nel menu
    studentsButton = CTkButton(leftFrame, text='Studenti', font=('Arial', 15), command=show_student_frame)
    studentsButton.grid(row=1, column=0, sticky="ew", padx=10, pady=5)

    iscrizioneButton = CTkButton(leftFrame, text='Iscrizioni', font=('Arial', 15), command=show_iscrizioni_frame)
    iscrizioneButton.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

    salesButton = CTkButton(leftFrame, text='Acquisti', font=('Arial', 15), command=show_acquisti_frame)
    salesButton.grid(row=3, column=0, sticky="ew", padx=10, pady=5)

    prenotazioneButton = CTkButton(leftFrame, text='Prenotazioni', font=('Arial', 15))
    prenotazioneButton.grid(row=4, column=0, sticky="ew", padx=10, pady=5)

    teoriaButton = CTkButton(leftFrame, text='Esami teorici', font=('Arial', 15))
    teoriaButton.grid(row=5, column=0, sticky="ew", padx=10, pady=5)

    praticaButton = CTkButton(leftFrame, text='Esami pratici', font=('Arial', 15))
    praticaButton.grid(row=6, column=0, sticky="ew", padx=10, pady=5)

    lezioniButton = CTkButton(leftFrame, text='Lezioni', font=('Arial', 15))
    lezioniButton.grid(row=7, column=0, sticky="ew", padx=10, pady=5)

    statisticheButton = CTkButton(leftFrame, text='Statistiche', font=('Arial', 15))
    statisticheButton.grid(row=8, column=0, sticky="ew", padx=10, pady=5)

    impostazioniButton = CTkButton(leftFrame, text='Impostazioni', font=('Arial', 15))
    impostazioniButton.grid(row=9, column=0, sticky="ew", padx=10, pady=5)

    # Loop principale dell'applicazione
    return window
