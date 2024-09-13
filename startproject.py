import login
from customtkinter import *

window = CTk()
window.geometry('930x478')
window.resizable(True, True)
window.title('login')

login.create_login_window(window)

window.mainloop()