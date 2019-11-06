from typing import Union

from PyQt5.QtCore import QAbstractItemModel, QModelIndex, Qt

from source.DB import DB
from source.client import TItem


class SerialsModel(QAbstractItemModel):
    def __init__(self, db: DB, parent=None, timeout=None):
        super().__init__(parent)
        self.db = db
        self.root = None
        self.watching_shows_id = []
        self.__restore()

    def __restore(self):
        self.beginResetModel()
        self.root = TItem(parent=None)
        shows = sorted(self.db.get_shows(), key=lambda el: el.show_id)
        self.watching_shows_id = self.db.get_watching_show()
        self.watching_episode_id = self.db.get_watched_episode()
        for i, show in enumerate(shows):
            if show.show_id in self.watching_shows_id:
                show.watching = True
            self.root.appendChild(TItem(show=show))
            for episode in self.db.get_episodes(show.show_id):
                if episode.id in self.watching_episode_id:
                    episode.watched = True
                self.root.child(i).appendChild(TItem(episode=episode))
        self.endResetModel()

    def data(self, index: QModelIndex, role=None) -> Union[str, None]:
        if not index.isValid():
            return None

        if role != Qt.DisplayRole:
            return None

        data = index.internalPointer().data()
        return data

    def columnCount(self, parent: QModelIndex = None, *args, **kwargs):
        if parent.isValid():
            return parent.internalPointer().columnCount()
        return self.root.columnCount()

    def rowCount(self, index: QModelIndex = None, *args, **kwargs):
        if index.column() > 0:
            return 0

        if not index.isValid():
            parent_item = self.root
        else:
            parent_item = index.internalPointer()

        return parent_item.childCount()

    def index(self, row, column, parent: QModelIndex = None, *args, **kwargs):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parent_item = self.root
        else:
            parent_item = parent.internalPointer()

        child_item = parent_item.child(row)

        if child_item is None:
            return QModelIndex()
        else:
            return self.createIndex(row, column, child_item)

    def parent(self, index: QModelIndex = None):
        if not index.isValid():
            return QModelIndex()

        child_item: TItem = index.internalPointer()
        parent_item = child_item.parentItem()

        if parent_item == self.root:
            return QModelIndex()

        return self.createIndex(parent_item.row(), 0, parent_item)

    def flags(self, index: QModelIndex):
        if not index.isValid():
            return Qt.NoItemFlags
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def headerData(self, section, orientation, role=None):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return 'Сериалы'
        return None

    def update(self):
        self.__restore()
