# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WelcomeDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog


class Ui_WelcomeDialog(QDialog):
    def __init__(self):
        super().__init__()
        super().__init__(self, Qt.Dialog)
        self.newUser = False
        self.setupUi()

    def setupUi(self):
        self.setObjectName("WelcomeDialog")
        self.resize(381, 125)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.Reg = QtWidgets.QPushButton(self)
        self.Reg.setObjectName("Reg")
        self.gridLayout.addWidget(self.Reg, 2, 0, 1, 1)
        self.SignIn = QtWidgets.QPushButton(self)
        self.SignIn.setObjectName("SignIn")
        self.gridLayout.addWidget(self.SignIn, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.Reg.clicked.connect(self.regClick)
        self.SignIn.clicked.connect(self.signInClick)

    def retranslateUi(self, WelcomeDialog):
        _translate = QtCore.QCoreApplication.translate
        WelcomeDialog.setWindowTitle(_translate("WelcomeDialog", "Добро пожаловать"))
        self.Reg.setText(_translate("WelcomeDialog", "Зарегистрироваться"))
        self.SignIn.setText(_translate("WelcomeDialog", "Войти"))
        self.label.setText(_translate("WelcomeDialog", "<html><head/><body><p align=\"center\">Добро пожаловать</p></body></html>"))

    def signInClick(self):
        self.newUser = False
        self.accept()

    def regClick(self):
        self.newUser = True
        self.accept()
