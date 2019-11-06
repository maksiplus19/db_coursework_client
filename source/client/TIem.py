from typing import List

from source.Show import Episode, Show


class TItem:
    def __init__(self, show: Show = None, parent=None, episode=None):
        self.__show = show
        self.__episode: Episode = episode
        self.__parent: TItem = parent
        self.__children: List[TItem] = []

    def appendChild(self, child):
        child.__parent = self
        self.__children.append(child)

    def child(self, row: int):
        if row < 0 or row >= len(self.__children):
            return None
        return self.__children[row]

    def childCount(self) -> int:
        return len(self.__children)

    def row(self) -> int:
        if self.__parent is not None:
            return self.__parent.__children.index(self)
        return 0

    def columnCount(self) -> int:
        return 1

    def data(self) -> str:
        if self.__show is not None:
            if self.__show.watching:
                return f'{self.__show.name} (Смотрю)'
            else:
                return self.__show.name
        elif self.__episode is not None:
            if self.__episode.watched:
                return f'{self.__episode.season}x{self.__episode.series} {self.__episode.name} (Просмотрено)'
            else:
                return f'{self.__episode.season}x{self.__episode.series} {self.__episode.name}'
        else:
            return 'Сериалы'

    def parentItem(self):
        return self.__parent

    def innerData(self):
        return self.__episode or self.__show
    #
    # def setParent(self, parent):
    #     self.__parent = parent
