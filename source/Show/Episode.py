class Episode:
    def __init__(self, episode_id: int, season: int, series: int, score: float = None, name: str = None,
                 description: str = None):
        self.id = episode_id
        self.season = season
        self.series = series
        self.score = score
        self.name = name
        self.description = description
        self.my_score = None
        self.watched = False

    def to_html(self, show):
        return f'<p><b>{self.name}</b> ({show.name})</p>' \
               f'<p>{self.season}x{self.series}</p>' \
               f'<p>Оценка {self.score} Моя оценка {self.my_score}</p>' \
               f'<p>{self.description}</p>'
