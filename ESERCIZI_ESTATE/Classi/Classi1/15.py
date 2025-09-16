'''
Esercizio 15 - Giocatore di Basket
Tema: Classe con più proprietà collegate e calcoli dinamici.
Obiettivo: Implementare una piccola classe “Giocatore” con statistiche e bonus che influenzano altri valori.
Traccia:
1. Crea una classe Giocatore con attributi: nome (str), punti (list[int]), bonus (int).
2. Validare: punti devono essere numeri interi ≥ 0; bonus ≥ 0.
3. Proprietà media_punti → media dei punti + bonus.
4. Proprietà top_scorer → True se media_punti >= 20, altrimenti False.
5. Metodo aggiungi_punti(punti: int) → aggiunge un punteggio alla lista, controllando la validità.
6. Metodo aggiungi_bonus(punti: int) → incrementa il bonus.
7. __str__ → restituisce nome, media_punti, top_scorer e bonus.
* Suggerimento: Usa _punti e _bonus come attributi privati e proprietà per validare i valori.
'''

class Giocatore:
    def __init__(self, nome: str, punti: list[int], bonus: int) -> None:
        self.nome = nome 
        self.punti = punti 
        self.bonus = bonus 

    @property
    def nome(self) -> str:
        return self._nome 
    
    @nome.setter 
    def nome(self, nome: str) -> None:
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Errore. Il nome inserito non è valido")
        self._nome = nome 

    @property
    def punti(self) -> list[int]:
        return self._punti 
    
    @punti.setter 
    def punti(self, punti: list[int]) -> None:
        if not isinstance(punti, (list) or not all(isinstance(p, int) and p >= 0 for p in punti)):
            raise ValueError("Errore. I voti inseriti devono essere numeri validi maggiori o uguali a 0")
        self._punti = punti 
    
    @property 
    def bonus(self) -> int:
        return self._bonus 

    @bonus.setter 
    def bonus(self, bonus: int) -> None:
        if not isinstance(bonus, int) or bonus < 0:
            raise ValueError("Errore. Il bonus deve essere un numero intero maggiore o uguale a 0")
        self._bonus = bonus 
    
    @property
    def media(self) -> float:
        if not self.punti:
            return float(self.bonus) 
        else:
            return (sum(self.punti) + self.bonus) / (len(self.punti) + 1)
    
    @property
    def top_scorer(self) -> bool:
        return self.media >= 20
    
    def aggiungi_punti(self, punti: int) -> None:
        if not isinstance(punti, int) or punti < 0:
            raise ValueError("Errore. Punti inseriti non validi")
        self.punti.append(punti)
    
    def aggiungi_bonus(self, punti: int) -> None:
        if not isinstance(punti, int) or punti < 0:
            raise ValueError("Errore. Bonus inserito non valido")
        self.bonus += punti 

    def __str__(self) -> str:
        return f"Nome: {self.nome}\nMedia: {self.media}\nTop scorer: {self.top_scorer}\nBonus: {self.bonus}"
    

atleta1 = Giocatore("Marco", [70, 2], 10)
print(atleta1)
print()
atleta1.aggiungi_bonus(10)
print(atleta1)
atleta1.aggiungi_punti(5)
print(atleta1)
print()
atleta2 = Giocatore("Giacomo", [2, 5, 10], 5)
print(atleta2)
