from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt

import sys

from Iniciador_Pagina_inicial import Pagina_inicial
from Iniciador_Registro import Registro
from Funciones.Conexion_DB_Mongo import Verificar_user
from Funciones.Manipulador_json import manage_json


class Inicio_sesion(QMainWindow):
    def __init__(self):
        super(Inicio_sesion, self).__init__()
        loadUi("src/Archivos.ui/Inicio_sesion.ui", self)
        self.setWindowTitle("Inicio de sesión")

        # Funcion que se ejecuta al presionar el boton de iniciar sesion
        self.Button_inicio_sesion.clicked.connect(self.datos_user)
        self.Button_registrarse.clicked.connect(self.registrarse)

    # Funcion que obtiene los datos del usuario
    def datos_user(self):
        self.user = self.Text_usuario.text()
        self.password = self.Text_password.text()
        if Verificar_user(self.user, self.password) == True:
            self.mantener_sesion()
            self.name_user()

            # abre la ventana de la pagina inicial
            self.pagina_inicial = Pagina_inicial()
            self.pagina_inicial.show()
            self.close()
        else:
            # genera una ventana emergente que dice que los datos son incorrectos
            self.mensaje = QtWidgets.QMessageBox()
            self.mensaje.setWindowTitle("Error")
            self.mensaje.setText("Usuario o contraseña incorrectos")
            self.mensaje.setIcon(QtWidgets.QMessageBox.Critical)
            self.mensaje.exec_()

    # Funcion que abre la ventana de registro y cierra la ventana de inicio de sesion
    def registrarse(self):
        self.registro = Registro()
        self.registro.show()
        self.close()

    # Funcion que cambia el valor del estado_check de json para que se mantenga la sesion
    def mantener_sesion(self):
        ruta = "src/Archivos.json/Nombre_usuario.json"
        prueba = manage_json(ruta)
        if self.Mantener_sesion.isChecked() == 1:
            prueba.edit_element("estado_check", 0, 1)
        else:
            if prueba.get_element("estado_check") == 1:
                prueba.edit_element("estado_check", 1, 0)
            else:
                prueba.edit_element("estado_check", 0, 0)

    # Funcion que le cambie el nombre de json al usaurio ingresado
    def name_user(self):
        ruta = "src/Archivos.json/Nombre_usuario.json"
        prueba = manage_json(ruta)
        resultado = prueba.get_element("Nombre")
        prueba.edit_element("Nombre", resultado, self.user)
