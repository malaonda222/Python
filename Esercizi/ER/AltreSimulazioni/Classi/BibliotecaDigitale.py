class EBook:
    def __init__(self, book_id: str, title: str, author: str) -> None:
        self.book_id: str = book_id
        self.title: str = title 
        self.author: str = author
        self.is_borrowed: bool = False 

    def borrow(self) -> None:
        if not self.is_borrowed:
            self.is_borrowed = True 
        else:
            print(f"Il libro '{self.title}' di '{self.author}' è già in prestito.")

    def return_book(self) -> None:
        if self.is_borrowed:
            self.is_borrowed = False 
        else:
            print(f"Il libro '{self.title}' di '{self.author}' non è attualmente in prestito.")
    

class User: 
    def __init__(self, user_id: str, name: str) -> None:
        self.user_id: str = user_id
        self.name: str = name 
        self.borrowed_books: list[EBook] = []

    def borrow_book(self, book: EBook) -> None:
        if not book.is_borrowed:
            self.borrowed_books.append(book)
            book.borrow()
        else:
            print(f"Il libro '{book.title}' non è disponibile per il prestito.")
    
    def return_book(self, book: EBook) -> None:
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
        else:
            print(f"Il libro '{book.title}' non è stato preso in prestito da questo utente.")
    

class DigitalLibrary:
    def __init__(self) -> None:
        self.books: dict[str, EBook] = {}
        self.users: dict[str, User] = {}
    
    def add_book(self, book_id: str, title: str, author: str) -> None:
        if book_id in self.books:
            print(f"Il libro con ID '{book_id}' esiste già.")
        else:
            self.books[book_id] = EBook(book_id, title, author)
    
    def register_user(self, user_id: str, name: str) -> None:
        if user_id in self.users:
            print(f"L'utente con ID '{user_id}' è già registrato.")
        else:
            self.users[user_id] = User(user_id, name)
    
    def borrow_book(self, user_id: str, book_id: str) -> None:
        if user_id in self.users and book_id in self.books:
            user = self.users[user_id]
            book = self.books[book_id]
            user.borrow_book(book)
        else:
            print("Utente o libro non trovato.")
    
    def return_book(self, user_id: str, book_id: str) -> None:
        if user_id in self.users and book_id in self.books:
            user = self.users[user_id]
            book = self.books[book_id]
            user.return_book(book)
        else:
            print("Utente o libro non trovato.")
    
    def list_available_books(self) -> list[str]:
        return [book_id for book_id, book in self.books.items() if not book.is_borrowed]
    
    def list_user_borrowed_books(self, user_id: str) -> list[str]|str:
        if user_id in self.users:
            user = self.users[user_id]
            return [book.book_id for book in user.borrowed_books]
        else:
            return "Errore. Utente non trovato."