import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E02_MetrosAPies.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Etiquetas
        #label_a
        #label_b
        #btn_convertir
        #txt_a
        #txt_b
        #btn_estado
        # Área de los Signals
        self.btn_convertir.clicked.connect(self.convertir)
        self.btn_estado.clicked.connect(self.intercambiar)
        self.estado = True  # True: Metros a Pies, False: Pies a Metros
    # Área de los Slots
    def convertir(self):
        try:
            if self.estado:
                # Metros a Pies
                a = float(self.txt_a.text())
                b = a * 3.28084
                self.txt_b.setText(str(b))
            else:
                # Pies a Metros
                b = float(self.txt_b.text())
                a = b / 3.28084
                self.txt_a.setText(str(a))
        except ValueError:
            self.msj("Error en los datos")

    def intercambiar(self):
        c = self.label_a.text()
        self.label_a.setText(self.label_b.text())
        self.label_b.setText(c)
        self.estado = not self.estado
        self.txt_a.setText("")
        self.txt_b.setText("")
        self.txt_a.setFocus()

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
