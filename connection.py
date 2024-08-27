import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="scuolaguida"
)

mycursor = mydb.cursor()
def veicoli():
    formula = "SELECT * FROM scuolaguida.veicoli"
    mycursor.execute(formula)
    myresult = mycursor.fetchall()

    # Supponiamo che tu voglia visualizzare le prime due colonne
    return [f"{item[0]} - {item[1]}" for item in myresult]

