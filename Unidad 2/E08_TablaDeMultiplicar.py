import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E08_TablaDeMultiplicar.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de los Signals
        self.btn_generar.clicked.connect(self.generar)
        self.btn_limpiar.clicked.connect(self.limpiar)

    #Area de los Slots
    def generar(self):
        try:
            n = float(self.txt_num.text())
            self.lbl_1.setText(f"     {n}     =     {n*1:.2f}")
            self.lbl_2.setText(f"     {n}     =     {n*2:.2f}")
            self.lbl_3.setText(f"     {n}     =     {n*3:.2f}")
            self.lbl_4.setText(f"     {n}     =     {n*4:.2f}")
            self.lbl_5.setText(f"     {n}     =     {n*5:.2f}")
            self.lbl_6.setText(f"     {n}     =     {n*6:.2f}")
            self.lbl_7.setText(f"     {n}     =     {n*7:.2f}")
            self.lbl_8.setText(f"     {n}     =     {n*8:.2f}")
            self.lbl_9.setText(f"     {n}     =     {n*9:.2f}")
            self.lbl_10.setText(f"     {n}     =     {n*10:.2f}")
        except:
            self.msj("Error en los datos ingresados")
    def limpiar(self):
        self.txt_num.setText("")
        self.lbl_1.setText("          =")
        self.lbl_2.setText("          =")
        self.lbl_3.setText("          =")
        self.lbl_4.setText("          =")
        self.lbl_5.setText("          =")
        self.lbl_6.setText("          =")
        self.lbl_7.setText("          =")
        self.lbl_8.setText("          =")
        self.lbl_9.setText("          =")
        self.lbl_10.setText("          =")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
