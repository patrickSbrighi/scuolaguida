import mysql.connector
import tkinter.messagebox as msg

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Monta100!",
    database="scuolaguida"
)

mycursor = mydb.cursor()

def delete_iscrizioni_scadute():
    mycursor.execute("SELECT idStudente FROM scuolaguida.iscrizioni WHERE dataInizio <= DATE_SUB(CURDATE(), INTERVAL 1 YEAR) AND chiusa = 'N'")
    data = mycursor.fetchall()

    for id in list(data):
        mycursor.execute("UPDATE scuolaguida.iscrizioni SET chiusa = 'I' WHERE (idStudente = %s)", id)

    mydb.commit()

# func in login
def is_Present(username, password):
    query = "SELECT * FROM admins WHERE username = %s AND password = %s"
    mycursor.execute(query, (username, password))
    result = mycursor.fetchone()
    return result

#func in studenti
def addStudent(CF, name, surname, address, phone, data):
    sql = "INSERT INTO `scuolaguida`.`studenti` (`CFStudente`, `nome`, `cognome`, `indirizzo`, `recapito`, `dataNascita`) VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, (CF, name, surname, address, phone, data))

    mydb.commit()

#func in studenti
def showStudent():
    sql="SELECT CFStudente, nome, cognome, indirizzo, recapito, dataNascita FROM studenti"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return list(data)

#func in iscrizione
def show_Patenti():
    sql="SELECT nome FROM tipologiepatenti"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return data

#func in iscrizione
def show_Pratici():
    sql="SELECT P.CFIstruttorePratico, P.nome, P.cognome, COUNT(idStudente) nStud \
        FROM scuolaguida.iscrizioni I RIGHT JOIN scuolaguida.istruttoripratici P ON (I.CFIstruttorePratico = P.CFIstruttorePratico) \
        GROUP BY CFIstruttorePratico \
        ORDER BY nStud \
        LIMIT 1"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return data

#func in iscrizione
def show_Teorici():
    sql="SELECT CFIstruttoreTeorico, nome, cognome FROM istruttoriteorici"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return data

#func in iscrizione
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

#func in iscrizione
def showIscritti():
    sql = "select i.CFStudente, s.nome, s.cognome, t.nome \
        from scuolaguida.iscrizioni i join scuolaguida.studenti s on (i.CFStudente = s.CFStudente) join scuolaguida.tipologiepatenti t\
        on (i.idTipologia = t.idTipologia)\
        where i.chiusa = 'N';"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return list(data)

#func in iscrizione
def showGuideMancanti(CFStudente):
    sql = "SELECT distinct (p.tipo - count(g.idGuida)) mancanti \
    from scuolaguida.pacchetti p join scuolaguida.guide g on (p.idPacchetto = g.idPacchetto)\
    where p.idPacchetto in\
    (SELECT distinct P.idPacchetto\
    FROM scuolaGuida.iscrizioni I JOIN scuolaguida.acquisti A ON (I.idStudente = A.idStudente) \
    JOIN scuolaguida.pacchetti P ON (P.idAcquisto = A.idAcquisto) \
    JOIN scuolaguida.guide G ON (G.idPacchetto = P.idPacchetto) \
    WHERE finito = 0 AND I.CFStudente = %s)\
    group by p.tipo;"
    mycursor.execute(sql, (CFStudente,) )
    data = mycursor.fetchone()

    if data is None:
        return None
    elif data[0]==0:
        sql = "" #TODO

    return data[0]

def showIscrittiTeorico():
    sql = "select i.CFStudente, s.nome, s.cognome, t.nome \
    from scuolaguida.iscrizioni i join scuolaguida.studenti s on (i.CFStudente = s.CFStudente) \
    join scuolaguida.tipologiepatenti t\
    on (i.idTipologia = t.idTipologia)\
    where i.chiusa = 'N' and (i.idStudente not in (select idStudente\
    from scuolaguida.esamiteorici) or \
    i.idStudente in \
    (select idStudente\
    from scuolaguida.esamiteorici\
    where esito='F' and idStudente not in (\
    select idStudente\
    from scuolaguida.esamiteorici\
    where esito='P' ))) ;"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    return list(data)

def addAcquisto(CFStudente, importo):
    mycursor.execute("select idStudente from scuolaguida.iscrizioni where CFStudente = %s",(CFStudente,) )
    idStudente = mycursor.fetchone()[0]

    mycursor.execute("insert into scuolaguida.acquisti (costoTotale, idStudente) values (%s, %s)", (importo, idStudente))
    mydb.commit()

