# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox


class Ui_RegDialog(QDialog):
    def __init__(self):
        super().__init__()
        super().__init__(self, Qt.Dialog)
        self.setupUi()
        self.login = None
        self.password = None
        self.closeFlag = False

    def setupUi(self):
        self.setObjectName("RegDialog")
        self.resize(400, 231)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.LoginEdit = QtWidgets.QLineEdit(self)
        self.LoginEdit.setObjectName("LoginEdit")
        self.gridLayout.addWidget(self.LoginEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.PasswordFirst = QtWidgets.QLineEdit(self)
        self.PasswordFirst.setObjectName("PasswordFirst")
        self.gridLayout.addWidget(self.PasswordFirst, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.PasswordSecond = QtWidgets.QLineEdit(self)
        self.PasswordSecond.setObjectName("PasswordSecond")
        self.gridLayout.addWidget(self.PasswordSecond, 2, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.onAccept)
        self.buttonBox.rejected.connect(self.onReject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, RegDialog):
        _translate = QtCore.QCoreApplication.translate
        RegDialog.setWindowTitle(_translate("RegDialog", "Регистрация"))
        self.label.setText(_translate("RegDialog", "<html><head/><body><p align=\"center\">Логин</p></body></html>"))
        self.label_2.setText(_translate("RegDialog", "<html><head/><body><p align=\"center\">Пароль</p></body></html>"))
        self.label_3.setText(_translate("RegDialog", "<html><head/><body><p align=\"center\">Еще раз пароль</p></body></html>"))

    def onAccept(self):
        if self.PasswordFirst.text() == self.PasswordSecond.text():
            self.login = self.LoginEdit.text() if self.LoginEdit.text() != '' else None
            self.password = self.PasswordFirst.text() if self.PasswordFirst.text() != '' else None

            if self.login is None or self.password is None or \
                    len(self.login.split(' ')) > 1 or len(self.password.split(' ')) > 1:
                QMessageBox.information(self, 'Ошибка', 'Пробелы или пустные строки не допустимы')
                self.login = None
                self.password = None
                return

            self.accept()
        else:
            QMessageBox.information(self, 'Ошибка', 'Пароли не совпадают')

    def onReject(self):
        self.login = None
        self.password = None
        self.closeFlag = True
        self.reject()
