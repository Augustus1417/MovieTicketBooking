import string, random

class Ticket:
    def __init__(self, movie_details,schedule, cinema, seating):
        self.reference_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        self.movie_details = movie_details
        self.schedule = schedule
        self.cinema = cinema
        self.seating = seating
    
    def __str__(self):
        ticket_info = [
            f"Reference ID: {self.reference_id}",
            f"Movie Details: {self.movie_details}",
            f"Schedule: {self.schedule}",
            f"Cinema: {self.cinema}",
            f"Seating: {self.seating}"
        ]
        max_length = max(len(line) for line in ticket_info)
        result = "+" + "-" * (max_length + 2) + "+\n"
        for line in ticket_info:
            result += f"| {line.ljust(max_length)} |\n"
        result += "+" + "-" * (max_length + 2) + "+"
        return result
            