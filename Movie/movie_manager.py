from Movie.movie import Movie
import json

class MovieManager:
    def __init__(self):
        with open("Movie\movies.json", "r") as file:
                data = json.load(file)
                self.movie_list = {
                    title: Movie(movie_data["title"], movie_data["duration"], movie_data["genre"])
                    for title, movie_data in data.items()
                }
    
    def view_all_movies(self):
        for movie in self.movie_list.values():
            print(movie, "\n")

    def add_new_movie(self, title, duration, genre):
        new_movie = Movie(title, duration, genre)
        self.movie_list[title] = new_movie
        self.update_json()
        return f"{title} has been added to the system."

    def delete_movie(self, title): 
        try: 
            del self.movie_list[title]
            self.update_json()
            return f"{title} has been deleted from the system."
        except: return f"{title} was not found in the system, try again."

    def edit_details(self, title, detail, new_detail):
        try:
            match detail:
                case "title": 
                    self.movie_list[new_detail] = self.movie_list[title]
                    self.movie_list[new_detail].title = new_detail
                    del self.movie_list[title]
                    self.update_json()
                    return f"{title} edited successfully: \n{self.movie_list[new_detail]}"
                case "duration":
                    self.movie_list[title].duration = new_detail
                case "genre":
                    self.movie_list[title].genre = new_detail
                case _: return "Unknown detail field, try again."
            self.update_json()
            return f"{title} edited successfully: \n{self.movie_list[title]}"
        except: return f"{title} was not found in the system, try again."
    
    def update_json(self):
        data_to_save = {
            title: {"title": movie.title, "duration": movie.duration, "genre": movie.genre}
            for title, movie in self.movie_list.items()
        }
        with open("Movie\movies.json", "w") as file:
            json.dump(data_to_save, file, indent=4)