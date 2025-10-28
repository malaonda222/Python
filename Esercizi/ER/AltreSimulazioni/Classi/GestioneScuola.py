'''Traccia

Scrivi un programma in Python che gestisca le informazioni principali di una scuola.
Crea le seguenti classi:

Persona
- Attributi: nome, cognome, eta
- Metodo: presentazione() → restituisce una stringa con nome completo ed età.

Studente (eredita da Persona)
- Attributi aggiuntivi: matricola, voti (lista di numeri)
Metodi:
- aggiungi_voto(voto)
- media_voti() → restituisce la media dei voti
- presentazione() → sovrascrive quello di Persona aggiungendo la matricola

Docente (eredita da Persona)
- Attributi aggiuntivi: materia
- Metodo: presentazione() → sovrascrive quello di Persona includendo la materia

ClasseScolastica
- Attributi: nome_classe, docente, studenti (lista di oggetti Studente)
Metodi:
- aggiungi_studente(studente)
- rimuovi_studente(matricola)
- media_classe() → restituisce la media complessiva di tutti gli studenti'''

class Persona:
    def __init__(self, nome: str, cognome: str, eta: int) -> None:
        self.nome: str = nome 
        self.cognome: str = cognome 
        self.eta: int = eta 

    def presentazione(self) -> str:
        return f"{self.nome} {self.cognome}, {self.eta} anni"

class Studente(Persona):
    def __init__(self, nome: str, cognome: str, eta: int, matricola: int) -> None:
        super().__init__(nome, cognome, eta)
        self.matricola: int = matricola 
        self.voti: list[int] = []
    
    def aggiungi_voto(self, voto: int) -> None:
        self.voti.append(voto)
    
    def media_voti(self) -> float|None:
        if not self.voti:
            return None 
        else:
            media = sum(self.voti)/len(self.voti)
            return media 
    
    def presentazione(self) -> str:
        return super().presentazione() + f", Matricola {self.matricola}"

class Docente(Persona):
    def __init__(self, nome: str, cognome: str, eta: int, materia: str) -> None:
        super().__init__(nome, cognome, eta)
        self.materia: str = materia 
    
    def presentazione(self) -> str:
        return super().presentazione() + f"Materia {self.materia}"

class ClasseScolastica:
    def __init__(self, nome_classe: str, docente: str) -> None:
        self.nome_classe: str = nome_classe
        self.docente: str = docente 
        self.studenti: list[Studente] = []
    
    def aggiungi_studente(self, studente: Studente) -> None:
        if studente not in self.studenti:
            self.studenti.append(studente)
        else:
            print(f"Studente {studente.nome} {studente.cognome} già presente nella classe")
    
    def rimuovi_studente(self, matricola: int) -> None:
        for studente in self.studenti:
            if studente.matricola == matricola:
                self.studenti.remove(studente)
                return 
        print(f"Nessuno studente con matricola {studente.matricola} presente nella classe")
    
    def media_classe(self) -> float:
        if not self.studenti:
            return 0.0
        voti_validi = [studente.media_voti() for studente in self.studenti]
        if not voti_validi:
            return 0.0 
        else:
            return sum(voti_validi)/len(voti_validi)
