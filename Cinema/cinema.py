import string, random
class Cinema:
    def __init__(self, cinema_name, schedule, showing):
        self.reference_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        self.cinema_name = cinema_name
        self.schedule = schedule
        self.showing = showing
        self.seats = [[0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0]]

    def __str__(self):
        seats_str = "\n".join([" ".join(map(str, row)) for row in self.seats])
        return f"\nID: {self.reference_id}\nSchedule:{self.schedule}\nCinema Name: {self.cinema_name}\nShowing : {self.showing}\nSeats:\n{seats_str}"