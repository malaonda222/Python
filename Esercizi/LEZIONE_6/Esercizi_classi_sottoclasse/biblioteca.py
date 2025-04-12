class Libro:
    def __init__(self): 
        self.autore:str = ""
        self.titolo:str = ""
        self.genere:list[str] = []

    def set_autore(self, nome_autore:str): # set per dare valore ai nostri oggetti libro
        self.autore = nome_autore
    
    def set_titolo(self, titolo_libro:str):
        self.titolo = titolo_libro
    
    def set_genere(self, lista_genere:list[str]):
        self.genere = lista_genere

    def get_autore(self) -> str: # get per ritornare valori 
        return self.autore 
    
    def get_titolo(self) -> str:
        return self.titolo
    
    def get_genere(self) -> list[str]:
        return self.genere
    
class Biblioteca:
    def __init__(self):
        self.libri:list[Libro] = []

    def set_libro(self, libro:Libro):
        self.libri.append(libro)
    
    def get_libri_titolo(self): #per avere tutti i titolo all'interno della biblioteca
        for item in self.libri:
            print(item.get_titolo())

if __name__ == "__main__":
    collezione:Biblioteca = Biblioteca() #oggetto vuoto
    print("Biblioteca creata")

    piccolo_principe:Libro = Libro() #creo il primo libro
    piccolo_principe.set_titolo("Il Piccolo Principe")
    piccolo_principe.set_autore("Saint-Exupery")
    piccolo_principe.set_genere(["Narrativa"])
    print(piccolo_principe.get_titolo(), piccolo_principe.get_autore(), piccolo_principe.get_genere())

    fm:Libro = Libro() #creo il secondo libro
    fm.set_titolo("Le avventure di Federico March")
    fm.set_autore("Federico March")
    fm.set_genere(["Avventura", "Dramma"])
    print(fm.get_titolo(), fm.get_autore(), fm.get_genere())


    #inserimento primo libro e secondo libro nella collezione(Biblioteca)
    collezione.set_libro(piccolo_principe)
    collezione.set_libro(fm)
    print("Libri aggiunti alla collezione")
    print("------------------------")
    collezione.get_libri_titolo()

    test:Libro = Libro()
    test.set_titolo("Harry Potter")
    test.set_autore("JK Rowling")
    test.set_genere(["Fantasy"])

    collezione.set_libro(test)
    print("------------------------")
    collezione.get_libri_titolo()

