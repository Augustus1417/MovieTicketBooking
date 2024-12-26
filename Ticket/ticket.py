import string, random

class Ticket:
    def __init__(self, movie_details, seating):
        self.reference_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        self.movie_details = movie_details
        self.seating = seating
    
    def __str__(self):
        return f"Reference ID: {self.reference_id}\nMovie:\n{self.movie_details}\nSeating: {self.seating}"