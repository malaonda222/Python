from __future__ import annotations
import datetime 


'''ESERCIZIO 1: class Studente 
Obiettivo: creare una classe per rappresentare uno studente con nome e voti.
Traccia:
    Crea una classe chiamata Studente.
    Ogni studente ha:
        un attributo nome
        un attributo voti (lista di interi)
    Aggiungi un metodo aggiungi_voto(voto) per aggiungere un voto alla lista.
    Aggiungi un metodo media() che restituisce la media dei voti o None se non ce ne sono.
    Aggiungi un metodo voto_massimo() che restituisce il voto più alto o None se non ce ne sono.'''


class Studente:
    def __init__(self, nome: str) -> None:
        self.set_nome(nome)
        self.voti = []
        self.lista_esami = []
    
    def set_nome(self, nome: str) -> None:
        if not isinstance(nome, str):
            raise ValueError("Il nome deve essere una stringa")
        self.nome = nome 
    
    def get_nome(self) -> str:
        return self.nome 
    
    def get_voti(self) -> list[int]:
        return self.voti 
    
    def aggiungi_voto(self, voto: int) -> None:
        if not isinstance(voto, int) or voto > 30 or voto < 18:
            raise ValueError("Errore. Inserire un numero valido")
        self.voti.append(voto)

    def aggiungi_esame(self, esame: Esame) -> None:
        self.lista_esami.append(esame)
    
    def media(self) -> float | None:
        if not self.voti:
            return None
        else:
            media = sum(self.voti)/len(self.voti)
            return f"Media: {media}"
        
    def media_esami(self) -> float | None:
        if not self.lista_esami:
            return None
        punteggi = [esame.punteggio for esame in self.lista_esami]
        return sum(punteggi)/len(punteggi)
    
    def voto_massimo(self) -> int | None:
        if not self.voti:
            return None
        else:
            massimo = max(self.voti)
            return f"Numero massimo: {massimo}"

'''ESERCIZIO 2: class Registro Studenti
Obiettivo: usare più oggetti Studente dentro una classe Registro.
Traccia:
    Crea una classe Registro che contiene una lista di oggetti Studente.
    Aggiungi un metodo aggiungi_studente(studente) per aggiungere uno studente.
    Aggiungi un metodo media_classe() che calcola la media di tutti i voti di tutti gli studenti.
    Aggiungi un metodo top_studente() che restituisce lo studente con la media più alta.'''

class Registro:
    def __init__(self) -> None:
        self.lista_studenti = []
    
    def aggiungi_studente(self, studente: Studente) -> None:
        self.lista_studenti.append(studente) 

    def media_classe(self) -> float | None:
        medie_totali = []
        for studente in self.lista_studenti:
            voti = studente.voti
            if voti:
                media_studente = sum(voti)/len(voti)
                medie_totali.append(media_studente)
        if not medie_totali:
            return None
        return sum(medie_totali)/len(medie_totali)
    
    def top_studente(self) -> str | None:
        migliore = None
        media_massima = -1
        for studente in self.lista_studenti:
            voti = studente.voti
            if voti: 
                media = sum(voti)/len(voti)
                if media > media_massima:
                    media_massima = media 
                    migliore = studente.nome
        return migliore


'''ESERCIZIO 3: class Esame
Traccia:
    Crea una classe Esame con:
        nome_esame
        data
        punteggio
    Fai in modo che la classe Studente tenga una lista di esami.
    Aggiungi un metodo media_esami() per calcolare la media dei punteggi.'''

class Esame: 
    def __init__(self, nome_esame: str, data: datetime, punteggio: int) -> None:
        self.nome_esame = nome_esame
        self.data = data 
        self.punteggio = punteggio 
    
    

studente1: Studente = Studente("Lisa")
studente1.aggiungi_voto(18)
studente1.aggiungi_voto(25)
studente1.aggiungi_voto(28)
studente1.aggiungi_voto(30)
studente1.aggiungi_voto(22)
studente2: Studente = Studente("Giorgio")
studente2.aggiungi_voto(29)
studente2.aggiungi_voto(23)
studente2.aggiungi_voto(21)
studente2.aggiungi_voto(18)
studente2.aggiungi_voto(18)

print(studente1.media())
print(studente1.voto_massimo())
registro: Registro = Registro()
registro.aggiungi_studente(studente1)
registro.aggiungi_studente(studente2)
print(registro.media_classe())
print(registro.top_studente())
esame1: Esame = Esame("Matematica", "2022-06-10", 28)
esame2: Esame = Esame("Informatica", "2021-08-12", 21)
print(studente1.aggiungi_esame(esame1))
print(studente1.aggiungi_esame(esame2))
print(studente1.media_esami())


