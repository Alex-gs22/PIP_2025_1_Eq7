import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P07_PromedioNumeros-Load.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de los Signals
        self.btn_cargar.clicked.connect(self.cargar)
        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_guardar.clicked.connect(self.guardar)
        self.calificaciones = []

    #Area de los Slots
    def cargar(self):
        ##Tarea EJ10 --- COMO COMPRUEBO SI EL ARCHIVO EXISTE ? ...
        archivo = open("../Archivos/Calificaciones.csv")
        contenido = archivo.readlines()
        print(contenido)
        datos = [int(x) for x in contenido]
        print(datos)
        #TAREA EJ 11 --- EN LUGAR DE SOBREESCRIBIR, CONCTENAR :D!
        self.calificaciones = datos
        self.promedio()
        #TAREA EJ 12 --- ASEGURARSE DE QUE SOLO SE PUEDA CARGAR HASTA ANTES DE
        #AGREGAR LA PRIMERA CALIFICACION ... ---> ENABLES Y/O CODIGO

    def agregar(self):
        self.calificaciones.append(float(self.txt_calificacion.text()))
        prom = sum(self.calificaciones) / len(self.calificaciones)
        self.txt_promedio.setText(str(prom))

    def guardar(self):
        archivo = open("../Archivos/Calificaciones.txt", "w")
        for cal in self.calificaciones:
            archivo.write(str(cal) + "\n")
        archivo.flush()
        archivo.close()
        self.msj("Calificaciones guardadas")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
