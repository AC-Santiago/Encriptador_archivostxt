from Iniciador_inicio_sesion import Inicio_sesion
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Inicio_sesion()
    window.show()
    sys.exit(app.exec_())
