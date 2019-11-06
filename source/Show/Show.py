class Show:
    def __init__(self, show_id: int, name: str, year: int, timing: int, description: str = None, score: float = None):
        self.show_id = show_id
        self.name = name
        self.year = year
        self.timing = timing
        self.description = description
        self.score = score
        self.my_score = None
        self.watching = False

    def to_html(self):
        return f'<p><b>{self.name}</b></p>' \
               f'<p>Год выпуска {self.year} Хронометраж {self.timing}мин</p>' \
               f'<p>Оценка {self.score} Моя оценка {self.my_score}</p>' \
               f'<p>{self.description}</p>'
