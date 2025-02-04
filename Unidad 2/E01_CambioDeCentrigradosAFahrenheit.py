import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E01_CambioDeCentrigradosAFahrenheit.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de los Signals
        self.btn_convertir.clicked.connect(self.convertir)
        self.btn_limpiar.clicked.connect(self.limpiar)

    #Area de los Slots
    def convertir(self):
        try:
            c = float(self.txt_c.text())
            f = c*9/5 + 32
            self.lbl_f.setText("{:.2f}".format(f))
        except:
            self.msj("Error en los datos ingresados")

    def limpiar(self):
        self.txt_c.setText("")
        self.lbl_f.setText("")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
