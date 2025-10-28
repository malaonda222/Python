'''
1. Classe Corso
Rappresenta un corso (materia o insegnamento) offerto dalla scuola.

Attributi
nome: stringa
docente: stringa (o oggetto Docente, se vuoi estendere dopo)
studenti_iscritti: lista di oggetti Studente
attivo: booleano (True se il corso è attivo)

Metodi
__init__
attiva() → imposta attivo = True
disattiva() → imposta attivo = False
aggiungi_studente(studente: Studente) → aggiunge uno studente alla lista
rimuovi_studente(studente: Studente) → rimuove lo studente
__str__() → restituisce una stringa tipo: "Corso di Matematica tenuto da Rossi (3 studenti, Attivo)"

2. Classe Studente
Rappresenta uno studente iscritto alla scuola.

Attributi
nome: stringa
id_studente: stringa
corsi_iscritti: lista di oggetti Corso

Metodi
__init__
iscriviti_corso(corso: Corso) → aggiunge il corso alla lista e iscrive lo studente nel corso
abbandona_corso(corso: Corso) → rimuove il corso dalla lista e dallo stesso corso
__str__() → restituisce "Nome (ID: S001) - Corsi: [Matematica, Inglese]" 


3.Classe Scuola
Rappresenta l’intero sistema della scuola digitale.

Attributi
nome: stringa
studenti: dizionario di oggetti Studente, chiave: id_studente
corsi: dizionario di oggetti Corso, chiave: nome

Metodi
__init__
aggiungi_studente(studente: Studente)
aggiungi_corso(corso: Corso)
iscrivi_studente_a_corso(id_studente: str, nome_corso: str)
rimuovi_studente_da_corso(id_studente: str, nome_corso: str)
lista_corsi_attivi() → restituisce tutti i corsi con attivo == True
__str__() → stampa un riepilogo con numero studenti e corsi'''


from __future__ import annotations

class Corso:
    def __init__(self, nome: str, docente: str) -> None:
        self.nome: str = nome 
        self.docente: str = docente 
        self.studenti_iscritti: list[Studente] = []
        self.attivo: bool = True 

    def disattiva(self) -> None:
        if self.attivo: 
            self.attivo = False 

    def aggiungi_studente(self, studente: Studente) -> None:
        if studente not in self.studenti_iscritti:
            self.studenti_iscritti.append(studente)
        else:
            print(f"Lo studente {self.nome} risulta già iscritto al corso")
    
    def rimuovi_studente(self, studente: Studente) -> None:
        if studente not in self.studenti_iscritti:
            print(f"Lo studente {studente.nome} non risulta nel corso")
        else:
            self.studenti_iscritti.remove(studente)
    
    def __str__(self) -> str:
        stato_corso = "Attivo" if self.attivo else "Non Attivo"
        return f"Corso di {self.nome} tenuto da {self.docente} ({len(self.studenti_iscritti)}, {stato_corso})"


class Studente:
    def __init__(self, nome: str, id_studente: str) -> None:
        self.nome: str = nome 
        self.id_studente: str = id_studente
        self.corsi_iscritti: list[Corso] = []
    
    def iscriviti_corso(self, corso: Corso) -> None:
        if corso not in self.corsi_iscritti:
            self.corsi_iscritti.append(corso)
            corso.aggiungi_studente(self)
        else:
            print(f"Il corso {corso.nome} si trova già nella lista dei corsi iscritti")
    
    def abbandona_corso(self, corso: Corso) -> None:
        if corso in self.corsi:
            self.corsi.remove(corso)
            corso.rimuovi_studente(self)
        else:
            print(f"Il corso {corso.nome} non risulta nei corsi iscritti")
    
    def __str__(self) -> str:
        corsi = ", ".join(corso.nome for corso in self.corsi_iscritti)
        return f"{self.nome} (ID: {self.id_studente}) - Corsi: {corsi}"


class Scuola:
    def __init__(self, nome: str) -> None:
        self.nome: str = nome 
        self.studenti: dict[str, Studente] = {}
        self.corsi: dict[str, Corso] = {}
    
    def aggiungi_studente(self, studente: Studente) -> None:
        if studente.id_studente not in self.studenti:
            self.studenti[studente.id_studente] = studente 
        else:
            print(f"Studente {studente.nome} già presente nel dizionario")
    
    def aggiungi_corso(self, corso: Corso) -> None:
        if corso.nome not in self.corsi:
            self.corsi[corso.nome] = corso 
        else:
            print(f"Corso {corso.nome} già presente nel dizionario")
    
    def iscrivi_studente_a_corso(self, id_studente: str, nome_corso: str) -> None:
        if id_studente in self.studenti and nome_corso in self.corsi:
            studente = self.studenti[id_studente]
            corso = self.corsi[nome_corso]
            corso.aggiungi_studente(studente)
        else:
            print("Corso o studente non trovato")
    
    def rimuovi_studente_da_corso(self, id_studente: str, nome_corso: str) -> None:
        if id_studente in self.studenti and nome_corso in self.corsi:
            corso = self.corsi[nome_corso]
            studente = self.studenti[id_studente]
            corso.rimuovi_studente(studente)
        else:
            print("Corso o studente non trovato")

    def lista_corsi_attivi(self) -> list | None:
        if not self.corsi:
            return None
        else:
            return [corso.nome for corso in self.corsi.values() if corso.attivo == True]
    
    def __str__(self) -> str:
        risultato = ""
        if not self.studenti:
            risultato += "La lista degli studenti è vuota"
        else:
            risultato += f"Il numero totale degli studenti è: {len(self.studenti)}\n"
        
        if not self.corsi:
            risultato += "La lista dei corsi è vuota"
        else:
            risultato += f"Il numero totale dei corsi è: {len(self.corsi)}"
        return risultato


matematica = Corso("Matematica", "Rossi")
filosofia = Corso("Filosofia", "Bianchi")
geografia = Corso("Geografia", "Verdi")

mario = Studente("Mario", "12345")
alessio = Studente("Alessio", "67891")
nino = Studente("Nino", "111213")

geografia.disattiva()

scuola = Scuola("Don Milani")

matematica.aggiungi_studente(mario)
filosofia.aggiungi_studente(alessio)
geografia.aggiungi_studente(nino)

scuola.aggiungi_studente(mario)
scuola.aggiungi_studente(alessio)
scuola.aggiungi_studente(nino)

scuola.aggiungi_corso(matematica)
scuola.aggiungi_corso(filosofia)
scuola.aggiungi_corso(geografia)

scuola.rimuovi_studente_da_corso("111213", geografia)
print(scuola.lista_corsi_attivi())

print(scuola)