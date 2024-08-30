import mysql.connector
import tkinter.messagebox as msg

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Monta100!",
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

def show_Student():
    sql="SELECT CFStudente, nome, cognome FROM studenti"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return data

def show_Patenti():
    sql="SELECT nome FROM tipologiepatenti"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return data

def show_Pratici():
    sql="SELECT CFIstruttorePratico, nome, cognome FROM istruttoripratici"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return data

def show_Teorici():
    sql="SELECT CFIstruttoreTeorico, nome, cognome FROM istruttoriteorici"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return data

def add_iscrizione(CFStudente, CFTeorico, CFPratico, data, tipo):
    mycursor.execute("select idTipologia from tipologiepatenti where nome=%s", (tipo,))
    idTipologia = mycursor.fetchone()[0]

    # Inserisci un nuovo record in 'iscrizioni'
    mycursor.execute(
        "INSERT INTO scuolaguida.iscrizioni (dataInizio, CFStudente, idTipologia, costo, chiusa, CFIstruttoreTeorico, CFIstruttorePratico) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (data, CFStudente, idTipologia, '500', 'N', CFTeorico, CFPratico)
    )

    # Recupera l'idStudente
    mycursor.execute("SELECT idStudente FROM scuolaguida.iscrizioni WHERE CFStudente = %s", (CFStudente,))
    idStudente = mycursor.fetchone()[0]  # Recupera il primo elemento della tupla

    # Inserisci un nuovo record in 'acquisti'
    mycursor.execute(
        "INSERT INTO scuolaguida.acquisti (costoTotale, idStudente) VALUES (%s, %s)", 
        ('500', idStudente)
    )

    # Recupera l'idAcquisto
    mycursor.execute("SELECT LAST_INSERT_ID()")
    idAcquisto = mycursor.fetchone()[0]  # Recupera l'id dell'ultimo inserimento

    # Inserisci un nuovo record in 'fatture'
    mycursor.execute(
        "INSERT INTO scuolaguida.fatture (importoLordo, IVA, importoNetto, idAcquisto) VALUES (%s, %s, %s, %s)",
        ('610', '22', '500', idAcquisto)
    )

    # Applica le modifiche
    mydb.commit()


