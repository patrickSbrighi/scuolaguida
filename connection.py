import mysql.connector
import tkinter.messagebox as msg

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="scuolaguida"
)

mycursor = mydb.cursor()

def deleteIscrizioniScadute():
    try:
        mycursor.execute("SELECT idStudente FROM scuolaguida.iscrizioni WHERE dataInizio <= DATE_SUB(CURDATE(), INTERVAL 1 YEAR) AND chiusa = '0'")
        data = mycursor.fetchall()

        for id in list(data):
            mycursor.execute("UPDATE scuolaguida.iscrizioni SET chiusa = '1' WHERE (idStudente = %s)", id)
            mydb.commit()

    except Exception as ex:
        msg.showerror('Error', ex)

# func in login
def isPresent(username, password):
    try:
        query = "SELECT * FROM admins WHERE username = %s AND password = %s"
        mycursor.execute(query, (username, password))
        result = mycursor.fetchone()
        return result
    except Exception as ex:
        msg.showerror('Error', ex)

#func in studenti
def addStudent(CF, name, surname, address, phone, data):
    try:
        sql = "INSERT INTO `scuolaguida`.`studenti` (`CFStudente`, `nome`, `cognome`, `indirizzo`, `recapito`, `dataNascita`) VALUES (%s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql, (CF, name, surname, address, phone, data))

        mydb.commit()
    except Exception as ex:
        msg.showerror('Error', ex)

#func in studenti
def showStudent():
    try:
        sql="SELECT CFStudente, nome, cognome, indirizzo, recapito, dataNascita FROM studenti"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        return list(data)
    except Exception as ex:
        msg.showerror('Error', ex)

def showNonIscritti():
    try:
        sql="SELECT CFStudente, nome, cognome, indirizzo, recapito, dataNascita FROM scuolaguida.studenti WHERE CFStudente NOT IN (SELECT CFStudente FROM scuolaguida.iscrizioni WHERE chiusa = 0)"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        return list(data)
    except Exception as ex:
        msg.showerror('Error', ex)

#func in iscrizione
def showPatenti():
    try:
        sql="SELECT nome FROM tipologiepatenti"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        return data
    except Exception as ex:
        msg.showerror('Error', ex)

#func in iscrizione
def showPratici():
    try:
        sql="SELECT P.CFIstruttorePratico, P.nome, P.cognome, COUNT(idStudente) nStud \
            FROM scuolaguida.iscrizioni I RIGHT JOIN scuolaguida.istruttoripratici P ON (I.CFIstruttorePratico = P.CFIstruttorePratico) \
            GROUP BY CFIstruttorePratico \
            ORDER BY nStud \
            LIMIT 1"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        return data
    except Exception as ex:
        msg.showerror('Error', ex)

#func in iscrizione
def showTeorici():
    try:
        sql="SELECT CFIstruttoreTeorico, nome, cognome FROM istruttoriteorici"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        return data
    except Exception as ex:
        msg.showerror('Error', ex)

def getTipologiaFromNome(tipo):
    try: 
        sql = "SELECT idTipologia FROM tipologiepatenti WHERE nome=%s"
        mycursor.execute(sql, (tipo,))
        myresult = mycursor.fetchone()[0]
        return myresult
    except:
        msg.showerror('Error', 'Database is not responding')

def addAcquistoByID(costo, IDStud):
    try:
        sql="INSERT INTO `scuolaguida`.`acquisti` (`costoTotale`, `idStudente`) VALUES (%s, %s);"
        mycursor.execute(sql, (costo, IDStud))
        mydb.commit()
    except:
        msg.showerror('Error', 'Operation failed')

def addFattura(lordo, iva, netto, IDAcquisto):
    try:
        sql="INSERT INTO scuolaguida.fatture (importoLordo, IVA, importoNetto, idAcquisto) VALUES (%s, %s, %s, %s)"
        mycursor.execute(sql, (lordo, iva, netto, IDAcquisto))
        mydb.commit()
    except:
        msg.showerror('Error', 'Operation failed')

