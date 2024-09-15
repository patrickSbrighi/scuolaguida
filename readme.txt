Istruzioni oer l'esecuzione:

- Lanciare XAMPP e aprire una connessione con MySQL
- Aprire MySQL Workbench e importare il file createDatabase.sql
- Installare lo schema scuolaguida su MySQL Workbench (credenziali: user='root', password='')
- Per la corretta esecuzione dell'applicazione è necessario installare le librerie Tkinter, CustomTkinter e tkcalendar
- Nello script di creazione del database è presente la creazione automatica di un admin di prova (username='admin', password='admin') per poter effettuare il login
- Avviare l'applicazione tramite il comando: 

======= Comando per Windows =======
python .\startproject.py

======= Comando per Linux e macOS =======
python ./startproject.py


Script per l'installazione delle librerie necessarie con pip: 

======= Comando per l' installazione Tkinter =======
pip install tk

======= Comando per l' installazione CustomTkinter =======
pip install customtkinter

======= Comando per l' installazione tkcalendar =======
pip install tkcalendar
