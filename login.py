from customtkinter import *
import tkinter.messagebox as msg
import connection
import menu

def create_login_window(window):
    def login():
        username = usernameEntry.get()
        password = passwordEntry.get()
        if connection.is_Present(username, password):
            menu_window = menu.create_menu_window(win)
            menu_window.mainloop()
        else:  
            return msg.showerror("Errore", "Username o password errati.")

        
    
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    
    win = CTkFrame(window)
    win.grid(row=0, column=0, sticky="nsew")

    lbl = CTkLabel(win, text='Accedi con username and password')
    lbl.place(relx=0.5, rely=0.3, anchor='center')
    usernameEntry = CTkEntry(win, placeholder_text='Username')
    usernameEntry.place(relx=0.5, rely=0.4, anchor='center')
    passwordEntry = CTkEntry(win, placeholder_text='Password', show='*')
    passwordEntry.place(relx=0.5, rely=0.5, anchor='center')

    loginbtn = CTkButton(win, text='Login', command=login)
    loginbtn.place(relx=0.5, rely=0.6, anchor='center')

    return window

