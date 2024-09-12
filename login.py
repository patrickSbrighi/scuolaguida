from customtkinter import *
import tkinter.messagebox as msg
import connection
import menu

def create_login_window():
    def login():
        username = usernameEntry.get()
        password = passwordEntry.get()
        if connection.is_Present(username, password):
            win.withdraw()
            menu_window = menu.create_menu_window()
            menu_window.mainloop()
            

        else:  
            return msg.showerror("Errore", "Username o password errati.")
        

        
    win = CTk()
    win.geometry('930x478')
    win.resizable(True, True)
    win.title('login')

    lbl = CTkLabel(win, text='Accedi con username and password')
    lbl.place(relx=0.5, rely=0.3, anchor='center')
    usernameEntry = CTkEntry(win, placeholder_text='Enter with your username')
    usernameEntry.place(relx=0.5, rely=0.4, anchor='center')
    passwordEntry = CTkEntry(win, placeholder_text='Enter with your password', show='*')
    passwordEntry.place(relx=0.5, rely=0.5, anchor='center')

    loginbtn = CTkButton(win, text='Login', cursor='hand2', command=login)
    loginbtn.place(relx=0.5, rely=0.6, anchor='center')

    return win

