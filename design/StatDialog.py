# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StatDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt


class Ui_StatDialog(QDialog):
    def __init__(self, model):
        super().__init__()
        self.setupUi()
        self.tableView.setModel(model)

    def setupUi(self):
        self.setObjectName("StatDialog")
        self.resize(450, 334)
        self.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtWidgets.QTableView(self)
        self.tableView.setMinimumSize(QtCore.QSize(0, 200))
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, StatDialog):
        _translate = QtCore.QCoreApplication.translate
        StatDialog.setWindowTitle(_translate("StatDialog", "Статистика"))
        self.label.setText(_translate("StatDialog", "<html><head/><body><p>В таблице приводтся список сериалов, общее время просмотра и</p><p align=\"justify\"> общаяя сумма количества просмтренных эпизодов по всему серивису</p></body></html>"))
