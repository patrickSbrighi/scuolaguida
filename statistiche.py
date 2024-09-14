from tkinter import *
from tkinter import ttk
from connection import *
from customtkinter import *

def create_statistiche_frame(parent_frame):

    def clearEsaminatori():
        for item in treeEsamnatori.get_children():
            treeEsamnatori.delete(item)

    def updateEsaminatori():
        clearEsaminatori()
        for ex in get_perc_esaminatori():
            if ex[2] is None:
                ex = list(ex)
                ex[2] = 0
            treeEsamnatori.insert('', END, values=ex)


    def clearIstruttoriPratici():
        for item in treeIstruttoriPratici.get_children():
            treeIstruttoriPratici.delete(item)

    def updateIstruttoriPratici():
        clearIstruttoriPratici()
        for ist in get_classifica_istruttori():
            treeIstruttoriPratici.insert('',END,values=ist)

    def clearIstruttoriTeorici():
        for item in treeIstruttoriTeorici.get_children():
            treeIstruttoriTeorici(item)

    def updateIstruttoriTeorici():
        clearIstruttoriTeorici()
        for ist in get_media_errori():
            treeIstruttoriTeorici.insert('',END,values=ist)

    window_bg_color = parent_frame.cget("fg_color")

    window = CTkFrame(parent_frame, fg_color=window_bg_color)
    window.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    statisticsFrame = Frame(window)
    statisticsFrame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
    
    window.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)
    parent_frame.grid_rowconfigure(0, weight=1)
    parent_frame.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    statisticsFrame.grid_rowconfigure(0, weight=1)
    statisticsFrame.grid_columnconfigure(1, weight=1)

    lblEsaminatori = Label(statisticsFrame, text='Bocciature per esaminatore:', font=('Arial', 12))
    lblEsaminatori.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

    treeEsamnatori = ttk.Treeview(statisticsFrame, columns=('Nome', 'Cognome', '%'), show="headings", height=5)
    treeEsamnatori.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
    treeEsamnatori.column('Nome', width=80, anchor='center')
    treeEsamnatori.column('Cognome', width=80, anchor='center')
    treeEsamnatori.column('%', width=80, anchor='center')
    treeEsamnatori.heading('Nome', text='Nome')
    treeEsamnatori.heading('Cognome', text='Cognome')
    treeEsamnatori.heading('%', text='%')

    scrittaScadenze = 'Percentuale scadenze iscrizioni: ' + str(get_perc_scadenze()[0][0]) + '%'
    lblScadenze = Label(statisticsFrame, text=scrittaScadenze, font=('Arial', 12))
    lblScadenze.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    lblIstruttoriPratici = Label(statisticsFrame, text='Classifica istruttori pratici:', font=('Arial', 12))
    lblIstruttoriPratici.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    treeIstruttoriPratici = ttk.Treeview(statisticsFrame, columns=('Nome', 'Cognome', 'Passati'), show="headings",height=5)
    treeIstruttoriPratici.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
    treeIstruttoriPratici.column('Nome', width=80, anchor='center')
    treeIstruttoriPratici.column('Cognome', width=80, anchor='center')
    treeIstruttoriPratici.column('Passati', width=80, anchor='center')
    treeIstruttoriPratici.heading('Nome', text='Nome')
    treeIstruttoriPratici.heading('Cognome', text='Cognome')
    treeIstruttoriPratici.heading('Passati', text='Promossi')

    scrittaPrimoColpo = 'Percentuale studenti che passano gli esami al primo tentativo: ' + str(get_perc_primo_tentativo()[0][0]) + '%'
    lblPrimoColpo = Label(statisticsFrame, text=scrittaPrimoColpo, font=('Arial', 12))
    lblPrimoColpo.grid(row=5, column=0, padx=5, pady=5, sticky="w")

    lblIstruttoriTeorici = Label(statisticsFrame, text='Media degli errori per ogni istruttore teorico:', font=('Arial', 12))
    lblIstruttoriTeorici.grid(row=6, column=0, padx=5, pady=5, sticky="w")

    treeIstruttoriTeorici = ttk.Treeview(statisticsFrame, columns=('Nome', 'Cognome', 'Errori'), show="headings", height=5)
    treeIstruttoriTeorici.grid(row=6, column=1, padx=5, pady=5, sticky="nsew")
    treeIstruttoriTeorici.column('Nome', width=80, anchor='center')
    treeIstruttoriTeorici.column('Cognome', width=80, anchor='center')
    treeIstruttoriTeorici.column('Errori', width=80, anchor='center')
    treeIstruttoriTeorici.heading('Nome', text='Nome')
    treeIstruttoriTeorici.heading('Cognome', text='Cognome')
    treeIstruttoriTeorici.heading('Errori', text='Errori')

    scrittaTempoMedioPatente = 'Tempo medio di presa della patente: ' + str(get_tempo_medio_patente()[0][0]) + ' mesi'
    lblTempoMedioPatente = Label(statisticsFrame, text=scrittaTempoMedioPatente, font=('Arial', 12))
    lblTempoMedioPatente.grid(row=7, column=0, padx=5, pady=5, sticky="w")

    scrittaTempoMedioTeorico = 'Tempo medio promozione esame teorico: ' + str(get_tempo_medio_patente()[0][0]) + ' mesi'
    lblTempoMedioTeorico = Label(statisticsFrame, text=scrittaTempoMedioTeorico, font=('Arial', 12))
    lblTempoMedioTeorico.grid(row=8, column=0, padx=5, pady=5, sticky="w")

    updateEsaminatori()
    updateIstruttoriPratici()
    updateIstruttoriTeorici()

    return window