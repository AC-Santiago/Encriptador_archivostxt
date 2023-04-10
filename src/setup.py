from Archivos_ui_en_py.Inicio_sesion import Inicio_sesion
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Inicio_sesion()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