#func in iscrizione
def addIscrizione(CFStudente, CFTeorico, CFPratico, data, tipo, costo, iva):
    try:
        costo = int(costo)
        idTipologia = getTipologiaFromNome(tipo)

        mycursor.execute(
            "INSERT INTO scuolaguida.iscrizioni (dataInizio, CFStudente, idTipologia, costo, chiusa, CFIstruttoreTeorico, CFIstruttorePratico) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (data, CFStudente, idTipologia, costo, 0, CFTeorico, CFPratico)
        )
        
        mycursor.execute("SELECT LAST_INSERT_ID()")
        idStudente = mycursor.fetchone()[0] 
        addAcquistoByID(costo, idStudente)
        
        mycursor.execute("SELECT LAST_INSERT_ID()")
        idAcquisto = mycursor.fetchone()[0] 
        netto = costo - ((costo*iva)/100)
        addFattura(costo, iva, netto, idAcquisto)
    except Exception as ex:
        msg.showerror('Error', ex)

#func in iscrizione 
def showIscritti():
    try:
        sql = "select i.CFStudente, s.nome, s.cognome, t.nome from scuolaguida.iscrizioni i join scuolaguida.studenti s on (i.CFStudente = s.CFStudente) join scuolaguida.tipologiepatenti t on (i.idTipologia = t.idTipologia)where i.chiusa = '0';"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        return list(data)
    except Exception as ex:
        msg.showerror('Error', ex)

#func in iscrizione
def showGuideMancanti(CFStudente):
    try:
        mycursor.execute("select idStudente from iscrizioni where CFStudente = %s ORDER BY idStudente DESC LIMIT 1", (CFStudente,))
        idStudente = mycursor.fetchone()[0]
        

        sql = "SELECT (12 - count(g.idGuida)) mancanti \
            from scuolaguida.guide g join scuolaguida.pacchetti p on (g.idPacchetto = p.idPacchetto)\
            join scuolaguida.acquisti a on (p.idAcquisto = a.idAcquisto)\
            join scuolaguida.iscrizioni i on (a.idStudente = i.idStudente)\
            where i.chiusa = 0 and i.idStudente = %s"
        mycursor.execute(sql, (idStudente,) )
        data = mycursor.fetchone()
        if data[0] < 0:
            return 0
        else: 
            return data[0]
    except Exception as ex:
        msg.showerror('Error', ex)

def showIscrittiTeorico():
    try:
        sql = "SELECT I.idStudente, S.nome, S.cognome, T.nome FROM scuolaguida.iscrizioni I JOIN scuolaguida.studenti S ON (I.CFStudente = S.CFStudente) JOIN scuolaguida.tipologiepatenti T ON (T.idTipologia = I.idTipologia) WHERE S.dataNascita < DATE_SUB(DATE_SUB(DATE_SUB(CURDATE(), INTERVAL T.eta YEAR), INTERVAL 1 MONTH), INTERVAL 1 DAY) AND I.chiusa = 0 AND I.idStudente NOT IN (SELECT I.idStudente FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamiteorici E ON (I.idStudente = E.idStudente) WHERE E.esito = 1 OR E.esito IS NULL OR E.esito = '') ORDER BY I.dataInizio"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        return list(data)
    except Exception as ex:
        msg.showerror('Error', ex)

def addAcquistoTeorico(IDStudente, importo):
    try:
        mycursor.execute("insert into scuolaguida.acquisti (costoTotale, idStudente) values (%s, %s)", (importo, IDStudente))
        mycursor.execute("SELECT LAST_INSERT_ID()")
        idAcquisto = mycursor.fetchone()[0]

        mycursor.execute("insert into scuolaguida.esamiteorici (costo, idStudente, idAcquisto) values (%s, %s, %s)", (importo, IDStudente, idAcquisto ))
        importoNetto = importo - (importo*22)/100

        mycursor.execute("insert into scuolaguida.fatture (importoLordo, IVA, importoNetto, idAcquisto) values (%s, %s, %s, %s)", (importo, '22', importoNetto, idAcquisto))
        mydb.commit() 
    except mysql.connector.Error as err:
        print(f"Errore: {err}")
        mydb.rollback()

