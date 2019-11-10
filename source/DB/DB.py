import hashlib
from typing import List

from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QMessageBox

from source.Show import Show, Episode


def get_hash(password: str):
    return hashlib.new('sha256', bytes(password, 'utf8')).hexdigest()


class DB:
    def __init__(self):
        self.__db = QSqlDatabase('QODBC3')
        self.__db.setDatabaseName('DRIVER={SQL Server};SERVER=localhost;DATABASE=SerialTracker;Port=1433')

        self.__id = 0
        self.__only_watching = False

        if not self.__db.open():
            QMessageBox.critical(self, 'Ошибка', 'Не удалось подключиться к базе данных')
            exit(-2)

        self.__query = QSqlQuery(self.__db)

    def authorise(self, login: str, password: str) -> bool:
        self.__query.exec(f"exec Authorise '{login}', '{get_hash(password)}'")
        self.__query.next()
        if self.__query.value(0):
            self.__id = self.__query.value(0)
        return self.__id > 0

    def get_shows(self) -> List[Show]:
        shows = []
        if not self.__only_watching:
            self.__query.exec('exec GetAllShows')
        else:
            self.__query.exec(f'exec GetWatchingShow {self.__id}')
        while self.__query.next():
            shows.append(Show(show_id=self.__query.value(0), name=self.__query.value(1),
                              year=self.__query.value(2), timing=self.__query.value(3),
                              description=self.__query.value(4), score=self.__query.value(5)))
        for show in shows:
            show.my_score = self.get_score(show)
        return shows

    def get_episodes(self, show_id: int) -> List[Episode]:
        episodes = []
        self.__query.exec(f'exec GetEpisodes {show_id}')
        while self.__query.next():
            episodes.append(Episode(
                episode_id=self.__query.value(0), season=self.__query.value(1),
                series=self.__query.value(2), score=self.__query.value(3),
                name=self.__query.value(4), description=self.__query.value(5)
            ))
        for episode in episodes:
            episode.my_score = self.get_score(episode)
        return episodes

    def set_only_watching(self, status: bool):
        self.__only_watching = status

    def episode_score_update(self, data: Episode, value: int):
        self.__query.exec(f'exec ReviewEpisode {self.__id}, {data.id}, {value}')

    def show_score_update(self, data: Show, value: int):
        self.__query.exec(f'exec ReviewShow {self.__id}, {data.show_id}, {value}')

    def get_score(self, data):
        if type(data) is Episode:
            self.__query.exec(f'exec GetWatcherEpisodeScore {self.__id}, {data.id}')
        else:
            self.__query.exec(f'exec GetWatcherShowScore {self.__id}, {data.show_id}')
        self.__query.next()

        return self.__query.value(0) if self.__query.value(0) else None

    def mark_status_show(self, data: Show):
        self.__query.exec(f'exec MarkShow {self.__id}, {data.show_id}')

    def get_watching_show(self):
        watching_show_id = []
        self.__query.exec(f'exec GetWatchingShow {self.__id}')
        while self.__query.next():
            watching_show_id.append(self.__query.value(0))
        return watching_show_id

    def get_watched_episode(self):
        watched_episode_id = []
        self.__query.exec(f'exec GetWatchedEpisode {self.__id}')
        while self.__query.next():
            watched_episode_id.append(self.__query.value(1))
        return watched_episode_id

    def get_stat_model(self):
        model = QSqlTableModel(None, self.__db)
        model.setTable('Stat')
        model.select()
        return model

    def registration(self, login: str, password: str):
        self.__query.exec(f"exec Registration '{login}', '{get_hash(password)}'")
        self.__query.next()
        return self.__query.value(0) == 1

    def mark_status_episode(self, data):
        self.__query.exec(f'exec MarkEpisode {self.__id}, {data.id}')

    def is_logged(self):
        return self.__id > 0
