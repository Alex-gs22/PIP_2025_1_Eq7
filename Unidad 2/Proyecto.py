import sys
import random
from PyQt5 import uic, QtWidgets, QtGui, QtCore

qtCreatorFile = "Proyecto.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.botones = [
            self.btn_1, self.btn_2, self.btn_3, self.btn_4,
            self.btn_5, self.btn_6, self.btn_7, self.btn_8,
            self.btn_9, self.btn_10, self.btn_11, self.btn_12
        ]
        self.labels = [
            self.lbl_1, self.lbl_2, self.lbl_3, self.lbl_4,
            self.lbl_5, self.lbl_6, self.lbl_7, self.lbl_8,
            self.lbl_9, self.lbl_10, self.lbl_11, self.lbl_12
        ]
        # Verifica bien las rutas, la del cuarto elemento estaba mal
        self.imagenes = [
            "/home/falexone/Documentos/PIP/PIP_2025_1_Eq7/Archivos/john cena.png",
            "/home/falexone/Documentos/PIP/PIP_2025_1_Eq7/Archivos/malenia.jpeg",
            "/home/falexone/Documentos/PIP/PIP_2025_1_Eq7/Archivos/3ueemqhb14k81.png",
            "/home/falexone/Documentos/PIP/PIP_2025_1_Eq7/Archivos/8s85l9yb14k81.png",  # Corregida la ruta
            "/home/falexone/Documentos/PIP/PIP_2025_1_Eq7/Archivos/besttvseries.jpeg",
            "/home/falexone/Documentos/PIP/PIP_2025_1_Eq7/Archivos/v1.jpeg"
        ] * 2
        self.ruta_dorso = "/home/falexone/Documentos/PIP/PIP_2025_1_Eq7/Archivos/favicon.jpeg"
        self.seleccionadas = []
        self.pares_encontrados = 0

        for i, btn in enumerate(self.botones):
            btn.clicked.connect(lambda _, idx=i: self.mostrar_carta(idx))
        self.btn_reiniciar.clicked.connect(self.reiniciar_juego)

        self.reiniciar_juego()

    def barajar_imagenes(self):
        # Realiza un shuffle asegurándose que no queden pares consecutivos
        while True:
            random.shuffle(self.imagenes)
            valido = True
            for i in range(len(self.imagenes) - 1):
                if self.imagenes[i] == self.imagenes[i + 1]:
                    valido = False
                    break
            if valido:
                break

    def reiniciar_juego(self):
        self.barajar_imagenes()
        self.seleccionadas = []
        self.pares_encontrados = 0
        # Se muestran todas las imágenes por 15 segundos
        for i, label in enumerate(self.labels):
            label.setPixmap(QtGui.QPixmap(self.imagenes[i]))
            label.setStyleSheet("")
        for btn in self.botones:
            btn.setEnabled(False)
            btn.setStyleSheet("")
        QtCore.QTimer.singleShot(15000, self.ocultar_todas)

    def ocultar_todas(self):
        for label in self.labels:
            label.setPixmap(QtGui.QPixmap(self.ruta_dorso))
        for btn in self.botones:
            btn.setEnabled(True)

    def mostrar_carta(self, idx):
        if len(self.seleccionadas) < 2 and self.labels[idx].pixmap().cacheKey() == QtGui.QPixmap(self.ruta_dorso).cacheKey():
            self.labels[idx].setPixmap(QtGui.QPixmap(self.imagenes[idx]))
            self.seleccionadas.append(idx)
            if len(self.seleccionadas) == 2:
                QtCore.QTimer.singleShot(1000, self.verificar_pareja)

    def verificar_pareja(self):
        idx1, idx2 = self.seleccionadas
        if self.imagenes[idx1] != self.imagenes[idx2]:
            self.labels[idx1].setPixmap(QtGui.QPixmap(self.ruta_dorso))
            self.labels[idx2].setPixmap(QtGui.QPixmap(self.ruta_dorso))
        else:
            self.botones[idx1].setStyleSheet("background-color: green;")
            self.botones[idx2].setStyleSheet("background-color: green;")
            self.botones[idx1].setEnabled(False)
            self.botones[idx2].setEnabled(False)
            self.pares_encontrados += 1
        self.seleccionadas = []
        if self.pares_encontrados == 6:
            self.msj("¡Ganaste!")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
