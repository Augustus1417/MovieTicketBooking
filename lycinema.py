from Ticket.ticket_manager import TicketManager
from Movie.movie_manager import MovieManager
from Cinema.cinema_manager import CinemaManager
movieManager = MovieManager()
cinemaManager = CinemaManager(movieManager)
ticketManager = TicketManager(movieManager,cinemaManager)

print("Welcome to Lycinema")
ticketManager.add_new_ticket("MOO4A","0BA7N", 4, 6)