def addAcquistoTeorico(CFStudente, importo):
    try:
        mycursor.execute("select idStudente from scuolaguida.iscrizioni where CFStudente = %s",(CFStudente,) )
        idStudente = mycursor.fetchone()[0]

        mycursor.execute("insert into scuolaguida.acquisti (costoTotale, idStudente) values (%s, %s)", (importo, idStudente))

        mycursor.execute("SELECT LAST_INSERT_ID()")
        idAcquisto = mycursor.fetchone()[0]

        mycursor.execute("insert into scuolaguida.esamiteorici (costo, idStudente, idAcquisto) values (%s, %s, %s)", ('100',idStudente, idAcquisto ))

        mydb.commit() 
    except mysql.connector.Error as err:
        print(f"Errore: {err}")
        mydb.rollback()

def addAcquistoPratico(CFStudente, importo):
    mycursor.execute("select idStudente from scuolaguida.iscrizioni where CFStudente = %s",(CFStudente,) )
    idStudente = mycursor.fetchone()[0]

    mycursor.execute("insert into scuolaguida.acquisti (costoTotale, idStudente) values (%s, %s)", (importo, idStudente))
    mycursor.fetchall()

    mycursor.execute("SELECT LAST_INSERT_ID()")
    idAcquisto = mycursor.fetchone()[0]

    mycursor.execute("select CFEsaminatore from scuolaguida.esaminatori limit 1")
    CFEsaminatore = mycursor.fetchone()[0]

    mycursor.execute("insert into scuolaguida.esamipratici (costo, idStudente, CFEsaminatore, idAcquisto) values (%s, %s, %s, %s)", ('100', idStudente, CFEsaminatore, idAcquisto))


    mydb.commit() 

def showIscrittiPratico():
    sql="SELECT I.CFStudente, S.nome, S.cognome, COUNT(G.idGuida) guide \
    FROM scuolaguida.iscrizioni I \
    JOIN scuolaguida.esamiteorici E ON (I.idStudente = E.idStudente) \
    JOIN scuolaguida.acquisti A ON (A.idStudente = I.idStudente) \
    JOIN scuolaguida.pacchetti P ON (A.idAcquisto = P.idAcquisto) \
    JOIN scuolaguida.guide G ON (G.IdPacchetto = P.IdPacchetto)\
    JOIN scuolaguida.studenti S ON (S.CFStudente = I.CFStudente)\
    WHERE I.chiusa = 'N' AND I.idStudente IN \
    (SELECT I.idStudente \
    FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamiteorici E ON (I.idStudente = E.idStudente) \
    WHERE E.esito = 'P')\
    AND I.idStudente NOT IN \
    (SELECT I.idStudente \
    FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamipratici E ON (I.idStudente = E.idStudente) \
    WHERE E.esito = 'P')\
    GROUP BY I.idStudente\
    HAVING guide >= 12\
    ORDER BY I.dataInizio"

    mycursor.execute(sql)
    data = mycursor.fetchall()
    return list(data)

def showIscrittiPacchetti():
    sql = "SELECT S.CFStudente, S.nome, S.cognome, greatest(12 - COUNT(G.idGuida), 0) guide_mancanti \
    FROM scuolaguida.iscrizioni I \
    JOIN scuolaguida.esamiteorici E ON (I.idStudente = E.idStudente) \
    JOIN scuolaguida.acquisti A ON (A.idStudente = I.idStudente) \
    JOIN scuolaguida.pacchetti P ON (A.idAcquisto = P.idAcquisto) \
    JOIN scuolaguida.guide G ON (G.IdPacchetto = P.IdPacchetto)\
    JOIN scuolaguida.studenti S ON (S.CFStudente = I.CFStudente)\
    WHERE I.chiusa = 'N' AND I.idStudente IN \
    (SELECT I.idStudente \
    FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamiteorici E ON (I.idStudente = E.idStudente) \
    WHERE E.esito = 'P') \
    AND I.idStudente NOT IN \
    (SELECT I.idStudente \
    FROM scuolaguida.iscrizioni I JOIN scuolaguida.esamipratici E ON (I.idStudente = E.idStudente) \
    WHERE E.esito = 'P')\
    GROUP BY I.idStudente\
    ORDER BY I.dataInizio"

    mycursor.execute(sql)
    data = mycursor.fetchall()
    return list(data)


def addAcquistoPacchetti(CFStudente, tipo):
    mycursor.execute("select idStudente from scuolaguida.iscrizioni where CFStudente = %s",(CFStudente,) )
    idStudente = mycursor.fetchone()[0]

    if tipo=='1':
        importo='50'
    elif tipo=='5':
        importo='200'
    elif tipo=='10':
        importo='400'
    elif tipo=='15':
        importo='650'
    else:
        print("tipo non disponibile")
        return
    

    sql = "insert into scuolaguida.acquisti (costoTotale, idStudente) values (%s, %s)"
    mycursor.execute(sql, (importo, idStudente))

    mycursor.execute("SELECT LAST_INSERT_ID()")
    idAcquisto = mycursor.fetchone()[0]

    mycursor.execute("insert into scuolaguida.pacchetti (prezzo, tipo, finito, idAcquisto) values (%s, %s, %s, %s)", (importo, tipo, 'N', idAcquisto))
    mydb.commit()

