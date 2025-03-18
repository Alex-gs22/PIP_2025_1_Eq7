import sys
import random
from functools import partial
from PyQt5 import uic, QtWidgets, QtGui, QtCore

qtCreatorFile = "E06_Memorizar_Patrones.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Área de Signals y Configuraciones Iniciales
        self.botones = [
            self.btn_1, self.btn_2, self.btn_3, self.btn_4,
            self.btn_5, self.btn_6, self.btn_7, self.btn_8,
        ]
        self.labels = [
            self.lbl_1, self.lbl_2, self.lbl_3, self.lbl_4,
            self.lbl_5, self.lbl_6, self.lbl_7, self.lbl_8,
        ]
        self.imagenes = [
            "/home/falexone/Documentos/PIP/PIP_2025_1_Eq7/Archivos/john cena.png",
            "/home/falexone/Documentos/PIP/PIP_2025_1_Eq7/Archivos/malenia.jpeg",
            "/home/falexone/Documentos/PIP/PIP_2025_1_Eq7/Archivos/3ueemqhb14k81.png",
            "/home/falexone/Documentos/PIP/PIP_2025_1_Eq7/Archivos/8s85l9yb14k81.png",
            "/home/falexone/Documentos/PIP/PIP_2025_1_Eq7/Archivos/besttvseries.jpeg",
            "/home/falexone/Documentos/PIP/PIP_2025_1_Eq7/Archivos/v1.jpeg",
            "/home/falexone/Documentos/PIP/PIP_2025_1_Eq7/Archivos/v2.jpeg",
            "/home/falexone/Documentos/PIP/PIP_2025_1_Eq7/Archivos/v3.jpeg"
        ]
        self.ruta_dorso = "/home/falexone/Documentos/PIP/PIP_2025_1_Eq7/Archivos/favicon.jpeg"

        self.patron = []
        self.patron_usuario = []
        self.current_score = 0
        self.high_score = 0
        self.indice_mostrado = 0

        self.btn_jugar.clicked.connect(self.iniciar_juego)
        for i, btn in enumerate(self.botones):
            btn.clicked.connect(partial(self.procesar_click, i))

    # Área de Slots
    def iniciar_juego(self):
        self.patron = []
        self.patron_usuario = []
        self.current_score = 0
        self.actualizar_puntuacion()
        self.siguiente_ronda()

    def siguiente_ronda(self):
        nuevo = random.randint(0, len(self.botones) - 1)
        self.patron.append(nuevo)
        self.patron_usuario = []
        self.current_score = len(self.patron)
        self.actualizar_puntuacion()
        for btn in self.botones:
            btn.setEnabled(False)
        self.indice_mostrado = 0
        self.mostrar_patron()

    def mostrar_patron(self):
        if self.indice_mostrado < len(self.patron):
            idx = self.patron[self.indice_mostrado]
            self.labels[idx].setPixmap(QtGui.QPixmap(self.imagenes[idx]))
            QtCore.QTimer.singleShot(800, partial(self.ocultar_label, idx))
            self.indice_mostrado += 1
            QtCore.QTimer.singleShot(1200, self.mostrar_patron)
        else:
            for btn in self.botones:
                btn.setEnabled(True)

    def ocultar_label(self, i):
        self.labels[i].setPixmap(QtGui.QPixmap(self.ruta_dorso))

    def procesar_click(self, idx):
        self.labels[idx].setPixmap(QtGui.QPixmap(self.imagenes[idx]))
        QtCore.QTimer.singleShot(500, partial(self.ocultar_label, idx))
        if idx == self.patron[len(self.patron_usuario)]:
            self.patron_usuario.append(idx)
            if len(self.patron_usuario) == len(self.patron):
                QtCore.QTimer.singleShot(1000, self.siguiente_ronda)
        else:
            self.derrota()

    def derrota(self):
        if self.current_score - 1 > self.high_score:
            self.high_score = self.current_score - 1
        self.actualizar_puntuacion()
        self.msj(f"Perdiste! Puntuación: {self.current_score - 1}")
        for btn in self.botones:
            btn.setEnabled(False)

    def actualizar_puntuacion(self):
        self.lbl_puntuacion.setText(f"Puntuacion: {self.current_score - 1}")
        self.lbl_record.setText(f"Record: {self.high_score}")

    def msj(self, texto):
        QtWidgets.QMessageBox.information(self, "Mensaje", texto)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())