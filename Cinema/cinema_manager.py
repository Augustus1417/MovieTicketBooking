from Cinema.cinema import Cinema
import json

class CinemaManager:
    def __init__(self):
        with open("Cinema\cinemas.json", "r") as file:
                data = json.load(file)
                self.cinemas = {
                    cinema_name: Cinema(cinema_data["cinema_name"], cinema_data["showing"])
                    for cinema_name, cinema_data in data.items()
                }

    def view_all_cinemas(self):
        for cinema in self.cinemas.values():
            print(cinema, "\n")

    def add_new_cinema(self, cinema_name, showing):
        new_cinema = Cinema(cinema_name, showing)
        self.cinemas[cinema_name] = new_cinema
        self.update_json()
        return f"{new_cinema.cinema_name} added successfully."

    def delete_cinema(self, cinema_name):
        try: 
            del self.cinemas[cinema_name]
            self.update_json()
            return f"{cinema_name} has been deleted from the system."
        except: return f"{cinema_name} was not found in the system, try again."

    def update_json(self):
        data_to_save = {
            cinema_name: {
                "cinema_name": cinema.cinema_name,
                "showing": cinema.showing,
                "seats": cinema.seats
            }
            for cinema_name, cinema in self.cinemas.items()
        }
        with open("Cinema\cinemas.json", "w") as file:
            json.dump(data_to_save, file, indent=4)