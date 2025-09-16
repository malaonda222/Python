from abc import ABC, abstractmethod

class LibroBase(ABC):
    def __init__(self, titolo: str, autore: str, disponibile: bool = True) -> None:
        self.titolo = titolo 
        self.autore = autore 
        self.disponibile = disponibile

    @property
    def disponibile(self) -> bool:
        return self._disponibile 
    
    @disponibile.setter
    def disponibile(self, stato: bool) -> None:
        if not isinstance(stato, bool):
            raise ValueError("Il valore di disponibilità deve essere True o False")
        self._disponibile = stato
        
    @property 
    def titolo(self) -> str:
        return self._titolo 
    
    @titolo.setter 
    def titolo(self, titolo: str) -> None:
        if not isinstance(titolo, str) or not titolo.strip():
            raise ValueError("Errore. Nome inserito non valido")
        self._titolo = titolo 
    
    @property 
    def autore(self) -> str:
        return self._autore 
    
    @autore.setter 
    def autore(self, autore: str) -> None:
        if not isinstance(autore, str) or not autore.strip():
            raise ValueError("Errore. Autore inserito non valido")
        self._autore = autore 
    
    @abstractmethod
    def __str__(self) -> str:
        pass 

    def prestito(self) -> bool:
        if self._disponibile:
            self._disponibile = False
    
    def restituisci(self) -> bool:
        if not self._disponibile:
            self._disponibile = True 
        
class LibroCartaceo(LibroBase):
    def __init__(self, titolo: str, autore: str, disponibile: bool, numero_pagine: int) -> None:
        super().__init__(titolo, autore, disponibile)
        self.numero_pagine = numero_pagine
    
    def __str__(self) -> str:
        stato = "Disponibile" if self.disponibile else "Non disponibile"
        return f"Titolo: {self.titolo}\nAutore: {self.autore}\nNumero di pagine: {self.numero_pagine}\nStato: {stato}"

class Ebook(LibroBase):
    def __init__(self, titolo: str, autore: str, disponibile: bool, dimensione_mb: float) -> None:
        super().__init__(titolo, autore, disponibile)
        self.dimensione_mb = dimensione_mb

    def __str__(self) -> str:
        stato = "Disponibile" if self.disponibile else "Non disponibile"
        return f"Titolo: {self.titolo}\nAutore: {self.autore}\nDimensione: {self.dimensione_mb}\nStato: {stato}"

class Utente:
    def __init__(self, nome: str, cognome: str, libri_presi: list[LibroBase] = None) -> None:
        self.nome = nome 
        self.cognome = cognome 
        self._libri_presi = libri_presi if libri_presi else []

    @property 
    def nome(self) -> str:
        return self._nome 
    
    @nome.setter 
    def nome(self, nome: str) -> None:
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Errore. Nome inserito non valido")
        self._nome = nome

    @property 
    def cognome(self) -> str:
        return self._cognome 
    
    @cognome.setter 
    def cognome(self, cognome: str) -> None:
        if not isinstance(cognome, str) or not cognome.strip():
            raise ValueError("Errore. Cognome inserito non valido")
        self._cognome = cognome

    @property
    def libri_presi(self) -> list[LibroBase]:
        return self._libri_presi
    
    def prendi_in_prestito(self, libro: LibroBase) -> None:
        if libro.disponibile:
            self.libri_presi.append(libro)
            libro.prestito()
        else:
            raise ValueError("Libro non disponibile")
    
    def restituisci_libro(self, libro: LibroBase) -> None:
        if libro not in self._libri_presi:
            raise ValueError("Errore. Il libro non risulta essere stato prestato")
        else:
            self._libri_presi.remove(libro)
            libro.restituisci() 
    
    def __str__(self) -> str:
        libri = "\n".join([str(libro) for libro in self._libri_presi]) or "Nessun libro"
        return f"Nome: {self.nome}\nCognome: {self.cognome}\nLista dei libri presi: {libri}"

librocartaceo = LibroCartaceo("Tre Piani", "Nevo", True, 190)
ebook = Ebook("Dance Dance Dance", "Murakami", True, 2)
print(librocartaceo)
print()
print(ebook)
utente1 = Utente("Bianca", "Ticci")
utente1.prendi_in_prestito(librocartaceo)
print()
print(librocartaceo)
print()
print(utente1)

utente2 = Utente("Margherita", "Siani")
utente2.prendi_in_prestito(ebook)
print()
print(ebook)
print()
print(utente2)
print()
utente2.restituisci_libro(ebook)
print(ebook)
print()
print(utente2)
