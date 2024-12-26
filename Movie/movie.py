class Movie():
    def __init__(self, title, duration, genre) -> None:
        self.title = title
        self.duration = duration
        self.genre = genre
    
    def __str__(self): return f"\tTitle: {self.title}\n\tGenre: {self.duration}\n\tDuration: {self.genre}" 