import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P05_EjemploSumarDosNumeros-V2.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de los Signals
        self.btn_sumar.clicked.connect(self.sumar)

    #Area de los Slots
    def sumar(self):
        try:
            a = float(self.txt_a.text())
            b = float(self.txt_b.text())
            r = a + b
            #self.msj("La suma es: " + str(r))
            self.txt_resultado.setText(str(r))
        except Exception as error:
            print(error)

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
