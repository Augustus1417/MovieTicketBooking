from Ticket.ticket import Ticket
import string, random, json

class TicketManager:
    def __init__(self, movie_manager,cinema_manager):
        self.movie_manager = movie_manager
        self.cinema_manager = cinema_manager
        self.ticket_list = {}
    
    def view_all_tickets(self):
        for ticket in self.ticket_list.values():
            print(ticket,"\n")

    def add_new_ticket(self, movie_id, cinema_id, seat_row, seat_column):
        reference_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        new_ticket = Ticket(reference_id,
                            self.movie_manager.movie_list[movie_id],
                            self.cinema_manager.cinemas[cinema_id],
                            seat_row,seat_column)
        self.ticket_list[reference_id] = new_ticket
        print(new_ticket)