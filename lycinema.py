from Ticket.ticket_manager import TicketManager
from Movie.movie_manager import MovieManager
from Cinema.cinema_manager import CinemaManager
import os

movieManager = MovieManager()
cinemaManager = CinemaManager(movieManager)
ticketManager = TicketManager(movieManager,cinemaManager)

def line(length): 
    for _ in range(length): print("-", end="")
    print()

def choose_seat(cinema_id):
    print("\n",cinemaManager.show_seats(cinema_id))
    row = int(input("\nInput desired row (vertical: 1-5): "))
    column = int(input("Input desired column (horizontal: 1-10): "))
    if cinemaManager.assign_seat(cinema_id,row-1,column-1) == False:
        print("Seat is occupied")
    else: return row, column

def book_cinema(movie_id):
    cinemaManager.view_available_cinema(movie_id)
    cinema_id = input("\nInput the ID of the cinema you want: ")
    if cinemaManager.validate_id(cinema_id):
        return cinema_id
    else: 
        print("Invalid cinema ID")
        return

def book_ticket():
    os.system("cls")
    print("""
______             _      _____ _      _        _   
| ___ \           | |    |_   _(_)    | |      | |  
| |_/ / ___   ___ | | __   | |  _  ___| | _____| |_ 
| ___ \/ _ \ / _ \| |/ /   | | | |/ __| |/ / _ \ __|
| |_/ / (_) | (_) |   <    | | | | (__|   <  __/ |_ 
\____/ \___/ \___/|_|\_\   \_/ |_|\___|_|\_\___|\__| """)
    line(50)
    movieManager.view_all_movies()
    movie_id = input("Input the ID of the movie you want: ")
    if movieManager.validate_id(movie_id):
        line(50)
        cinema_id = book_cinema(movie_id)
    else: print("Invalid movie ID")
    row, column = choose_seat(cinema_id)
    ticketManager.add_new_ticket(movie_id,cinema_id,row,column)
    os.system("cls")

def view_your_ticket(ticket_id): pass

def main():
    print("""
 _                _                            
| |              (_)                           
| |    _   _  ___ _ _ __   ___ _ __ ___   __ _ 
| |   | | | |/ __| | '_ \ / _ \ '_ ` _ \ / _` |
| |___| |_| | (__| | | | |  __/ | | | | | (_| |
\_____/\__, |\___|_|_| |_|\___|_| |_| |_|\__,_|
        __/ |                                  
       |___/                                   """)
    while True:
        line(50)
        choice = input("1. Book a ticket\n"
                    "2. View your ticket\n"
                    "3. Cancel ticket\n"
                    "4. View Available Movies\n"
                    "5. Exit\n"
                    "Your choice (1-5): ")
        match choice:
            case "1": book_ticket()
            case "2": pass
            case "3": pass
            case "4": pass
            case "5": break
            case _: print("1-5 only, try again.")

main()