def addAcquistoPratico(idStudente, importo):
    try:
        mycursor.execute("insert into scuolaguida.acquisti (costoTotale, idStudente) values (%s, %s)", (importo, idStudente))
        mycursor.execute("SELECT LAST_INSERT_ID()")
        idAcquisto = mycursor.fetchone()[0]
        mycursor.execute("select CFEsaminatore from scuolaguida.esaminatori limit 1")
        CFEsaminatore = mycursor.fetchone()[0]
        mycursor.execute("insert into scuolaguida.esamipratici (costo, idStudente, CFEsaminatore, idAcquisto) values (%s, %s, %s, %s)", ('100', idStudente, CFEsaminatore, idAcquisto))
        importoNetto = importo - (importo*22)/100
        mycursor.execute("insert into scuolaguida.fatture (importoLordo, IVA, importoNetto, idAcquisto) values (%s, %s, %s, %s)", (importo, '22', importoNetto, idAcquisto))
        mydb.commit() 
    except Exception as ex:
        msg.showerror('Error', ex)

def showIscrittiPratico():
    try:
        sql="SELECT I.idStudente, S.nome, S.cognome, COUNT(DISTINCT G.idGuida) guide FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamiteorici E ON (I.idStudente = E.idStudente) JOIN scuolaguida.acquisti A ON (A.idStudente = I.idStudente) JOIN scuolaguida.pacchetti P ON (A.idAcquisto = P.idAcquisto) JOIN scuolaguida.guide G ON (G.IdPacchetto = P.IdPacchetto) JOIN scuolaguida.studenti S ON (I.CFStudente = S.CFStudente) WHERE I.chiusa = '0' AND I.idStudente IN (SELECT I.idStudente FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamiteorici E ON (I.idStudente = E.idStudente) WHERE E.esito = '1') AND I.idStudente NOT IN (SELECT I.idStudente FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamipratici E ON (I.idStudente = E.idStudente) WHERE E.esito = '1' OR E.esito IS NULL OR E.esito = '') GROUP BY I.idStudente HAVING guide >= 12 ORDER BY I.dataInizio"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        return list(data)
    except Exception as ex:
        msg.showerror('Error', ex)

def showIscrittiPacchetti():
    try:
        sql = "SELECT S.CFStudente, S.nome, S.cognome FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamiteorici E ON (I.idStudente = E.idStudente) JOIN scuolaguida.studenti S ON (S.CFStudente = I.CFStudente) WHERE I.chiusa = '0' AND I.idStudente IN (SELECT I.idStudente FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamiteorici E ON (I.idStudente = E.idStudente) WHERE E.esito = '1') AND I.idStudente NOT IN (SELECT I.idStudente FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamipratici E ON (I.idStudente = E.idStudente) WHERE E.esito = '1')  AND I.idStudente NOT IN (SELECT I.idStudente FROM scuolaguida.pacchetti P JOIN scuolaguida.acquisti A ON P.idAcquisto = A.idAcquisto JOIN scuolaguida.iscrizioni I ON A.idStudente = I.idStudente WHERE P.finito = 0) GROUP BY I.idStudente ORDER BY I.dataInizio"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        return list(data)
    except Exception as ex:
        msg.showerror('Error', ex)


def addAcquistoPacchetti(CFStudente, tipo):
    try:
        mycursor.execute("select idStudente from scuolaguida.iscrizioni where CFStudente = %s ORDER BY idStudente DESC LIMIT 1",(CFStudente,) )
        idStudente = mycursor.fetchone()[0]

        iva = 22
        if tipo=='1':
            importo='50'
        elif tipo=='5':
            importo='200'
        elif tipo=='10':
            importo='400'
        elif tipo=='15':
            importo='650'
        else:
            return
        

        sql = "insert into scuolaguida.acquisti (costoTotale, idStudente) values (%s, %s)"
        mycursor.execute(sql, (int(importo), idStudente))
        mycursor.execute("SELECT LAST_INSERT_ID()")
        idAcquisto = mycursor.fetchone()[0]

        mycursor.execute("insert into scuolaguida.pacchetti (prezzo, tipo, finito, idAcquisto) values (%s, %s, %s, %s)", (importo, tipo, 0, idAcquisto))
        addFattura(int(importo), iva, int(importo) - (int(importo)*iva/100), idAcquisto)
        mydb.commit()
    except Exception as ex:
        msg.showerror('Error', ex)


