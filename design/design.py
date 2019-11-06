# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 672)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setObjectName("treeView")
        self.gridLayout.addWidget(self.treeView, 0, 0, 1, 1)
        self.onlyWatched = QtWidgets.QCheckBox(self.centralwidget)
        self.onlyWatched.setObjectName("onlyWatched")
        self.gridLayout.addWidget(self.onlyWatched, 2, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 1, 1, 1)
        self.scoreScroll = QtWidgets.QSlider(self.centralwidget)
        self.scoreScroll.setMaximum(5)
        self.scoreScroll.setTracking(True)
        self.scoreScroll.setOrientation(QtCore.Qt.Horizontal)
        self.scoreScroll.setInvertedAppearance(False)
        self.scoreScroll.setInvertedControls(False)
        self.scoreScroll.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.scoreScroll.setTickInterval(1)
        self.scoreScroll.setObjectName("scoreScroll")
        self.gridLayout.addWidget(self.scoreScroll, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.watchedUnwatchedButton = QtWidgets.QPushButton(self.centralwidget)
        self.watchedUnwatchedButton.setObjectName("watchedUnwatchedButton")
        self.horizontalLayout.addWidget(self.watchedUnwatchedButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 906, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionStat = QtWidgets.QAction(MainWindow)
        self.actionStat.setObjectName("actionStat")
        self.menu.addAction(self.actionUpdate)
        self.menu.addAction(self.actionStat)
        self.menu.addSeparator()
        self.menu.addAction(self.actionClose)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.actionClose.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Трекер просмотра сериалов"))
        self.onlyWatched.setText(_translate("MainWindow", "Только просматриваемые   сериалы"))
        self.label.setText(_translate("MainWindow", "Оценка"))
        self.watchedUnwatchedButton.setText(_translate("MainWindow", "Отметить как \"Смотрю/Не смотрю\""))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.actionUpdate.setText(_translate("MainWindow", "Обновить"))
        self.actionClose.setText(_translate("MainWindow", "Выход"))
        self.actionStat.setText(_translate("MainWindow", "Посмотреть статистику"))
        self.actionStat.setShortcut(_translate("MainWindow", "Ctrl+S"))
