import time as t
import sys
from PyQt5 import uic, QtWidgets,QtCore
qtCreatorFile = "P12_RadioButton_GroupBox.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de los Signals
        self.rb_perro.clicked.connect(self.perro)
        self.rb_gato.clicked.connect(self.gato)
        self.rb_hamster.clicked.connect(self.hamster)
        self.rb_negro.clicked.connect(self.negro)
        self.rb_azul.clicked.connect(self.azul)
        self.rb_verde.clicked.connect(self.verde)
    #Area de los Slots
    def perro(self):
        v = self.perro()
        print("perro")
    def gato(self):
        print("gato")
    def hamster(self):
        print("hamster")

    def negro(self):
        print("negro")
    def azul(self):
        print("azul")
    def verde(self):
        print("verde")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
