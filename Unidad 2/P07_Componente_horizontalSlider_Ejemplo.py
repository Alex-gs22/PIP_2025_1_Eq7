import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P07_Componente_horizontalSlider_Ejemplo.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de los Signals
        self.horizontalSlider.setMinimum(-50)
        self.horizontalSlider.setMaximum(50)
        self.horizontalSlider.setSingleStep(5)
        self.horizontalSlider.setValue(-50)
        self.horizontalSlider.valueChanged.connect(self.cambiaValor)
        self.txt_valor.setText("-50")

    #Area de los Slots
    def cambiaValor(self):
        value = self.horizontalSlider.value()
        self.txt_valor.setText(str(value))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
