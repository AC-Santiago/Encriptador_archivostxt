from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
import sys


class Pagina_inicial(QMainWindow):
    def __init__(self):
        super(Pagina_inicial, self).__init__()
        loadUi("src/Archivos.ui/Pagina_inicial.ui", self)
        self.setWindowTitle("Pagina inicial")

        self.Abrir_menu.clicked.connect(self.abrir_menu)

    def abrir_menu(self):
        # Obtener el ancho del frame (Frame_menu)
        ancho = self.Frame_menu.width()
        if ancho == 0:
            # Cambiar el tamaño del ancho al frame (Frame_menu) a 200
            self.Frame_menu.setMaximumWidth(200)
        else:
            # Cambiar el tamaño del ancho al frame (Frame_menu) a 0
            self.Frame_menu.setMaximumWidth(0)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Pagina_inicial()
    window.show()
    sys.exit(app.exec_())
