class Book:
    def __init__(self, title:str, author:str, year:int):
        self.title = title
        self.author = author 
        self.year = year 

    def __str__(self):
        return f"Titolo: {self.title}, Autore: {self.author}, Anno: {self.year}"
    
    def is_classic(self):
        return self.year < 2000
            

first_book = Book("Pinocchio", "Collodi", 1990)
print(f"Il primo libro inserito è: {first_book}.")
print(f"Il primo libro è un classico? {first_book.is_classic()}.")

second_book = Book("La Profezia dell'Armadillo", "Zerocalcare", 2017)
print(f"Il secondo libro inserito è: {second_book}.")
print(f"Il secondo libro è un classico? {second_book.is_classic()}")


