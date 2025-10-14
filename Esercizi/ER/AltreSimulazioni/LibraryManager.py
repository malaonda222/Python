class LibraryManager:
    def __init__(self) -> None:
        self.books: dict[str, dict] = {}

    def aggiungi_libro(self, book_id: str, titolo: str) -> dict|str:
        if book_id in self.books:
            raise ValueError("Errore. Il libro esiste già.")
        else:
            self.books[book_id] = {"titolo": titolo, "disponibile": True}
            return {book_id: self.books[book_id]}
        
    def presta_libro(self, book_id: str) -> dict|str:
        if book_id not in self.books:
            raise ValueError("Errore. Il libro non esiste")
        elif self.books[book_id]["disponibile"] == False:
            raise ValueError("Errrore. Il libro non è disponibile")
        else:
            self.books[book_id]["disponibile"] = False 
            return {book_id: self.books[book_id]}
        
    def restituisci_libro(self, book_id: str) -> dict|str:
        if book_id not in self.books:
            raise ValueError("Errore. Libro non trovato.")
        elif self.books[book_id]["disponibile"] == True:
            raise ValueError("Errore. Libro già disponibile")
        else:
            self.books[book_id]["disponibile"] = True
            return {book_id: self.books[book_id]}
        
    def rimuovi_libro(self, book_id: str) -> dict|str:
        if book_id not in self.books:
            raise ValueError("Errore. Libro non trovato")
        else:
            rimosso = self.books.pop(book_id)
            return {book_id: rimosso}
    
    def elenco_libri(self) -> list[str]:
        return list(self.books.keys())
    
    def get_libro(self, book_id: str) -> dict|str:
        if book_id not in self.books:
            raise ValueError("Errore. Libro non trovato.")
        else:
            return {book_id: self.books[book_id]}