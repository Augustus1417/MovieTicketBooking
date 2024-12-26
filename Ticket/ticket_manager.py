from Ticket.ticket import Ticket
import json

class TicketManager:
    def __init__(self):
        self.ticket_list = {}
    
    def view_all_tickets(self):
        for ticket in self.ticket_list.values():
            print(ticket,"\n")

    def add_new_ticket(self):
        new