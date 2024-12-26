from movie_manager import MovieManager
movieManager = MovieManager()

def add_movie():
    print("Add Movie")
    title = input("Movie Title: ")
    duration = input("Duration: ")
    genre = input("Genre: ")
    print(movieManager.add_new_movie(title,duration,genre))

def remove_movie():
    title = input("Enter title to delete: ")
    print(movieManager.delete_movie(title))

def edit_movie():
    title = input("Enter title to edit: ")
    detail = input("Enter detail to edit: ").lower()
    new_detail = input("Enter new detail:")
    print(movieManager.edit_details(title, detail, new_detail))

def view_movies():
    movieManager.view_all_movies()

def main():
    print("Welcome, Admin!")
    while True:
        choice = input("\n1. Add new movie"
                    "\n2. Remove movie"
                    "\n3. Edit movie details"
                    "\n4. View all movies"
                    "\n5. Exit"
                    "\nYour choice (1-5): ")
        match choice:
            case "1": add_movie()
            case "2": remove_movie()
            case "3": edit_movie()
            case "4": view_movies()
            case "5": break
            case _: print("1-5 only, try again")

main()