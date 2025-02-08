import time as t
import sys
from PyQt5 import uic, QtWidgets,QtCore
qtCreatorFile = "P10_SegundoPlanoTimer.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de los Signals
        self.btn_temporizar.clicked.connect(self.temporizar2doPlano)
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.controlSegundoPlano)
        self.valorN = -1
    #Area de los Slots
    def controlSegundoPlano(self):
        self.txt_temporizador.setText(str(self.valorN))
        self.valorN -= 1
        if self.valorN == -1:
            self.segundoPlano.stop()

    def temporizar2doPlano(self):
        self.valorN = int(self.txt_temporizador.text())
        self.segundoPlano.start(500)
    def temporizar(self):
        valor = self.txt_temporizador.text()
        for i in range(valor,0,-1):
            self.txt_temporizador.setText(str(i))
            print(i)
            t.sleep(0.1)

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
