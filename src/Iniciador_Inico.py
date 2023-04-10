from PyQt5.QtWidgets import QMainWindow, QApplication,QLineEdit
from PyQt5.QtGui import QGuiApplication,QIcon
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi 
from PyQt5.QtCore import Qt
import sys

class Inicio_sesion(QMainWindow):
    def __init__(self):
        super(Inicio_sesion, self).__init__()
        loadUi('src/Archivos.ui/Inicio_sesion.ui', self)
        self.setWindowTitle("Inicio de sesión")

        #Funcion que se ejecuta al presionar el boton de iniciar sesion
        self.Button_inicio_sesion.clicked.connect(self.datos_user)
        self.Button_registrarse.clicked.connect(self.registrarse)

    #Funcion que obtiene los datos del usuario
    def datos_user(self):
        self.user = self.Text_usuario.text()
        self.password = self.Text_password.text()
        print(self.user)
        print(self.password)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Inicio_sesion()
    window.show()
    sys.exit(app.exec_())

