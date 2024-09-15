from customtkinter import *
import studenti  
import iscrizione
import acquisti
import connection
import login
import esamiPratici
import selezionaPrenotazione
import esamiTeorici
import lezioni
import statistiche
import option

def create_menu_window(parent_frame):

    set_appearance_mode("white")  
    set_default_color_theme("blue") 
    parent_frame.grid_rowconfigure(0, weight=1)
    parent_frame.grid_columnconfigure(0, weight=1)
    

    window_bg_color = parent_frame.cget("fg_color")

    window = CTkFrame(parent_frame, fg_color=window_bg_color)
    window.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    connection.deleteIscrizioniScadute()


    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)


    main_frame = CTkFrame(window, corner_radius=15, fg_color=window_bg_color)
    main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")


    main_frame.grid_rowconfigure(0, weight=0)
    main_frame.grid_rowconfigure(1, weight=1)
    main_frame.grid_columnconfigure(0, weight=0)
    main_frame.grid_columnconfigure(1, weight=1)


    titleLabel = CTkLabel(main_frame, text='Scuola guida', font=('Arial', 30, 'bold'))
    titleLabel.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(10, 0))

    def logout():
        login_window = login.create_login_window(parent_frame)  
        login_window.mainloop()


    logoutButton = CTkButton(main_frame, text='Logout', font=('Arial', 15), command=logout)
    logoutButton.grid(row=0, column=1, sticky="ne", padx=(0, 10), pady=(10, 0))


    leftFrame = CTkFrame(main_frame, width=200, corner_radius=10, fg_color=window_bg_color)
    leftFrame.grid(row=1, column=0, sticky="ns", padx=(10, 0), pady=(10, 10))


    leftFrame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)


    rightFrame = CTkFrame(main_frame)
    rightFrame.grid(row=1, column=1, sticky="nsew", padx=(10, 10), pady=(10, 10))


    def show_student_frame():

        for widget in rightFrame.winfo_children():
            widget.destroy()
        

        student_frame = studenti.create_student_frame(rightFrame)
        student_frame.grid(row=0, column=0, sticky="nsew")

    def show_iscrizioni_frame():

        for widget in rightFrame.winfo_children():
            widget.destroy()
        

        student_frame = iscrizione.create_iscrizioni_frame(rightFrame)
        student_frame.grid(row=0, column=0, sticky="nsew")

    def show_acquisti_frame():

        for widget in rightFrame.winfo_children():
            widget.destroy()
        

        student_frame = acquisti.create_acquisti_frame(rightFrame)
        student_frame.grid(row=0, column=0, sticky="nsew")

    def show_esamipratici_frame():

        for widget in rightFrame.winfo_children():
            widget.destroy()
        

        esamiPratici_frame = esamiPratici.create_esamipratici_frame(rightFrame)
        esamiPratici_frame.grid(row=0, column=0, sticky="nsew")

    def show_prenotazione_frame():

        for widget in rightFrame.winfo_children():
            widget.destroy()
        

        prenotazione_frame = selezionaPrenotazione.create_seleziona_studente(rightFrame)
        prenotazione_frame.grid(row=0, column=0, sticky="nsew")

    def show_esamiteorici_frame():

        for widget in rightFrame.winfo_children():
            widget.destroy()
        

        esamiTeorici_frame = esamiTeorici.create_esamiteorici_frame(rightFrame)
        esamiTeorici_frame.grid(row=0, column=0, sticky="nsew")


    def show_lezioni_frame():

        for widget in rightFrame.winfo_children():
            widget.destroy()

        lezioni_frame = lezioni.create_lezioni_frame(rightFrame)
        lezioni_frame.grid(row=0, column=0, sticky="nsew")


    def show_statistiche_frame():

        for widget in rightFrame.winfo_children():
            widget.destroy()
        

        lezioni_frame = statistiche.create_statistiche_frame(rightFrame)
        lezioni_frame.grid(row=0, column=0, sticky="nsew")

    def show_impostazioni_frame():

        for widget in rightFrame.winfo_children():
            widget.destroy()
        

        impostazioni_frame = option.create_impostazioni_frame(rightFrame)
        impostazioni_frame.grid(row=0, column=0, sticky="nsew")



    menuLabel = CTkLabel(leftFrame, text='Menu', font=('Arial', 15))
    menuLabel.grid(row=0, column=0, sticky="ew", pady=5)


    studentsButton = CTkButton(leftFrame, text='Studenti', font=('Arial', 15), command=show_student_frame)
    studentsButton.grid(row=1, column=0, sticky="ew", padx=10, pady=5)

    iscrizioneButton = CTkButton(leftFrame, text='Iscrizioni', font=('Arial', 15), command=show_iscrizioni_frame)
    iscrizioneButton.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

    salesButton = CTkButton(leftFrame, text='Acquisti', font=('Arial', 15), command=show_acquisti_frame)
    salesButton.grid(row=3, column=0, sticky="ew", padx=10, pady=5)

    prenotazioneButton = CTkButton(leftFrame, text='Prenotazioni', font=('Arial', 15), command=show_prenotazione_frame)
    prenotazioneButton.grid(row=4, column=0, sticky="ew", padx=10, pady=5)

    teoriaButton = CTkButton(leftFrame, text='Esami teorici', font=('Arial', 15), command=show_esamiteorici_frame)
    teoriaButton.grid(row=5, column=0, sticky="ew", padx=10, pady=5)

    praticaButton = CTkButton(leftFrame, text='Esami pratici', font=('Arial', 15), command=show_esamipratici_frame)
    praticaButton.grid(row=6, column=0, sticky="ew", padx=10, pady=5)

    lezioniButton = CTkButton(leftFrame, text='Lezioni', font=('Arial', 15), command=show_lezioni_frame)
    lezioniButton.grid(row=7, column=0, sticky="ew", padx=10, pady=5)

    statisticheButton = CTkButton(leftFrame, text='Statistiche', font=('Arial', 15), command=show_statistiche_frame)
    statisticheButton.grid(row=8, column=0, sticky="ew", padx=10, pady=5)

    impostazioniButton = CTkButton(leftFrame, text='Impostazioni', font=('Arial', 15), command=show_impostazioni_frame)
    impostazioniButton.grid(row=9, column=0, sticky="ew", padx=10, pady=5)

    
    return window
