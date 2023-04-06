from Inicio_sesion import Ui_Inicio_sesion
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Inicio_sesion = QtWidgets.QMainWindow()
    ui = Ui_Inicio_sesion()
    ui.setupUi(Inicio_sesion)
    Inicio_sesion.show()
    sys.exit(app.exec_())
