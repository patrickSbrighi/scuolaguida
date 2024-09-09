from customtkinter import *
import tkinter.messagebox as msg
import connection

def login():
    username = usernameEntry.get()
    password = passwordEntry.get()
    if connection.is_Present(username, password):
        return msg.showinfo("Login", "Login effettuato con successo!")
    
    return msg.showerror("Errore", "Username o password errati.")
    

    
win = CTk()
win.geometry('930x478')
win.resizable(0,0)
win.title('login')

lbl = CTkLabel(win, text='Login with username and password')
lbl.place(relx=0.5, rely=0.3, anchor='center')
usernameEntry = CTkEntry(win, placeholder_text='Enter with your username')
usernameEntry.place(relx=0.5, rely=0.4, anchor='center')
passwordEntry = CTkEntry(win, placeholder_text='Enter with your password', show='*')
passwordEntry.place(relx=0.5, rely=0.5, anchor='center')

loginbtn = CTkButton(win, text='Login', cursor='hand2', command=login)
loginbtn.place(relx=0.5, rely=0.6, anchor='center')

win.mainloop()

