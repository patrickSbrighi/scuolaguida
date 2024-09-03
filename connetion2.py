import mysql.connector
import tkinter.messagebox as msg

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="scuolaguida"
    )
    mycursor = mydb.cursor()
except:
    msg.showerror('Error', 'Connection with database failed')

def get_veicoli():
    try:
        sql="SELECT * FROM scuolaguida.veicoli"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
    except:
        msg.showerror('Error', 'Database is not responding')

def add_veicolo(targa, modello):
    if not targa or not modello:
        msg.showerror('Error', 'Fill all attribute')
    else:
        try:
            sql="INSERT INTO scuolaguida.veicoli (`targa`, `modello`) VALUES (%s, %s)"
            mycursor.execute(sql, (targa, modello))
            mydb.commit()
        except:
            msg.showerror('Error', 'Operation failed')

def get_tipologie():
    try:
        sql = "SELECT nome, eta FROM scuolaguida.tipologiepatenti"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
    except:
        msg.showerror('Error', 'Database is not responding')

def add_tipologia(nome, eta):
    if not nome or not eta:
        msg.showerror('Error', 'Fill all attribute')
    else:
        try:
            sql="INSERT INTO `scuolaguida`.`tipologiepatenti` (`nome`, `eta`) VALUES (%s, %s);"
            mycursor.execute(sql, (nome, eta))
            mydb.commit()
        except:
            msg.showerror('Error', 'Operation failed')

def get_admins():
    try:
        sql = "SELECT username FROM scuolaguida.admins;"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
    except:
        msg.showerror('Error', 'Database is not responding')

def add_admin(username, password):
    if not username or not password:
        msg.showerror('Error', 'Fill all attribute')
    else:
        try:
            sql="INSERT INTO `scuolaguida`.`admins` (`username`, `password`) VALUES (%s, %s)"
            mycursor.execute(sql, (username, password))
            mydb.commit()
        except:
            msg.showerror('Error', 'Operation failed')


