import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E03_Ahorcado.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Area de los Signals
        self.palabra = ""
        self.letras_usadas = set()
        self.errores = 0
        self.orden_partes = [self.pierna1, self.pierna2, self.brazo1, self.brazo2, self.cuerpo, self.cabeza]
        self.btn_jugar.clicked.connect(self.iniciar_juego)
        self.btn_probar.clicked.connect(self.probar_letra)

    #Area de Slots
    def iniciar_juego(self):
        palabra = self.txt_palabra.text().strip().lower()
        if not palabra:
            self.msj("Por favor, ingresa una palabra para jugar.")
            return

        self.palabra = palabra
        self.letras_usadas = set()
        self.errores = 0

        self.txt_palabra.setText("")
        for parte in self.orden_partes:
            parte.setStyleSheet("")
        self.actualizar_lbl_palabra()

    def actualizar_lbl_palabra(self):
        resultado = ""
        for letra in self.palabra:
            if letra in self.letras_usadas:
                resultado += letra + " "
            else:
                resultado += "_ "
        self.lbl_palabra.setText(resultado.strip())

    def probar_letra(self):
        if not self.palabra:
            self.msj("Inicia el juego ingresando una palabra.")
            return
        letra = self.txt_letra.text().strip().lower()
        self.txt_letra.setText("")
        if len(letra) != 1 or not letra.isalpha():
            self.msj("Ingresa solo una letra.")
            return
        if letra in self.letras_usadas:
            self.msj("Ya probaste esa letra.")
            return
        self.letras_usadas.add(letra)
        if letra in self.palabra:
            self.actualizar_lbl_palabra()
            if all(l in self.letras_usadas for l in self.palabra):
                self.msj("¡Ganaste!")
                self.reiniciar_juego()
        else:
            if self.errores < len(self.orden_partes):
                parte = self.orden_partes[self.errores]
                parte.setStyleSheet("background-color: red;")
                self.errores += 1
                if self.errores == len(self.orden_partes):
                    self.msj("¡Perdiste! La palabra era: " + self.palabra)
                    self.reiniciar_juego()

    def reiniciar_juego(self):
        self.palabra = ""
        self.letras_usadas = set()
        self.errores = 0
        self.lbl_palabra.setText("")
        self.txt_palabra.setText("")
        self.txt_letra.setText("")
        for parte in self.orden_partes:
            parte.setStyleSheet("")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
