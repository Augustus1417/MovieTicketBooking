from Cinema.cinema import Cinema
import json, string, random
from datetime import datetime

class CinemaManager:
    def __init__(self, movie_list):
        with open("Cinema\cinemas.json", "r") as file:
                data = json.load(file)
                self.cinemas = {
                    reference_id: Cinema(
                        cinema_name=cinema_data["cinema_name"],
                        schedule=datetime.strptime(cinema_data["schedule"], "%Y-%m-%d %H:%M"),
                        showing=cinema_data["showing"]
                    )
                    for reference_id, cinema_data in data.items()
                }
        self.movie_list = movie_list

    def view_all_cinemas(self):
        for cinema in self.cinemas.values():
            print(cinema, "\n")

    def add_new_cinema(self, cinema_name, schedule, showing):
        for movie in self.movie_list.movie_list.values():
            if movie.title == showing:
                schedule_str = schedule.strftime("%Y-%m-%d %H:%M")
                reference_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
                new_cinema = Cinema(cinema_name, schedule_str ,showing)
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
    
    def assign_seat(self, reference_id, row, column):
        self.cinemas[reference_id].seats[row][column] = 1
        self.update_json()
        return f"Seat assigned successfully."

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