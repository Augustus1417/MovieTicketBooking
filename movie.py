class Movie():
    def __init__(self, title, duration, genre) -> None:
        self.title = title
        self.duration = duration
        self.genre = genre
    
    def __str__(self) -> str: return f"Title: {self.title}\nGenre: {self.duration}\nDuration: {self.genre}" 