#connection2
def get_veicoli():
    try:
        sql="SELECT targa, modello FROM scuolaguida.veicoli"
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
        sql = "SELECT nome, cognome, CAST(bocciati*100/totale AS DECIMAL(10,0)) AS percentuale FROM (SELECT E.CFEsaminatore, E.nome, E.cognome, bocciati, COUNT(I.idStudente) totale FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamipratici EP ON I.idStudente = EP.idStudente JOIN scuolaguida.esaminatori E ON E.CFEsaminatore = EP.CFEsaminatore LEFT JOIN (SELECT E.CFEsaminatore, COUNT(I.idStudente) bocciati FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamipratici EP ON I.idStudente = EP.idStudente JOIN scuolaguida.esaminatori E ON E.CFEsaminatore = EP.CFEsaminatore WHERE EP.esito = 0 GROUP BY E.CFEsaminatore) Q ON E.CFEsaminatore = Q.CFEsaminatore GROUP BY E.CFEsaminatore, E.nome, E.cognome) perc"
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
        sql = "SELECT DISTINCT stu.idStudente, stu.nome, stu.cognome FROM (SELECT I.idStudente, S.nome, S.cognome FROM scuolaguida.iscrizioni I JOIN scuolaguida.studenti S ON (I.CFStudente = S.CFStudente) JOIN scuolaguida.tipologiepatenti T ON (T.idTipologia = I.idTipologia) WHERE S.dataNascita < DATE_SUB(DATE_SUB(DATE_SUB(CURDATE(), INTERVAL T.eta YEAR), INTERVAL 1 MONTH), INTERVAL 1 DAY) AND I.chiusa = 0 AND I.idStudente NOT IN (SELECT I.idStudente FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamiteorici E ON (I.idStudente = E.idStudente) WHERE E.esito = 1) ORDER BY I.dataInizio) stu JOIN scuolaguida.acquisti A ON stu.idStudente = A.idStudente JOIN scuolaguida.esamiteorici ES ON A.idAcquisto = ES.idAcquisto WHERE ES.esito IS NULL OR ES.esito = ''"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
     except:
        msg.showerror('Error', 'Database is not responding')

def add_esame_teorico(ID, errori, data):
    try:
        maxError = 3
        sql = "UPDATE `scuolaguida`.`esamiteorici` AS e\
            JOIN (SELECT `idEsame` \
                FROM `scuolaguida`.`esamiteorici` \
                WHERE `idStudente` = %s AND (`esito` IS NULL OR `esito` = '')) AS subquery \
            ON e.idEsame = subquery.idEsame\
            SET e.data = %s, e.esito = %s, e.numErrori = %s;"

        if int(errori) <= maxError:
            mycursor.execute(sql, (ID, data, 1, errori))
            mydb.commit()
        else:
            mycursor.execute(sql, (ID, data, 0, errori))
            mydb.commit()
    except Exception as ex:
        msg.showerror('Error', ex)

def get_studenti_pratici():
     try: 
        sql = "SELECT DISTINCT sub.idStudente, S.nome, S.cognome FROM (SELECT I.idStudente, I.CFStudente, COUNT(G.idGuida) guide FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamiteorici E ON (I.idStudente = E.idStudente) JOIN scuolaguida.acquisti A ON (A.idStudente = I.idStudente) JOIN scuolaguida.pacchetti P ON (A.idAcquisto = P.idAcquisto) JOIN scuolaguida.guide G ON (G.IdPacchetto = P.IdPacchetto) WHERE I.chiusa = '0' AND I.idStudente IN (SELECT I.idStudente FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamiteorici E ON (I.idStudente = E.idStudente) WHERE E.esito = '1') AND I.idStudente NOT IN (SELECT I.idStudente FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamipratici E ON (I.idStudente = E.idStudente) WHERE E.esito = '1') GROUP BY I.idStudente HAVING guide >= 12 ORDER BY I.dataInizio) sub JOIN scuolaguida.studenti S ON sub.CFStudente = S.CFStudente JOIN scuolaguida.acquisti A ON sub.idStudente = A.idStudente JOIN scuolaguida.esamipratici ES ON A.idAcquisto = ES.idAcquisto WHERE ES.esito IS NULL OR ES.esito = ''"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
     except:
        msg.showerror('Error', 'Database is not responding')

