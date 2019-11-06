import sys

from PyQt5.QtCore import QModelIndex

from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableView, QMessageBox

from source.DB import DB
from source.Show import Episode
from source.client import SerialsModel, TItem


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.tables = {
            'Сериалы': 'Show',
            'Просмотренные серии': 'WatcherEpisode',
            'Просматриваемые сериалы': 'WatcherShow'
        }
        super().__init__()
        self.setupUi(self)
        self.db = DB()
        self.data = None

        welcome = Ui_WelcomeDialog()
        if welcome.exec_() == 0:
            exit(0)
        else:
            if welcome.newUser is False:
                dialog = Ui_AuthDialog()
                if dialog.exec_() == 0:
                    exit(0)

                while dialog.l is None or dialog.p is None or not self.db.authorise(dialog.l, dialog.p):
                    QMessageBox.critical(self, 'Ошибка', 'Не удалось авторизоваться')
                    if dialog.exec_() == 0:
                        exit(0)
            else:
                dialog = Ui_RegDialog()
                if dialog.exec_() == 0 and dialog.closeFlag:
                    exit(0)

                while dialog.login is None or dialog.password is None or \
                        not self.db.registration(dialog.login, dialog.password):
                    QMessageBox.critical(self, 'Ошибка', 'Не удалось зарегистрироваться')
                    if dialog.exec_() == 0 and dialog.closeFlag:
                        exit(0)

        self.model = SerialsModel(self.db)

        self.treeView.setEditTriggers(QTableView.NoEditTriggers)
        self.treeView.setModel(self.model)
        self.treeView.clicked.connect(self.textBrowserUpdate)
        self.treeView.collapsed.connect(self.textBrowserUpdate)
        self.treeView.expanded.connect(self.textBrowserUpdate)
        self.treeView.entered.connect(self.textBrowserUpdate)
        self.treeView.activated.connect(self.textBrowserUpdate)
        self.treeView.update()

        self.onlyWatched.clicked.connect(self.wathingSwitch)

        self.scoreScroll.valueChanged.connect(self.scoreChange)

        self.watchedUnwatchedButton.clicked.connect(self.markStatus)

        self.actionUpdate.triggered.connect(self.model.update)
        self.actionStat.triggered.connect(self.showStat)

    def wathingSwitch(self, status: bool):
        self.db.set_only_watching(status)
        self.model.update()

    def textBrowserUpdate(self, index: QModelIndex):
        if index is None:
            self.textBrowser.setText('')
            return
        self.data: TItem = index.internalPointer()
        self.scoreScroll.setValue(0 if self.data.innerData().my_score is None else self.data.innerData().my_score)
        if type(self.data.innerData()) is Episode:
            self.textBrowser.setText(self.data.innerData().to_html(index.parent().internalPointer().innerData()))
        else:
            self.textBrowser.setText(self.data.innerData().to_html())

    def scoreChange(self, value: int):
        if self.data is None or self.data.innerData() is None:
            self.scoreScroll.setValue(0)
            return
        if value == 0:
            value = None
        self.data.innerData().my_score = value
        if type(self.data.innerData()) is Episode:
            self.db.episode_score_update(self.data.innerData(), value)
            self.textBrowser.setText(self.data.innerData().to_html(self.data.parentItem().innerData()))
        else:
            self.db.show_score_update(self.data.innerData(), value)
            self.textBrowser.setText(self.data.innerData().to_html())

    def markStatus(self):
        if self.treeView.currentIndex() is None or not self.treeView.currentIndex().isValid():
            return
        data = self.treeView.currentIndex().internalPointer().innerData()
        if type(data) is Episode:
            self.db.mark_status_episode(data)
        else:
            self.db.mark_status_show(data)
        self.model.update()

    def showStat(self):
        dialog = Ui_StatDialog(self.db.get_stat_model())
        dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()
