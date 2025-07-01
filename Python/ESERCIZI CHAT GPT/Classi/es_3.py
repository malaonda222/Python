class Library:
    total_books = 0

    @classmethod
    def add_book(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books
    

Library.add_book()
Library.add_book()
Library.add_book()
Library.add_book()


print(f"Il numero totale dei libri è: {Library.get_total_books()}")