def add_esame_pratico(ID, esito, data, esaminatore):
    try:
        sql="UPDATE `scuolaguida`.`esamipratici` SET `data` = %s, `esito` = %s, `CFEsaminatore` = %s WHERE (`idStudente` = %s) AND (esito IS NULL OR esito ='');"
        mycursor.execute(sql, (data, esito, esaminatore, ID))
        mydb.commit()
    except:
        msg.showerror('Error', 'Operation failed')

def get_esaminatori():
     try: 
        sql = "SELECT CFEsaminatore, nome, cognome FROM scuolaguida.esaminatori;"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
     except:
        msg.showerror('Error', 'Database is not responding')

def get_studenti_per_guide():
     try: 
        sql = "SELECT I.idStudente, S.nome, S.cognome FROM scuolaguida.iscrizioni I JOIN scuolaguida.studenti S ON I.CFStudente = S.CFStudente JOIN scuolaguida.esamiteorici E ON I.idStudente = E.idStudente WHERE esito = 1 AND chiusa = 0"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
     except:
        msg.showerror('Error', 'Database is not responding')

def get_guide_future(id):
    try: 
        sql = "SELECT idGuida, data, ora, targa, CFIstruttorePratico FROM scuolaguida.guide G JOIN scuolaguida.pacchetti P ON  P.idPacchetto = G.idPacchetto JOIN scuolaguida.acquisti A ON A.idAcquisto = P.idAcquisto WHERE G.data >= CURDATE() AND A.idStudente = %s"
        mycursor.execute(sql, (id,))
        myresult = mycursor.fetchall()
        return myresult
    except:
        msg.showerror('Error', 'Database is not responding')

def get_disponibilita_istruttore(data, CF):
    try:
        sql = "SELECT ora FROM scuolaguida.guide WHERE data = %s AND CFIstruttorePratico = %s"
        mycursor.execute(sql, (data, CF))
        myresult = mycursor.fetchall()
        return myresult
    except Exception as e:
        msg.showerror('Error', f'Database is not responding: {e}')

def get_istruttore_pratico_studente(ID):
    try:
        sql = "SELECT CFIstruttorePratico FROM scuolaguida.iscrizioni WHERE idStudente = %s"
        mycursor.execute(sql,(ID,))
        myresult = mycursor.fetchall()
        return myresult
    except:
        msg.showerror('Error', 'Database is not responding')

def riprogramma_guida(ID, data, ora):
    try:
        if isinstance(ora, str):
            ora = int(ora)
        ora_formattata = f"{ora:02d}:00:00" 
        sql="UPDATE `scuolaguida`.`guide` SET `data` = %s, `ora` = %s WHERE (`idGuida` = %s);"
        mycursor.execute(sql, (data, ora_formattata, ID))
        mydb.commit()
    except:
        msg.showerror('Error', 'Operation failed')

def get_guide_rimaste(ID):
    try:
        sql = "SELECT (p.tipo - count(g.idGuida)) mancanti from scuolaguida.pacchetti p left join scuolaguida.guide g on (p.idPacchetto = g.idPacchetto) where p.idPacchetto in (SELECT distinct P.idPacchetto FROM scuolaGuida.iscrizioni I JOIN scuolaguida.acquisti A ON (I.idStudente = A.idStudente) JOIN scuolaguida.pacchetti P ON (P.idAcquisto = A.idAcquisto) WHERE finito = 0 AND I.idStudente = %s) group by p.tipo;"
        mycursor.execute(sql,(ID,))
        myresult = mycursor.fetchall()
        return myresult
    except:
        msg.showerror('Error', 'Database is not responding')

def get_id_pacchetto(ID):
    try:
        sql = "SELECT idPacchetto FROM scuolaguida.pacchetti P JOIN scuolaguida.acquisti A ON P.idAcquisto = A.idAcquisto WHERE idStudente=%s AND finito = 0;"
        mycursor.execute(sql,(ID,))
        myresult = mycursor.fetchall()
        return myresult
    except:
        msg.showerror('Error', 'Database is not responding')

