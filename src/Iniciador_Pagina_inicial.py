from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QLineEdit,
    QGraphicsBlurEffect,
    QGraphicsOpacityEffect,
)
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt

from Funciones.Manipulador_json import manage_json
import sys


class Pagina_inicial(QMainWindow):
    def __init__(self):
        super(Pagina_inicial, self).__init__()
        loadUi("src/Archivos.ui/Pagina_inicial.ui", self)
        self.setWindowTitle("Pagina inicial")

        # pone el nombre del usuario en el label (Label_nombreU) este nombre traido del json
        Nombre_Use = manage_json("src/Archivos.json/Nombre_usuario.json")
        Name = Nombre_Use.get_element("Nombre")
        self.Label_nombreU.setText(Name)

        self.Abrir_menu.clicked.connect(self.abrir_menu)
        self.Button_cerrar_sesion.clicked.connect(self.Cerrar_sesion)

    def abrir_menu(self):
        # Obtener el ancho del frame (Frame_menu)
        ancho = self.Frame_menu.width()
        # da un efecto de opacidad
        blur_effect = QGraphicsBlurEffect()
        effect = QGraphicsBlurEffect()
        effect.setBlurRadius(0)
        if ancho == 0:
            # Cambiar el tamaño del ancho al frame (Frame_menu) a 200
            self.Frame_menu.setMaximumWidth(200)

            # mientras se hace el cambio de tamaño hacer una animacion de 500 milisegundos
            self.animation = QtCore.QPropertyAnimation(self.Frame_menu, b"maximumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(0)
            self.animation.setEndValue(200)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

            self.Abrir_menu.setIcon(QIcon("src/imagenes/left-arrow.png"))

            # efecto de opacidad
            blur_effect.setBlurRadius(10)
            self.Frame_principal.setGraphicsEffect(blur_effect)

        else:
            # Cambiar el tamaño del ancho al frame (Frame_menu) a 0 y mientras se hace el cambio de tamaño hacer una animacion de 500 milisegundos
            self.Frame_menu.setMaximumWidth(0)

            self.animation = QtCore.QPropertyAnimation(self.Frame_menu, b"maximumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(200)
            self.animation.setEndValue(0)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

            # efecto de opacidad
            blur_effect.setBlurRadius(0)
            self.Frame_principal.setGraphicsEffect(blur_effect)

            # cambiar el icono del boton "Abrir_menu" a un icono de flecha hacia la derecha
            self.Abrir_menu.setIcon(QIcon("src/imagenes/Flecha_derecha.png"))

    def Nombre_User(self):
        self.Label_nombreU.setText("Hola")

    def Cerrar_sesion(self):
        from Funciones.Manipulador_json import manage_json
        from Iniciador_inicio_sesion import Inicio_sesion

        ruta = "src/Archivos.json/Nombre_usuario.json"
        manage = manage_json(ruta)

        # * Quita el esatdo de 1 a 0 para que no se mantenga la sesion
        if manage.get_element("estado_check") == 1:
            manage.edit_element("estado_check", 1, 0)

        self.inicio_sesion = Inicio_sesion()
        self.inicio_sesion.show()
        self.close()
