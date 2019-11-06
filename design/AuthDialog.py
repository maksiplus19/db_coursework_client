# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AuthDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class Ui_AuthDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.setModal(True)
        self.l = None
        self.p = None

    def setupUi(self):
        self.setObjectName("AuthDialog")
        self.resize(335, 182)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.login = QtWidgets.QLineEdit(self)
        self.login.setObjectName("login")
        self.gridLayout.addWidget(self.login, 0, 1, 1, 1)
        self.password = QtWidgets.QLineEdit(self)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)

        self.retranslateUi()
        self.buttonBox.accepted.connect(self.onAccept)
        self.buttonBox.rejected.connect(self.onReject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AuthDialog", "Авторизация"))
        self.label.setText(_translate("AuthDialog", "Логин"))
        self.label_2.setText(_translate("AuthDialog", "Пароль"))

    def onAccept(self):
        self.l = self.login.text() if self.login.text() != '' else None
        self.p = self.password.text() if self.password.text() != '' else None
        self.accept()

    def onReject(self):
        self.l = None
        self.p = None
        self.reject()
