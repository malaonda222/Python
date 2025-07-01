class Book:
    def __init__(self, titolo: str, autore: str, isbn: str):
        self._titolo = titolo
        self._autore = autore 
        self._isbn = isbn

    def __str__(self) -> str:
        return f"Titolo: {self._titolo}\nAutore: {self._autore}\nISBN: {self._isbn}"
    
    @classmethod 
    def from_string(cls, str_repr: str):
        parts: list[str] = str_repr.split(", ")
        return Book(parts[0], parts[1], parts[2])

class Membro:
    def __init__(self, nome: str, member_id: int):
        self.nome = nome 
        self.member_id = member_id 
        self.borrowed_books = []

    def borrow_book(self, libro: Book):
        if libro not in self.borrowed_books:
            self.borrowed_books.append(libro)
            print(f"Libro \"{libro}\"\npreso in prestito da {self.nome}.\n")
        else:
            print(f"{self.nome} ha già preso in prestito il libro \"{libro}\".\n")

    def return_book(self, libro: Book):
        if libro in self.borrowed_books:
            self.borrowed_books.remove(libro)
        else:
            print("Il libro non si trova nella lista.")
    
    def __str__(self):
        return f"Nome: {self.nome}\nMember_id: {self.member_id}"
    
    @classmethod 
    def from_string(cls, member_str: str):
        parts = member_str.split(", ")
        if len(parts) != 2:
            raise ValueError("La stringa deve essere nel formato \"nome, member_id\".")
        nome, member_id = parts 
        return cls(nome, int(member_id))


class Libreria:
    totale_libri = 0
    def __init__(self):
        self.libri = []
        self.membri = []
    
    def aggiungi_libro(self, libro: Book):
        self.libri.append(libro)
        Libreria.totale_libri += 1

    def rimuovi_libro(self, libro: Book):
        if libro in self.libri:
            self.libri.remove(libro)
            Libreria.totale_libri -= 1
        else:
            print("Il libro non si trova nella libreria.")

    def registra_membro(self, membro: Membro):
        if membro not in self.membri:
            self.membri.append(membro)
        else:
            print("La persona è già un membro della libreria.")

    def presta_libro(self, libro: Book, membro: Membro):
        if libro not in self.libri:
            print("Libro non disponibile in libreria.")
            return
        if membro not in self.membri:
            print("Membro non registrato nella libreria.")
            return
        
        membro.borrow_book(libro)
        self.rimuovi_libro(libro)
        print(f"Libro \"{libro.titolo}\" prestato a {membro.nome}, {membro.member_id}.")

    def __str__(self):
        libri_str = ""
        if not self.libri:
            libri_str = "Nessun libro disponibile."
        else:
            for libro in self.libri:
                libri_str += str(libro) + "\n\n"
        
        membri_str = ""
        if not self.membri:
            membri_str = "Nessun membro registrato."
        else:
            for membro in self.membri:
                membri_str += str(membro) + "\n\n"

        return (
            f"Biblioteca:\n\n"
            "Libri disponibili("+str(len(self.libri)) + "):\n\n" + libri_str.strip() + "\n\n"
            "Membri registrati("+str(len(self.membri)) + "):\n\n" + membri_str.strip() + "\n"
        )
    
    @classmethod
    def library_statistic(cls):
        print(f"Totale libri registrati nella libreria: {cls.totale_libri}.")
        
        

libreria = Libreria()

info = "La Divina Commedia, Dante Alighieri, 855695324"
divina_commedia = Book.from_string(info)
print(divina_commedia)

infor = "\"1984\", George Orwell, 1584693"
george_orwell = Book.from_string(infor)
print(george_orwell)

informa = "Il Piccolo Principe, Antoine de Saint-Exupery, 154693"
principe = Book.from_string(informa)
print(principe)

informaz = "Tre Piani, Eskol Nevo, 1479936546"
piani = Book.from_string(informaz)
print(piani)

print("\n-----------------\n")

infos = "Giuseppe Mini, 10596"
giuseppe = Membro.from_string(infos)
print(giuseppe)

inform = "Gino Fini, 145976"
gino = Membro.from_string(inform)
print(gino)

print("\n-----------------\n")

gino.borrow_book("Il Piccolo Principe")

print(libreria)

giuseppe.borrow_book("La Divina Commedia")

libreria.aggiungi_libro(divina_commedia)
libreria.aggiungi_libro(george_orwell)
libreria.aggiungi_libro(principe)
libreria.aggiungi_libro(piani)
libreria.registra_membro(giuseppe)
libreria.registra_membro(gino)

print(libreria)

libreria.presta_libro(piani, gino)

print(libreria)
print(gino)

libreria.library_statistic()


