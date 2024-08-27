import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import connection

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setGeometry(50, 100, 1800, 700)
    win.setWindowTitle("Prova")

    lbl = QtWidgets.QLabel(win)
    lbl.setText('Nome')
    lbl.move(50, 50)

    txt = QtWidgets.QLineEdit(win)
    txt.move(50, 100)

    btn = QtWidgets.QPushButton(win)
    btn.setText('Bottone')
    btn.move(50, 200)
    btn.clicked.connect(open_second_window)  # funzione per bottone

    win.show()
    sys.exit(app.exec_())

def open_second_window():
    veicoli = QMainWindow()
    veicoli.setGeometry(50, 100, 400, 300)
    veicoli.setWindowTitle("Veicoli")

    # Chiama la funzione per ottenere i dati
    veicoli_list = connection.veicoli()

    # Crea un QListWidget e aggiungi gli elementi della lista
    list_widget = QtWidgets.QListWidget(veicoli)
    list_widget.addItems(veicoli_list)
    list_widget.setGeometry(10, 10, 380, 280)

    veicoli.show()

    # Mantieni una referenza alla finestra per evitare che venga eliminata
    open_second_window.veicoli_window = veicoli

window()
