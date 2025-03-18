import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E05_Gato.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Area de los Signals
        self.turno = "X"
        self.celdas = [
            self.txt_1, self.txt_2, self.txt_3,
            self.txt_4, self.txt_5, self.txt_6,
            self.txt_7, self.txt_8, self.txt_9
        ]
        for celda in self.celdas:
            celda.textChanged.connect(lambda _, c=celda: self.marcar_celda(c))
        self.btn_reiniciar.clicked.connect(self.reiniciar_juego)

    # Area de los Slots
    def marcar_celda(self, celda):
        if celda.text() in ["X", "O"]:
            celda.setEnabled(False)
            if self.verificar_ganador():
                return
            self.turno = "O" if self.turno == "X" else "X"

    def verificar_ganador(self):
        combinaciones = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in combinaciones:
            if self.celdas[a].text() and self.celdas[a].text() == self.celdas[b].text() == self.celdas[c].text():
                self.msj(f"¡{self.celdas[a].text()} gana!")
                self.bloquear_tablero()
                return True

        if all(celda.text() in ["X", "O"] for celda in self.celdas):
            self.msj("¡Empate!")
            return True

        return False

    def bloquear_tablero(self):
        for celda in self.celdas:
            celda.setEnabled(False)

    def reiniciar_juego(self):
        for celda in self.celdas:
            celda.setText("")
            celda.setEnabled(True)
        self.turno = "X"

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
