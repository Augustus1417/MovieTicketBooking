class Cinema:
    def __init__(self,cinema_name, schedule, showing):
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
        return f"\nSchedule:{self.schedule}\nCinema Name: {self.cinema_name}\nShowing : {self.showing}\nSeats:\n{seats_str}"