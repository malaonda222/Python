from __future__ import annotations
from abc import ABC, abstractmethod
from flask import Flask, jsonify, request, url_for
from typing import List, Dict, Any

app = Flask(__name__)

# Classe base per un libro
class Book(ABC):
    def __init__(self, id: str, title: str, author: str, year: int, description: str) -> None:
        self.id: str = id
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.description: str = description

    @abstractmethod
    def category(self) -> str:
        """Restituisce la categoria del libro."""
        pass

    def info(self) -> dict:
        """Restituisce un dizionario con le informazioni principali."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "description": self.description,
            "category": self.category()
        }

# Classe per un libro di tipo Fiction
class FictionBook(Book):
    def __init__(self, id: str, title: str, author: str, year: int, description: str, genre: str) -> None:
        super().__init__(id, title, author, year, description)
        self.genre = genre

    def category(self) -> str:
        return "fiction"

    def info(self) -> dict:
        info_dict = super().info()
        info_dict["genre"] = self.genre
        return info_dict

# Classe per un libro di tipo Non-Fiction
class NonFictionBook(Book):
    def __init__(self, id: str, title: str, author: str, year: int, description: str, subject: str) -> None:
        super().__init__(id, title, author, year, description)
        self.subject = subject

    def category(self) -> str:
        return "non-fiction"

    def info(self) -> dict:
        info_dict = super().info()
        info_dict["subject"] = self.subject
        return info_dict

# Gestione dei libri
class Library:
    def __init__(self, books: Dict[str, Book] = None) -> None:
        self.books = books if books else {}

    def add(self, book: Book) -> None:
        self.books[book.id] = book

    def get(self, book_id: str) -> Book | None:
        return self.books.get(book_id)

    def list_all(self) -> List[Book]:
        return sorted(self.books.values(), key=lambda b: b.title)

    def update(self, book_id: str, updated_book: Book) -> bool:
        if book_id in self.books:
            self.books[book_id] = updated_book
            return True
        return False

    def delete(self, book_id: str) -> bool:
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False


# Creazione della libreria e aggiunta dei libri
library = Library()

# Aggiungiamo alcuni libri
library.add(FictionBook("1", "The Great Gatsby", "F. Scott Fitzgerald", 1925, "A novel about the American dream.", "Literary Fiction"))
library.add(NonFictionBook("2", "Sapiens", "Yuval Noah Harari", 2011, "A brief history of humankind.", "History"))


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify ({
        "message": "Welcome to Book API",
        "links": {
            "all_books": url_for("get_all_books"),
            "get_book": url_for("get_book", book_id="34JK"),
            "post_book": url_for("create_book"),
            "put_book": url_for("put_book", book_id="34JK"),
            "delete_book": url_for("delete_book", book_id="34JK")
        }
    })

@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify(library.list_all())

@app.route('/books/<string:book_id>', methods=['GET'])
def get_book(book_id):
    book = library.get(book_id)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book.info())

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Request must be a JSON object"}), 400
    
    if "category" not in data:
        return jsonify({"error": "Missing cateogry field"}), 400
    
    category = data["category"]

    try:
        if category == "fiction":
            required_fields = ['id', 'title', 'author', 'year', 'description', 'genre']
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": "Missing field {field}"}), 400
                
            book = FictionBook(
                id= data["id"],
                title=data["title"],
                author=data["author"],
                year=data["year"],
                description=data["description"],
                genre=data["genre"]
            )

        elif category == "non-fiction":
            required_fields = ['id', 'title', 'author', 'year', 'description', 'subject']
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": "Missing required field"}), 400
                
            book = NonFictionBook(
                id=data["id"],
                title=data["title"],
                author=data["author"],
                year=data["year"],
                description=data["description"],
                subject=data["subject"]
            )

        else:
            return jsonify({"error": "invalid category. It mus be 'fiction' or 'book'"}), 400

        library.add(book)
        return jsonify({book.info()}), 201
    
    except KeyError:
        return jsonify({"errore": "invalid data. Missing required fields"}), 400

@app.route('/books/<string:book_id>', methods=['PUT'])
def put_book(book_id):
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Request must be in JSON object"}), 400
    
    book = library.get(book_id)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    
    if 'category' not in data:
        return jsonify({"error": "category field is required"}), 400
    
    category = data["category"]

    try:
        if category == "fiction":
            required_fields = ['id', 'title', 'author', 'year', 'description', 'genre']
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": "Missing field {field}"}), 400
                
            book = FictionBook(
                id=book_id, #mantieni l'id originario
                title=data["title"],
                author=data["author"],
                year=data["year"],
                description=data["description"],
                genre=data["genre"]
            )

        elif category == "non-fiction":
            required_fields = ['id', 'title', 'author', 'year', 'description', 'subject']
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": "Missing required field"}), 400
                
            book = NonFictionBook(
                id=book_id, #mantieni l'id originario
                title=data["title"],
                author=data["author"],
                year=data["year"],
                description=data["description"],
                subject=data["subject"]
            )

        else:
            return jsonify({"error": "invalid category. It mus be 'fiction' or 'book'"}), 400

        library.update(book_id, book)
        return jsonify({book.info()})
    
    except KeyError:
        return jsonify({"error": "invalid data. Missing required fields"}), 400
    

@app.route('/books/<string:book_id>', methods=['DELETE'])
def delete_book(book_id):
    deleted = library.delete(book_id)
    if not deleted:
        return jsonify({"error": "Book not found"}), 404
    return jsonify({"deleted": True, "book_id": book_id}), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
