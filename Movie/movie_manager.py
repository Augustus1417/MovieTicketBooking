from Movie.movie import Movie
import string, random
import json

class MovieManager:
    def __init__(self):
        with open("Movie\movies.json", "r") as file:
                data = json.load(file)
                self.movie_list = {
                    reference_id: Movie(movie_data["title"], movie_data["duration"], movie_data["genre"])
                    for reference_id, movie_data in data.items()
                }
    
    def view_all_movies(self):
        for reference_id, movie in self.movie_list.items():
            print(f"\nReference ID: {reference_id}\n{movie}\n")

    def add_new_movie(self,title, duration, genre):
        reference_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        new_movie = Movie(title, duration, genre)
        self.movie_list[reference_id] = new_movie
        self.update_json()
        return f"{title} has been added to the system."

    def delete_movie(self, reference_id): 
        try: 
            title = self.movie_list[reference_id].title
            del self.movie_list[reference_id]
            self.update_json()
            return f"{title} has been deleted from the system."
        except: return f"{reference_id} was not found in the system, try again."

    def edit_details(self, reference_id, detail, new_detail):
        try:
            old_title = self.movie_list[reference_id].title
            match detail:
                case "title": self.movie_list[reference_id].title = new_detail
                case "duration": self.movie_list[reference_id].duration = new_detail
                case "genre": self.movie_list[reference_id].genre = new_detail
                case _: return "Unknown detail field, try again."
            self.update_json()
            return f"{old_title} edited successfully: \n{self.movie_list[reference_id]}"
        except: return f"{old_title} was not found in the system, try again."
    
    def update_json(self):
        data_to_save = {
            reference_id: {"title": movie.title, "duration": movie.duration, "genre": movie.genre}
            for reference_id, movie in self.movie_list.items()
        }
        with open("Movie\movies.json", "w") as file:
            json.dump(data_to_save, file, indent=4)