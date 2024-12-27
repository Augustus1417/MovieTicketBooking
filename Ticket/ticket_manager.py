from Ticket.ticket import Ticket
import string, random, json

class TicketManager:
    def __init__(self, movie_manager,cinema_manager):
        self.movie_manager = movie_manager
        self.cinema_manager = cinema_manager
        with open("Ticket\\tickets.json","r") as file:
            data = json.load(file)
            self.ticket_list = {
                reference_id: Ticket(ticket_data["reference_id"],ticket_data["movie_details"],ticket_data["cinema"],ticket_data["seat_row"],ticket_data["seat_column"], )
                for reference_id, ticket_data in data.items()
            }
    
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
        self.update_json()
        print(new_ticket)
        print("!TAKE NOTE OF THE REFERENCE ID!")

    def update_json(self):
        data_to_save = {
            reference_id: {"reference_id": ticket.reference_id, "movie_details": ticket.movie_details, "cinema": ticket.cinema, "seat_row": ticket.seat_row, "seat_column" : ticket.seat_column}
            for reference_id, ticket in self.ticket_list.items()
        }
        with open("Ticket\\tickets.json", "w") as file:
            json.dump(data_to_save, file, indent=4)