'''
Esercizio 13 - Gioco di Carte (Classe Carta)
Tema: Classe con proprietà calcolate e validazioni tramite @property.
Obiettivo: Creare una carta da gioco con valore e seme, con proprietà che calcolano il punteggio e se la carta è alta. 
Traccia:
1. Crea una classe Carta con attributi:
    * valore (numero intero da 1 a 13)
    * seme (stringa: “cuori”, “quadri”, “fiori”, “picche”)
2. Usa @property per:
    * valore → getter e setter con validazione (1-13)
    * seme → getter e setter con validazione (solo i quattro semi validi)
3. Aggiungi proprietà calcolate:
    * punteggio → 10 per 11, 12, 13; altrimenti uguale al valore
    * alta → True se il valore è ≥ 11, False altrimenti
4. Aggiungi __str__ per stampare in modo leggibile la carta:
    Esempio: "Carta: 12 di cuori, punteggio 10, alta: True"
Suggerimento:
* Usa _valore e _seme come attributi interni.
* Le proprietà calcolate (punteggio e alta) devono essere solo getter, senza setter.
'''

class Carta:
    def __init__(self, valore: int, seme: str) -> None:
        self.valore = valore 
        self.seme = seme 

    @property
    def valore(self) -> int:
        return self._valore 
    
    @valore.setter 
    def valore(self, valore: int) -> None:
        if not 1 <= valore <= 13:
            raise ValueError("Errore. La carta deve essere compresa tra 1 e 13")
        self._valore = valore 

    @property 
    def seme(self) -> str:
        return self._seme 
    
    @seme.setter 
    def seme(self, seme: str) -> None:
        if seme not in ["cuori", "quadri", "fiori", "picche"]:
            raise ValueError("Errore. Il seme inserito non è valido")
        self._seme = seme 
    @property
    def punteggio(self) -> int:
        if self.valore >= 11:
            return "Punteggio: 10"
        return f"Punteggio: {self.valore}"

    @property 
    def alta(self) -> bool:
        return self.valore >= 11
    

    def __str__(self) -> str:
        return f"Carta: {self.valore} di {self.seme}, {self.punteggio}, alta: {self.alta}"
    
carta1 = Carta(11, "cuori")
print(carta1)

carta2 = Carta(3, "picche")
print(carta2)

carta2.seme = "spade"
print(carta2)