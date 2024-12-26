import string, random

class Ticket:
    def __init__(self, movie_details,schedule, cinema, seating):
        self.reference_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        self.movie_details = movie_details
        self.schedule = schedule
        self.cinema = cinema
        self.seating = seating
    
    def __str__(self):
        return f"Reference ID: {self.reference_id}\nMovie Details:\n{self.movie_details}\nSchedule: {self.schedule}\nCinema: {self.cinema}\nSeating: {self.seating}"