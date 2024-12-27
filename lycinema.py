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
    os.system('cls')
    print("""
   _____            _   _             
  / ____|          | | (_)            
 | (___   ___  __ _| |_ _ _ __   __ _ 
  \___ \ / _ \/ _` | __| | '_ \ / _` |
  ____) |  __/ (_| | |_| | | | | (_| |
 |_____/ \___|\__,_|\__|_|_| |_|\__, |
                                 __/ |
                                |___/ """)
    line(40)
    print("\n",cinemaManager.show_seats(cinema_id))
    row = int(input("\nInput desired row (vertical: 1-5): "))
    column = int(input("Input desired column (horizontal: 1-10): "))
    if cinemaManager.assign_seat(cinema_id,row-1,column-1) == False:
        print("Seat is occupied")
    else: 
        os.system("cls")
        return row, column

def book_cinema(movie_id):
    os.system('cls')
    print("""
   _____ _                            
  / ____(_)                           
 | |     _ _ __   ___ _ __ ___   __ _ 
 | |    | | '_ \ / _ \ '_ ` _ \ / _` |
 | |____| | | | |  __/ | | | | | (_| |
  \_____|_|_| |_|\___|_| |_| |_|\__,_| """)
    line(50)
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

def view_your_ticket():
    os.system("cls")
    print("""
 __      ___                 _______ _      _        _   
 \ \    / (_)               |__   __(_)    | |      | |  
  \ \  / / _  _____      __    | |   _  ___| | _____| |_ 
   \ \/ / | |/ _ \ \ /\ / /    | |  | |/ __| |/ / _ \ __|
    \  /  | |  __/\ V  V /     | |  | | (__|   <  __/ |_ 
     \/   |_|\___| \_/\_/      |_|  |_|\___|_|\_\___|\__| """)
    line(65)
    ticket_id = input("Enter ticket ID: ")
    ticketManager.view_ticket(ticket_id)

def cancel_ticket():
    os.system('cls')
    print("""
   _____                     _   _______ _      _        _   
  / ____|                   | | |__   __(_)    | |      | |  
 | |     __ _ _ __   ___ ___| |    | |   _  ___| | _____| |_ 
 | |    / _` | '_ \ / __/ _ \ |    | |  | |/ __| |/ / _ \ __|
 | |___| (_| | | | | (_|  __/ |    | |  | | (__|   <  __/ |_ 
  \_____\__,_|_| |_|\___\___|_|    |_|  |_|\___|_|\_\___|\__| """)
    line(60)
    ticket_id = input("Enter ticket ID: ")
    print(ticketManager.cancel_ticket(ticket_id))

def view_movies(): movieManager.view_all_movies()

def main():
    os.system('cls')
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
            case "2": view_your_ticket()
            case "3": cancel_ticket()
            case "4": view_movies()
            case "5": break
            case _: print("1-5 only, try again.")

main()