def add_guida(data, ora, idPacchetto, targa, CFist):
    try:
        if isinstance(ora, str):
            ora = int(ora)
        ora_formattata = f"{ora:02d}:00:00"
        sql = "INSERT INTO `scuolaguida`.`guide` (`data`, `ora`, `idPacchetto`, `targa`, `CFIstruttorePratico`) VALUES (%s, %s, %s, %s, %s);"
        mycursor.execute(sql, (data, ora_formattata, idPacchetto, targa, CFist))
        mydb.commit()
        chiudi_pacchetto()
    except:
        msg.showerror('Error', 'Operation failed')

def get_pacchetto_da_chiudere():
    try:
        sql = "SELECT idPacchetto FROM (SELECT DISTINCT P.idPacchetto, P.tipo, COUNT(idGuida) guide FROM scuolaguida.pacchetti P JOIN scuolaguida.guide G ON (P.idPacchetto = G.idPacchetto) WHERE P.finito = 0 GROUP BY P.idPacchetto) mancanti WHERE guide = tipo"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
    except:
        msg.showerror('Error', 'Database is not responding')

def chiudi_pacchetto():
    try:
        id = get_pacchetto_da_chiudere()
        if id:
            id = id[0][0]
            sql = "UPDATE `scuolaguida`.`pacchetti` SET `finito` = '1' WHERE (`IdPacchetto` = %s);"
            mycursor.execute(sql, (id,))
            mydb.commit()
    except:
        msg.showerror('Error', 'Operation failed')

def get_iscrizione_scadua_teorico():
    try:
        sql = "SELECT idStudente FROM (SELECT I.idStudente, COUNT(idEsame) numeroEsami FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamiteorici E ON (I.idStudente = E.idStudente) WHERE E.esito = 0 GROUP BY I.idStudente) bocciato WHERE numeroEsami = 2"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
    except:
        msg.showerror('Error', 'Database is not responding')

def chiudi_iscirzione_teorico():
    try:
        id = get_iscrizione_scadua_teorico()
        if id:
            id = id[0][0]
            sql = "UPDATE `scuolaguida`.`iscrizioni` SET `chiusa` = '1' WHERE (`idStudente` = %s);"
            mycursor.execute(sql, (id,))
            mydb.commit()
    except Exception as ex:
        msg.showerror('Error', ex)

def get_iscrizione_scadua_pratico():
    try:
        sql = "SELECT idStudente FROM (SELECT I.idStudente, COUNT(idEsame) numeroEsami FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamipratici E ON (I.idStudente = E.idStudente) WHERE E.esito = 0 GROUP BY I.idStudente) bocciato WHERE numeroEsami = 3"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
    except:
        msg.showerror('Error', 'Database is not responding')

def get_presa_patente():
    try:
        sql = "SELECT I.idStudente FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamipratici E ON (I.idStudente = E.idStudente) WHERE I.chiusa = 0 AND E.esito = 1"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
    except:
        msg.showerror('Error', 'Database is not responding')

def chiudi_iscirzione_pratico():
    try:
        id = get_iscrizione_scadua_pratico()
        if id:
            id = id[0][0]
            sql = "UPDATE `scuolaguida`.`iscrizioni` SET `chiusa` = '1' WHERE (`idStudente` = %s);"
            mycursor.execute(sql, (id,))
            mydb.commit()
        id = get_presa_patente()
        if id:
            id = id[0][0]
            sql = "UPDATE `scuolaguida`.`iscrizioni` SET `chiusa` = '1' WHERE (`idStudente` = %s);"
            mycursor.execute(sql, (id,))
            mydb.commit()
    except Exception as ex:
        msg.showerror('Error', ex)

def add_lezione(data, ora, CFist):
    try:
        if isinstance(ora, str):
            ora = int(ora)
        ora_formattata = f"{ora:02d}:00:00"
        sql = "INSERT INTO `scuolaguida`.`lezioni` (`data`, `ora`, `CFIstruttoreTeorico`) VALUES (%s, %s, %s);"
        mycursor.execute(sql, (data, ora_formattata, CFist))
        mydb.commit()
    except Exception as ex:
        msg.showerror('Error', 'Operation failed')

def get_istruttori_teorici():
    try:
        sql = "SELECT CFIstruttoreTeorico, nome, cognome FROM scuolaguida.istruttoriteorici;"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
    except:
        msg.showerror('Error', 'Database is not responding')