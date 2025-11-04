'''Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

    Classe Book:
        Attributi:
            book_id: str - Identificatore di un libro.
            title: str - titolo del libro.
            author: str - autore del libro
            is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
        Metodi:
            borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
            return_book()- Contrassegna il libro come restituito.

    Classe Member:
        Attributi:
            member_id: str - identificativo del membro.
            name: str - il nome del membro.
            borrowed_books: list[Book] - lista dei libri presi in prestito.
        Metodi:
            borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
            return_book(book): rimuove il libro dalla lista borrowed_books.

    Classe Library:
        Attributi:
            books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
            members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
        Metodi:
            add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
            register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
            borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
            return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
            get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.
'''

class Book:
    def __init__(self, book_id: str, title: str, author: str) -> None:
        self.book_id: str = book_id
        self.title: str = title 
        self.author: str = author
        self.is_borrowed: bool = False 
    
    def borrow(self) -> None:
        if not self.is_borrowed:
            self.is_borrowed = True 
        else:
            print(f"Il libro è già in prestito")
    
    def return_book(self) -> None:
        if self.is_borrowed:
            self.is_borrowed = False 
        else:
            print(f"Il libro non è stato prestato")
    

class Member:
    def __init__(self, member_id: str, name: str) -> None:
        self.member_id: str = member_id
        self.name: str = name 
        self.borrowed_books: list[Book] = []
    
    def borrow_book(self, book: Book) -> None:
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"Il libro è già stato preso in prestito")
    
    def return_book(self, book: Book) -> None:
        if book.is_borrowed:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"Il libro non è stato preso in prestito")

class Library:
    def __init__(self) -> None:
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}

    def add_book(self, book_id: str, title: str, author: str) -> None:
        if book_id not in self.books:
            self.books[book_id] = Book(book_id, title, author)
        else:
            print("Il libro esiste già")
    
    def register_member(self, member_id: str, name: str) -> None:
        if member_id not in self.members:
            self.members[member_id] = Member(member_id, name)
        else:
            print("Il membro è già registrato")

    def borrow_book(self, member_id: str, book_id: str) -> None:
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            member.borrow_book(book)
        else:
            print("Membro o libro non trovato")
    
    def return_book(self, member_id: str, book_id: str) -> None:
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            member.return_book(book)
        else:
            print("Membro o libro non trovato")
    
    def get_borrowed_books(self, member_id: str) -> list[Book]|str:
        if member_id not in self.members:
            return "Membro non trovato"
        else:
            member = self.members[member_id]
            return [book.book_id for book in member.borrowed_books]
