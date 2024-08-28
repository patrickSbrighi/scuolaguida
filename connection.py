import mysql.connector
import tkinter.messagebox as msg

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="scuolaguida"
)

mycursor = mydb.cursor()

def populate_db():
    sqlFormula = "INSERT INTO `scuolaguida`.`studenti` (`CFStudente`, `nome`, `cognome`, `indirzzo`, `recapito`, `dataNascita`) VALUES (%s, %s, %s, %s, %s, %s)"
    students = [("MNTGNN05R25C573M", "Giovanni", "Montalti", "Via Emilia Ponente", "331545630", "2005-10-25"),
                ("BNGGNS03E53C573W", "Agnese", "Benaglia", "Via Emilia Ponente", "3234569838", "2003-05-13")]

    mycursor.executemany(sqlFormula, students)

    mydb.commit()

def get_data():
    sql = "SELECT * FROM studenti WHERE cognome = 'Montalti'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for result in myresult:
        print(result)

def id_exist(cf):
    mycursor.execute('SELECT COUNT(*) FROM studenti WHERE CFStudente=%s', cf)
    result = mycursor.fechone()
    return result[0]>0

def verifica(username, password):
    query = "SELECT * FROM admin WHERE username = %s AND password = %s"
    mycursor.execute(query, (username, password))
    result = mycursor.fetchone()
    return result


def addPerson(CF, name, surname, address, phone, data):
    sql = "INSERT INTO `scuolaguida`.`studenti` (`CFStudente`, `nome`, `cognome`, `indirzzo`, `recapito`, `dataNascita`) VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, (CF, name, surname, address, phone, data))

    mydb.commit()

def show_Person():
    sql="SELECT CFStudente, nome, cognome, indirzzo, recapito, dataNascita FROM studenti"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return data