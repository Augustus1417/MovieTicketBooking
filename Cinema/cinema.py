class Cinema:
    def __init__(self,cinema_name, schedule, showing, seats):
        self.cinema_name = cinema_name
        self.schedule = schedule
        self.showing = showing
        self.seats = seats

    def get_cinema_name(self): return self.cinema_name
    def get_schedule(self): return self.schedule
    def get_seat(self): return "\n\t".join([" ".join(map(str, row)) for row in self.seats])

    def __str__(self):
        seats_str = "\n\t".join([" ".join(map(str, row)) for row in self.seats])
        return f"Schedule: {self.schedule}\nCinema Name: {self.cinema_name}\nShowing : {self.showing}\nSeats:\n\t{seats_str}"