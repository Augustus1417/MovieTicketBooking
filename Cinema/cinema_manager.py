from Cinema.cinema import Cinema
import json, string, random
from datetime import datetime

class CinemaManager:
    def __init__(self, movie_list):
        with open("Cinema\cinemas.json", "r") as file:
                data = json.load(file)
                self.cinemas = { # hashmap created from the json file
                    reference_id: Cinema(
                        cinema_name=cinema_data["cinema_name"],
                        schedule=datetime.strptime(cinema_data["schedule"], "%Y-%m-%d %H:%M"),
                        showing=cinema_data["showing"],
                        seats=cinema_data["seats"]
                    )
                    for reference_id, cinema_data in data.items()
                }
        self.movie_list = movie_list

    def view_all_cinemas(self):
        for reference_id, cinema in self.cinemas.items():
            print(f"\nReference ID: {reference_id}\n{cinema}\n")

    def add_new_cinema(self, cinema_name, schedule, showing):
        for movie in self.movie_list.movie_list.values():
            if movie.title == showing:
                schedule_str = schedule.strftime("%Y-%m-%d %H:%M")
                reference_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
                seats = [["O" for _ in range(10)] for _ in range(5)]
                new_cinema = Cinema(cinema_name, schedule_str ,showing, seats)
                self.cinemas[reference_id] = new_cinema
                self.update_json()
                return f"{cinema_name} added successfully."
        return f"{showing} is not in the system."

    def delete_cinema(self, reference_id):
        try: 
            del self.cinemas[reference_id]
            self.update_json()
            return f"{reference_id} has been deleted from the system."
        except: return f"{reference_id} was not found in the system, try again."
    
    def assign_seat(self, reference_id, column, row):
        if self.cinemas[reference_id].seats[column][row] == "O":
            self.cinemas[reference_id].seats[column][row] = "X"
            self.update_json()
            return "Seat assigned successfully."
        else: return False
    
    def remove_seat(self, reference_id, column, row):
        if self.cinemas[reference_id].seats[column][row] == "X":
            self.cinemas[reference_id].seats[column][row] = "O"
            self.update_json()
            return "Seat removed successfully."
        else: return False
    
    def view_available_cinema(self, movie_id):
        try: movie_title = self.movie_list.movie_list[movie_id].title
        except: print(f"{movie_id} was not found in the system, try again")
        for reference_id, cinema in self.cinemas.items():
            if cinema.showing == movie_title:
                print(f"\nReference ID: {reference_id}\n{cinema.cinema_name}\n{cinema.schedule}")
    
    def validate_id(self,cinema_id):
        for reference_id in self.cinemas.keys():
            if reference_id == cinema_id: return True
        return False
    
    def show_seats(self, cinema_id):
        return f"\t{self.cinemas[cinema_id].get_seat()}"

    def update_json(self):
        data_to_save = {
            reference_id: {
                "cinema_name": cinema.cinema_name,
                "schedule": cinema.schedule.strftime("%Y-%m-%d %H:%M")
                if isinstance(cinema.schedule, datetime)
                else cinema.schedule,
                "showing": cinema.showing,
                "seats": cinema.seats
            }
            for reference_id, cinema in self.cinemas.items()
        }
        with open("Cinema\cinemas.json", "w") as file:
            json.dump(data_to_save, file, indent=4)