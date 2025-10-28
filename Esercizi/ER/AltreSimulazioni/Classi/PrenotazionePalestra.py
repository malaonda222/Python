'''Classe Corso

Rappresenta un corso della palestra. Deve avere:
corso_id: str
nome: str
istruttore: str
posti: int

Metodi:
__init__
prenota() → decrementa posti_disponibili se > 0, altrimenti ritorna un errore
cancella_prenotazione() → incrementa posti_disponibili
__str__() → restituisce "Nome corso" di Istruttore (Posti disponibili: X)


Classe GymManager
Gestisce i corsi. Deve avere:
corsi: dict[str, Corso]

Metodi da implementare:
aggiungi_corso(corso_id: str, nome: str, istruttore: str, posti: int) → aggiunge un corso se corso_id non esiste
rimuovi_corso(corso_id: str) → rimuove un corso se esiste
prenota_corso(corso_id: str) → prenota un posto nel corso
cancella_prenotazione(corso_id: str) → cancella una prenotazione
lista_corsi() → ritorna tutti gli ID dei corsi
info_corso(corso_id: str) → ritorna le informazioni sul corso'''


class Corso:
    def __init__(self, corso_id: str, nome: str, istruttore: str, posti: int) -> None:
        self.corso_id: str = corso_id
        self.nome: str = nome 
        self.istruttore: str = istruttore
        self.posti: int = posti
    
    def prenota(self, numero_posti: int = 1) -> None:
        if self.posti <= 0 or self.posti < numero_posti:
            raise ValueError("Posti disponibili insufficienti")
        else:
            self.posti -= numero_posti

    def cancella_prenotazione(self, numero_posti: int = 1) -> None:
        if numero_posti < 0:
            raise ValueError("Errore. Input non valido")
        else:
            self.posti += numero_posti
 
    def __str__(self) -> str:
        return f"Nome corso: '{self.nome}' (Posti disponibili: {self.posti})"


class GymManager:
    def __init__(self) -> None:
        self.corsi: dict[str, Corso] = {}

    def aggiungi_corso(self, corso_id: str, nome: str, istruttore: str, posti: int) -> None:
        if corso_id not in self.corsi:
            self.corsi[corso_id] = Corso(corso_id, nome, istruttore, posti)
        else:
            print(f"Il corso (ID {corso_id}) è già presente nel dizionario dei corsi")
    
    def rimuovi_corso(self, corso_id: str) -> None:
        if corso_id in self.corsi:
            self.corsi.pop(corso_id)
        else:
            print(f"Il corso con ID {corso_id} non è presente nel dizionario")
    
    def prenota_corso(self, corso_id: str, numero_posti: int = 1) -> None:
        if corso_id in self.corsi:
            corso = self.corsi[corso_id]
            corso.prenota(numero_posti)
        else:
            print(f"Non è possibile prenotare per il corso con ID {corso_id}")
    
    def cancella_prenotazione(self, corso_id: str, numero_posti: int = 1) -> None:
        if corso_id in self.corsi:
            corso = self.corsi[corso_id]
            corso.cancella_prenotazione(numero_posti)
        else:
            print(f"Non è possibile cancellare la prenotazione per il corso con ID {corso_id}")

    def lista_posti(self) -> list:
        if not self.corsi:
            return []
        else:
            return [corso.corso_id for corso_id, corso in self.corsi.items()]
    
    def info_corso(self, corso_id: str) -> dict:
        if corso_id not in self.corsi:
            return f"Corso con ID {corso_id} non presente nel dizionario"
        else:
            return {corso_id: self.corsi[corso_id]}
    
