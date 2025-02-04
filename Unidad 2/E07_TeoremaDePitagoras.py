import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E07_TeoremaDePitagoras.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de los Signals
        self.btn_calcular.clicked.connect(self.calcular)
        self.btn_limpiar.clicked.connect(self.limpiar)

    #Area de los Slots
    def calcular(self):
        try:
            a = float(self.txt_cateto_a.text())
            b = float(self.txt_cateto_b.text())
            c = (a**2 + b**2)**0.5
            self.lbl_hipotenusa.setText("{:.2f}".format(c))
        except:
            self.msj("Error en los datos ingresados")

    def limpiar(self):
        self.txt_cateto_a.setText("")
        self.txt_cateto_b.setText("")
        self.lbl_hipotenusa.setText("")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
