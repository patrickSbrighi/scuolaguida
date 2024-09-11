import mysql.connector
import tkinter.messagebox as msg

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Monta100!",
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

def get_perc_esaminatori():
     try: 
        sql = "SELECT nome, cognome, CAST(bocciati*100/totale AS DECIMAL(10,0)) AS percentuale FROM (SELECT E.CFEsaminatore, E.nome, E.cognome, bocciati, COUNT(I.idStudente) totale FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamipratici EP ON I.idStudente = EP.idStudente JOIN scuolaguida.esaminatori E ON E.CFEsaminatore = EP.CFEsaminatore JOIN (SELECT E.CFEsaminatore, COUNT(I.idStudente) bocciati FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamipratici EP ON I.idStudente = EP.idStudente JOIN scuolaguida.esaminatori E ON E.CFEsaminatore = EP.CFEsaminatore WHERE EP.esito = 0 GROUP BY E.CFEsaminatore) Q ON E.CFEsaminatore = Q.CFEsaminatore GROUP BY E.CFEsaminatore, E.nome, E.cognome) perc"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
     except:
        msg.showerror('Error', 'Database is not responding')

def get_perc_scadenze():
     try: 
        sql = "SELECT CAST(scadute*100/tot AS DECIMAL(10,0)) AS perc FROM (SELECT COUNT(*) AS tot FROM scuolaguida.iscrizioni WHERE chiusa = 1) totale JOIN (SELECT COUNT(*) AS scadute FROM scuolaguida.iscrizioni WHERE chiusa = 1 AND idStudente NOT IN (SELECT I.idStudente FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamipratici E ON I.idStudente = E.idStudente WHERE chiusa = 1 AND esito = 1)) scad"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
     except:
        msg.showerror('Error', 'Database is not responding')

def get_classifica_istruttori():
     try: 
        sql = "SELECT I.nome, I.cognome, COUNT(I.CFIstruttorePratico) AS num FROM scuolaguida.istruttoripratici I JOIN scuolaguida.iscrizioni ISCR ON ISCR.CFIstruttorePratico = I.CFIstruttorePratico JOIN scuolaguida.esamipratici E ON ISCR.idStudente = E.idStudente WHERE chiusa = 1 AND esito = 1 GROUP BY(I.CFIstruttorePratico) ORDER BY(num) DESC"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
     except:
        msg.showerror('Error', 'Database is not responding')

def get_perc_primo_tentativo():
     try: 
        sql = "SELECT CAST(done*100/tot AS DECIMAL(10,0)) AS perc FROM (SELECT COUNT(*) AS done FROM (SELECT I.idStudente AS studTeor, COUNT(I.idStudente) AS num FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamiteorici E ON I.idStudente = E.idStudente WHERE I.idStudente IN (SELECT idStudente FROM scuolaguida.esamiteorici WHERE esito = 1) GROUP BY I.idStudente HAVING num = 1) teoria JOIN (SELECT I.idStudente AS studPrat, COUNT(I.idStudente) AS num FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamipratici E ON I.idStudente = E.idStudente WHERE I.idStudente IN (SELECT idStudente FROM scuolaguida.esamipratici WHERE esito = 1) GROUP BY I.idStudente HAVING num = 1) pratico ON studTeor = studPrat) conto JOIN (SELECT COUNT(*) AS tot FROM scuolaguida.iscrizioni WHERE chiusa=1) totale"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
     except:
        msg.showerror('Error', 'Database is not responding')

def get_media_errori():
     try: 
        sql = "SELECT T.nome, T.cognome, CAST(AVG(E.numErrori) AS DECIMAL(10,0)) AS mediaErrori FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamiteorici E ON I.idStudente = E.idStudente JOIN scuolaguida.istruttoriteorici T ON I.CFIstruttoreTeorico = T.CFIstruttoreTeorico GROUP BY T.CFIstruttoreTeorico"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
     except:
        msg.showerror('Error', 'Database is not responding')

def get_tempo_medio_patente():
     try: 
        sql = "SELECT CAST(AVG(mesi) AS DECIMAL(10,0)) as media FROM (SELECT PERIOD_DIFF(DATE_FORMAT(data , '%Y%m'), DATE_FORMAT(dataInizio, '%Y%m')) AS mesi FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamipratici E ON I.idStudente = E.idStudente WHERE chiusa = 1 AND esito = 1) months "
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
     except:
        msg.showerror('Error', 'Database is not responding')

def get_studenti_teorici():
     try: 
        sql = "SELECT stu.idStudente, stu.nome, stu.cognome FROM (SELECT I.idStudente, S.nome, S.cognome FROM scuolaguida.iscrizioni I JOIN scuolaguida.studenti S ON (I.CFStudente = S.CFStudente) JOIN scuolaguida.tipologiepatenti T ON (T.idTipologia = I.idTipologia) WHERE S.dataNascita < DATE_SUB(DATE_SUB(DATE_SUB(CURDATE(), INTERVAL T.eta YEAR), INTERVAL 1 MONTH), INTERVAL 1 DAY) AND I.chiusa = 0 AND I.idStudente NOT IN (SELECT I.idStudente FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamiteorici E ON (I.idStudente = E.idStudente) WHERE E.esito = 1) ORDER BY I.dataInizio) stu JOIN scuolaguida.acquisti A ON stu.idStudente = A.idStudente JOIN scuolaguida.esamiteorici ES ON A.idAcquisto = ES.idAcquisto WHERE ES.esito IS NULL"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
     except:
        msg.showerror('Error', 'Database is not responding')