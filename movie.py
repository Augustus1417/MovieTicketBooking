class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
    
    def __str__(self):
        return f"Movie Title: {self.title}\nYear: {self.year}\nGenre: {self.genre}"