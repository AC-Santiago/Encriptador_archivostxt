from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import sys

class Ui_Ventana_principal(object):
    def setupUi(self, Ventana_principal):
        Ventana_principal.setObjectName("Ventana_principal")
        Ventana_principal.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(Ventana_principal)
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
        Ventana_principal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ventana_principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        Ventana_principal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ventana_principal)
        self.statusbar.setObjectName("statusbar")
        Ventana_principal.setStatusBar(self.statusbar)

        self.retranslateUi(Ventana_principal)
        QtCore.QMetaObject.connectSlotsByName(Ventana_principal)

    def retranslateUi(self, Ventana_principal):
        _translate = QtCore.QCoreApplication.translate
        Ventana_principal.setWindowTitle(_translate("Ventana_principal", "MainWindow"))
        self.label.setText(_translate("Ventana_principal", "Encriptador de archivos txt"))
        self.label_2.setText(_translate("Ventana_principal", "Archivo:"))
        self.label_3.setText(_translate("Ventana_principal", "Clave:"))
        self.pushButton.setText(_translate("Ventana_principal", "Encriptar"))

        self.pushButton.clicked.connect(self.encriptar)

    def encriptar(self):
        archivo = self.lineEdit.text()
        clave = self.lineEdit_2.text()
        if archivo == "" or clave == "":
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("No se ingresaron todos los datos")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
        else:
            archivo = open(archivo, "r")
            texto = archivo.read()
            archivo.close()
            texto_encriptado = ""
            for i in texto:
                texto_encriptado += chr(ord(i) + int(clave))
            archivo = open(archivo, "w")
            archivo.write(texto_encriptado)
            archivo.close()
            msg = QMessageBox()
            msg.setWindowTitle("Encriptado")
            msg.setText("El archivo se encriptó correctamente")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit.setFocus()
