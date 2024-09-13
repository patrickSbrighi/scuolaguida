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
        sql = "SELECT stu.idStudente, stu.nome, stu.cognome FROM (SELECT I.idStudente, S.nome, S.cognome FROM scuolaguida.iscrizioni I JOIN scuolaguida.studenti S ON (I.CFStudente = S.CFStudente) JOIN scuolaguida.tipologiepatenti T ON (T.idTipologia = I.idTipologia) WHERE S.dataNascita < DATE_SUB(DATE_SUB(DATE_SUB(CURDATE(), INTERVAL T.eta YEAR), INTERVAL 1 MONTH), INTERVAL 1 DAY) AND I.chiusa = 0 AND I.idStudente NOT IN (SELECT I.idStudente FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamiteorici E ON (I.idStudente = E.idStudente) WHERE E.esito = 1) ORDER BY I.dataInizio) stu JOIN scuolaguida.acquisti A ON stu.idStudente = A.idStudente JOIN scuolaguida.esamiteorici ES ON A.idAcquisto = ES.idAcquisto WHERE ES.esito IS NULL OR ES.esito = ''"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
     except:
        msg.showerror('Error', 'Database is not responding')

def add_esame_teorico(ID, errori, data):
    try:
        maxError = 3
        sql="UPDATE `scuolaguida`.`esamiteorici` SET `data` = %s, `esito` = %s, `numErrori` = %s WHERE `idEsame` = (SELECT `idEsame` FROM `scuolaguida`.`esamiteorici` WHERE `idStudente` = %s AND `esito` IS NULL OR `esito` = '');"
        if int(errori) <= maxError:
            mycursor.execute(sql, (data, 1, errori, ID))
            mydb.commit()
        else:
            mycursor.execute(sql, (data, 0, errori, ID))
            mydb.commit()
    except Exception as ex:
        print(ex)
        msg.showerror('Error', ex)

def get_studenti_pratici():
     try: 
        sql = "SELECT sub.idStudente, S.nome, S.cognome FROM (SELECT I.idStudente, I.CFStudente, COUNT(G.idGuida) guide FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamiteorici E ON (I.idStudente = E.idStudente) JOIN scuolaguida.acquisti A ON (A.idStudente = I.idStudente) JOIN scuolaguida.pacchetti P ON (A.idAcquisto = P.idAcquisto) JOIN scuolaguida.guide G ON (G.IdPacchetto = P.IdPacchetto) WHERE I.chiusa = '0' AND I.idStudente IN (SELECT I.idStudente FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamiteorici E ON (I.idStudente = E.idStudente) WHERE E.esito = '1') AND I.idStudente NOT IN (SELECT I.idStudente FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamipratici E ON (I.idStudente = E.idStudente) WHERE E.esito = '1') GROUP BY I.idStudente HAVING guide >= 12 ORDER BY I.dataInizio) sub JOIN scuolaguida.studenti S ON sub.CFStudente = S.CFStudente JOIN scuolaguida.acquisti A ON sub.idStudente = A.idStudente JOIN scuolaguida.esamipratici ES ON A.idAcquisto = ES.idAcquisto WHERE ES.esito IS NULL OR ES.esito = ''"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
     except:
        msg.showerror('Error', 'Database is not responding')

def add_esame_pratico(ID, esito, data, esaminatore):
    try:
        sql="UPDATE `scuolaguida`.`esamipratici` SET `data` = %s, `esito` = %s, `CFEsaminatore` = %s WHERE (`idStudente` = %s);"
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

def get_guide_future():
    try: 
        sql = "SELECT idGuida, data, ora, targa, CFIstruttorePratico FROM scuolaguida.guide WHERE data >= CURDATE()"
        mycursor.execute(sql)
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
        else:
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
        print(ex)
        msg.showerror('Error', 'Operation failed')

def get_istruttori_teorici():
    try:
        sql = "SELECT CFIstruttoreTeorico, nome, cognome FROM scuolaguida.istruttoriteorici;"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
    except:
        msg.showerror('Error', 'Database is not responding')