from __future__ import annotations
from abc import ABC, abstractmethod
from flask import Flask, jsonify, request, url_for
from typing import List, Dict, Any

app = Flask(__name__)

# Classe base per un film
class Movie(ABC):
    def __init__(self, id: str, title: str, director: str, year: int, description: str) -> None:
        self.id: str = id
        self.title: str = title
        self.director: str = director
        self.year: int = year
        self.description: str = description

    @abstractmethod
    def category(self) -> str:
        """Restituisce la categoria del film."""
        pass

    def info(self) -> dict:
        """Restituisce un dizionario con le informazioni principali."""
        return {
            "id": self.id,
            "title": self.title,
            "director": self.director,
            "year": self.year,
            "description": self.description,
            "category": self.category()
        }

# Classe per un film di tipo Action
class ActionMovie(Movie):
    def __init__(self, id: str, title: str, director: str, year: int, description: str, lead_actor: str) -> None:
        super().__init__(id, title, director, year, description)
        self.lead_actor = lead_actor

    def category(self) -> str:
        return "action"

    def info(self) -> dict:
        info_dict = super().info()
        info_dict["lead_actor"] = self.lead_actor
        return info_dict

# Classe per un film di tipo Drama
class DramaMovie(Movie):
    def __init__(self, id: str, title: str, director: str, year: int, description: str, theme: str) -> None:
        super().__init__(id, title, director, year, description)
        self.theme = theme

    def category(self) -> str:
        return "drama"

    def info(self) -> dict:
        info_dict = super().info()
        info_dict["theme"] = self.theme
        return info_dict

# Gestione dei film
class MovieLibrary:
    def __init__(self, movies: Dict[str, Movie] = None) -> None:
        self.movies = movies if movies else {}

    def add(self, movie: Movie) -> None:
        self.movies[movie.id] = movie

    def get(self, movie_id: str) -> Movie | None:
        return self.movies.get(movie_id)

    def list_all(self) -> List[Movie]:
        return sorted(self.movies.values(), key=lambda m: m.title)

    def update(self, movie_id: str, updated_movie: Movie) -> bool:
        if movie_id in self.movies:
            self.movies[movie_id] = updated_movie
            return True
        return False

    def delete(self, movie_id: str) -> bool:
        if movie_id in self.movies:
            del self.movies[movie_id]
            return True
        return False
    
    def patch_year(self, movie_id: str, new_year: int) -> bool:
        """Aggiorna l'anno di un film dato l'id."""
        movie = self.get(movie_id)
        if not movie:
            return False

        movie.year = new_year  # Cambia solo l'anno del film
        return True


# Creazione della libreria e aggiunta dei film
movie_library = MovieLibrary()

# Aggiungiamo alcuni film
movie_library.add(ActionMovie("1", "Mad Max: Fury Road", "George Miller", 2015, "A high-octane action film.", "Tom Hardy"))
movie_library.add(DramaMovie("2", "The Shawshank Redemption", "Frank Darabont", 1994, "A powerful story about hope.", "Prison Drama"))


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to FILM API",
        "links": {
            "get_all_movies": url_for("get_movies"),
            "get_movie": url_for("get_movie", movie_id="123"),
            "create_movie": url_for("add_movie"),
            "put_movie": url_for("put_movie", movie_id="123"),
            "patch_movie": url_for("patch_movie", movie_id="123")
        }
    })

@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movie_library.list_all())

@app.route('/movies/<string:movie_id>', methods=['GET'])
def get_film(movie_id):
    movie = movie_library.get(movie_id)
    if movie is None:
        return jsonify({"error": "Movie not found"}), 404 
    return jsonify(movie.info())

@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Request must be in JSON body"}), 400
    
    if "category" not in data:
        return jsonify({"error": "Missing category"}), 400
    
    category = data.get("category")
    try:
        if category == "action":
            required_fields = ['id', 'title', 'director', 'year', 'description', 'lead_actor']
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": "missing field"}), 400

            movie = ActionMovie(
                id=data["id"],
                title=data["title"],
                directior=data["director"], 
                year=data["year"],
                description=data["description"],
                lead_actor=data["lead_actor"]
            ) 

        elif category == "drama":
            required_fields = ['id', 'title', 'director', 'year', 'description', 'theme']
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": "Missing required fields"}), 400
            
            movie = DramaMovie(
                id=data["id"],
                title=data["title"],
                director=data["director"],
                year=data["year"],
                description=data["description"],
                theme=data["theme"]
            )

        else:
            return jsonify({"error": "Category not valid"}), 400
        
        ok = movie_library.add(movie)
        if not ok:
            return jsonify({"error": "Device already exist"}), 400
        return jsonify(movie.info()), 201
    
    except KeyError:
        return jsonify({"error": "Invalid data. Missing required fields"}), 400
    
@app.route('/movies/<string:movie_id>', methods=['PUT'])
def put_movie(movie_id):
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Request must be a JSON object"}), 400
    
    movie = movie_library.get(movie_id)
    if movie is None:
        return jsonify({"error": "Movie not found"}), 404 
    
    if "category" not in data:
        return jsonify({"error": "Missing category"}), 400
    
    category = data["category"]
    try: 
        if category == "action":
            required_fields = ['id', 'title', 'director', 'year', 'description', 'lead_actor']
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": "Missing required fields"}), 400
            
            movie = ActionMovie(
                id=movie_id,
                title=data["title"],
                director=data["director"],
                year=data["year"],
                description=data["description"],
                lead_actor=data["lead_actor"]
            )

        elif category == "drama":
            required_fields = ['id', 'title', 'director', 'year', 'description', 'theme']
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": "Missing required fields"}), 400
                
            movie = DramaMovie(
                id=movie_id,
                title=data["title"],
                director=data["director"],
                year=data["year"],
                description=data["description"],
                theme=data["theme"]
            )
        
        else:
            return jsonify({"error": "Input not valid, category not valid"}), 400
        
        movie_library.update(movie_id, movie)
        return jsonify(movie.info())
        
    except Exception:
        return jsonify({"error": "Invalid data. Missing required fields"}), 400
    
@app.route('/movies/<string:movie_id>/year', methods=['PATCH'])
def patch_movie(movie_id):
    movie = movie_library.get(movie_id)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404 
    
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Request must be a JSON object"}), 400
    
    if "year" not in data:
        return jsonify({"error": "Missing year field"}), 400
    
    new_year = data["year"]
    if not new_year or not isinstance(new_year, int):
        return jsonify({"error": "Invalid input for year"}), 400
    
    movie_library.patch_year(movie_id, new_year)
    return jsonify(movie_library.get(movie_id).info())

@app.route('/movies/<string:movie_id', methods=['DELETE'])
def delete_movie(movie_id):
    deleted = movie_library.delete(movie_id)
    if not deleted:
        return jsonify({"error": "Movie not found"}), 404
    return "Movie deleted", 204 

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)