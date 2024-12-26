class Ticket:
    def __init__(self, reference_id ,movie_details, cinema, seat_row, seat_column):
        self.reference_id = reference_id
        self.movie_details = movie_details
        self.cinema = cinema
        self.seat_row = seat_row
        self.seat_column = seat_column
    
    def __str__(self):
        movie_summary = f"\nTitle: {self.movie_details.title}\nGenre: {self.movie_details.genre}\nDuration: {self.movie_details.duration}"
        cinema_summary = f"\nSchedule: {self.cinema.schedule}\nCinema Name: {self.cinema.cinema_name}"
        
        ticket_info = [
            "Ticket Details:",
            f"Reference ID: {self.reference_id}",
            movie_summary,
            cinema_summary,
            f"Seat: {self.seat_row}-{self.seat_column}",
        ]

        ticket_lines = [line for section in ticket_info for line in section.split("\n")]
        max_length = max(len(line) for line in ticket_lines)
        
        result = "+" + "-" * (max_length + 2) + "+\n"
        for line in ticket_lines:
            result += f"| {line.ljust(max_length)} |\n"
        result += "+" + "-" * (max_length + 2) + "+"
        return result
                    