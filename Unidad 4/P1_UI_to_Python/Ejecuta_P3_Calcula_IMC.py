import sys
from PyQt5 import uic, QtWidgets
import P3_vPython_Calcula_IMC as interfaz

#Ejercicios... Parte 3: Escoger 10 ejercicios
class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de los Signals
        self.btn_calcular.clicked.connect(self.calcular)

    #Area de los Slots
    def calcular(self):
        pass

    def limpiar(self):
        pass

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())
