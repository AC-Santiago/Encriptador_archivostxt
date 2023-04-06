#Interface de inicio de sesion generada con la libreria PyQt5
#

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from Ventana_principal import Ui_Ventana_principal
import sys

class Ui_Inicio_sesion(object):
    def setupUi(self, Inicio_sesion):
        Inicio_sesion.setObjectName("Inicio_sesion")
        Inicio_sesion.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(Inicio_sesion)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 100, 241, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 160, 241, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 220, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        Inicio_sesion.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Inicio_sesion)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        Inicio_sesion.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Inicio_sesion)
        self.statusbar.setObjectName("statusbar")
        Inicio_sesion.setStatusBar(self.statusbar)

        self.retranslateUi(Inicio_sesion)
        QtCore.QMetaObject.connectSlotsByName(Inicio_sesion)

    def retranslateUi(self, Inicio_sesion):
        _translate = QtCore.QCoreApplication.translate
        Inicio_sesion.setWindowTitle(_translate("Inicio_sesion", "Inicio de sesion"))
        self.label.setText(_translate("Inicio_sesion", "Bienvenido a Encriptador de archivos txt"))
        self.label_2.setText(_translate("Inicio_sesion", "Usuario:"))
        self.label_3.setText(_translate("Inicio_sesion", "Contraseña:"))
        self.pushButton.setText(_translate("Inicio_sesion", "Iniciar sesion"))
        self.pushButton.clicked.connect(self.iniciar_sesion)

    def iniciar_sesion(self):
        usuario = self.lineEdit.text()
        contrasena = self.lineEdit_2.text()
        if usuario == "admin" and contrasena == "admin":
            self.ventana_principal()
        else:
            self.mensaje_error()

    def ventana_principal(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Ventana_principal()
        self.ui.setupUi(self.window)
        self.window.show()

    def mensaje_error(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Usuario o contraseña incorrectos")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit.setFocus()



