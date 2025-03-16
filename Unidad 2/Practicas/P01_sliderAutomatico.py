import time as t
import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore

qtCreatorFile = "P01_sliderAutomatico.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.selectorImagen.setMinimum(1)
        self.selectorImagen.setMaximum(10)
        self.selectorImagen.setSingleStep(1)
        self.selectorImagen.setValue(1)  ##valr inicial
        self.selectorImagen.valueChanged.connect(self.cambiaValor)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.cambiar_imagen_automaticamente)
        self.intervalo = 2000
        self.timer.start(self.intervalo)

        self.valorN = -1  # Ya no se usa para el timer automático
        self.diccionarioDatos = {
            1: (":/ejercicios/john cena.png", ["John Cenna"]),
            2: (":/ejercicios/malenia.jpeg", ["Malenia Espada de Mikela"]),
            3: (":/ejercicios/3ueemqhb14k81.png", ["Walter White"]),
            4: (":/ejercicios/8s85l9yb14k81.png", ["Walter White"]),
            5: (":/ejercicios/besttvseries.jpeg", ["Walter White"]),
            6: (":/ejercicios/btw.jpeg", ["Walter White"]),
            7: (":/logos/favicon.jpeg", ["Walter White"]),
            8: (":/ejercicios/v1.jpeg", ["Walter White"]),
            9: (":/ejercicios/v2.jpeg", ["Walter White"]),
            10: (":/ejercicios/v3.jpeg", ["Walter White"])
        }
        self.indice = 1
        self.mostrar_imagen()

    # Área de los Slot
    def cambiar_imagen_automaticamente(self):
        self.indice = (self.indice % 10) + 1
        self.mostrar_imagen()
        self.selectorImagen.setValue((self.indice %10)+ 1)

    def mostrar_imagen(self):
        nombre = self.diccionarioDatos[self.indice][1][0]
        self.txt_nombre.setText(nombre)
        self.imagen.setPixmap(QtGui.QPixmap(self.diccionarioDatos[self.indice][0]))

    def cambiaValor(self):
        self.indice = self.selectorImagen.value()
        self.mostrar_imagen()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())