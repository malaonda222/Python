'''
Esercizio 14 - Studente con Bonus
Tema: Classe avanzata con proprietà calcolate e metodi collegati tra loro.
Obiettivo: Creare una classe StudenteAvanzato che gestisce voti, media, stato promosso e bonus extra.
Traccia:
1. Crea una classe StudenteAvanzato con attributi:
    * nome (stringa non vuota)
    * voti (lista di numeri 0-10)
    * bonus (numero ≥ 0, default 0)
2. Usa @property per:
    * media → calcola la media dei voti + bonus
    * promosso → True se media ≥ 6, altrimenti False
    * ha_bonus → True se bonus > 0
3. Aggiungi metodi per:
    * aggiungi_voto(voto) → aggiunge un voto valido alla lista
    * aggiungi_bonus(punti) → aumenta il bonus se punti ≥ 0
4. Aggiungi __str__ per stampare:
    * Nome, media, promosso e se ha bonus
Suggerimento:
* Usa _nome, _voti, _bonus come attributi interni.
* Tutti i controlli devono sollevare ValueError se i valori non sono validi.
* Le proprietà media, promosso e ha_bonus devono essere solo getter.
'''

class StudenteAvanzato:
    def __init__(self, nome: str, voti: list[int], bonus: int = 0) -> None:
        self.nome = nome 
        self.voti = voti 
        self.bonus = bonus 
    
    @property 
    def nome(self) -> str:
        return self._nome 
    
    @nome.setter 
    def nome(self, nome: str) -> None:
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Errore. Il nome deve essere una stringa o non può essere vuoto")
        self._nome = nome 
    
    @property
    def voti(self) -> list[int]:
        return self._voti 

    @voti.setter 
    def voti(self, voti: list[int]) -> None:
        if not all(isinstance(v, (int, float)) and 0 <= v <= 10 for v in voti):
            raise ValueError("Errore. Il voto deve essere compreso tra 0 e 10")
        self._voti = voti 

    @property
    def bonus(self) -> int:
        return self._bonus
    
    @bonus.setter 
    def bonus(self, bonus: int) -> int:
        if not isinstance(bonus, (int, float)) or bonus < 0:
            raise ValueError("Errore. Il bonus non può essere inferiore a 0")
        self._bonus = bonus 
    
    @property
    def media(self) -> float:
        if not self.voti:
            return float(self.bonus)
        return (sum(self.voti) + self.bonus) / (len(self.voti)+1)

    @property
    def promosso(self) -> bool:
        return self.media >= 6
    
    @property 
    def ha_bonus(self) -> bool:
        return self.bonus > 0
    
    def aggiungi_voto(self, voto: int) -> None:
        if not isinstance(voto, (int|float)) or not 0 <= voto <= 10:
            raise ValueError("Voto inserito non valido")
        return self.voti.append(voto)
    
    def aggiungi_bonus(self, punti: int) -> None:
        if not isinstance(punti, (int, float)) or punti < 0:
            raise ValueError("Errore. Punti non validi")
        self.bonus += punti 

    def __str__(self) -> str:
        return f"Nome: {self.nome}\nMedia: {self.media}\nPromosso: {self.promosso}\nBonus: {self.bonus}"

studente1 = StudenteAvanzato("Arianna", [10, 4, 6])
print(studente1)
print()
studente1.aggiungi_bonus(10)
print(studente1.media)
print(studente1)
studente1.aggiungi_voto(8)
print(studente1)
