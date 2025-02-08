import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E07_Promedio5Numeros.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de las etiquetas
        #btn_promediar
        #txt_1
        #txt_2
        #txt_3
        #txt_4
        #txt_5
        #txt_promedio

        #Area de los Signals
        self.btn_promediar.clicked.connect(self.promediar)

    #Area de los Slots
    def promediar(self):
        try:
            n1 = float(self.txt_1.text())
            n2 = float(self.txt_2.text())
            n3 = float(self.txt_3.text())
            n4 = float(self.txt_4.text())
            n5 = float(self.txt_5.text())
            promedio = (n1 + n2 + n3 + n4 + n5) / 5
            self.txt_promedio.setText(str(promedio))
        except:
            self.msj("Error en los datos")
    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
