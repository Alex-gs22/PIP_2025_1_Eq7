import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P09_sliderImagenes_Manual.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.selectorImagen.setMinimum(1)
        self.selectorImagen.setMaximum(3)
        self.selectorImagen.setSingleStep(1)
        self.selectorImagen.setValue(1) ##valr inicial
        self.selectorImagen.valueChanged.connect(self.cambiaValor)

        self.diccionarioDatos = {
            1: (":/ejercicios/john cena.png",["John Cenna", "32 Años","1.90"]),
            2: (":/ejercicios/malenia.jpeg", ["Malenia Espada de Mikela", "28 Años", "2.10"]),
            3: (":/ejercicios/3ueemqhb14k81.png", ["Walter White", "55 Años", "1.72"])
        }
        self.indice = 1
        self.obtenerDatos()

    # Área de los Slots
    def obtenerDatos(self):
        nombre = self.diccionarioDatos[self.indice][1][0]
        edad = self.diccionarioDatos[self.indice][1][1]
        estatura = self.diccionarioDatos[self.indice][1][2]
        self.txt_nombre.setText(nombre)
        self.txt_edad.setText(edad)
        self.txt_estatura.setText(estatura)
        self.imagen.setPixmap(QtGui.QPixmap(self.diccionarioDatos[self.indice][0]))
        
    def cambiaValor(self):
        self.indice = self.selectorImagen.value()
        self.obtenerDatos()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

