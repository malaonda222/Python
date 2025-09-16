'''
Esercizio 12 - Studente con media e promozione
Tema: Attributi calcolati dinamicamente e validazioni con @property.
Obiettivo: Creare una classe Studente che gestisca voti e calcoli automatici della media e 
dello stato di promozione. 
Traccia:
1. Crea una classe Studente con gli attributi:
    * nome (stringa non vuota)
    * voti (lista di numeri da 0 a 10)
2. Usa @property per:
    * media → calcola la media dei voti
    * promosso → restituisce True se la media ≥ 6, altrimenti False
3. Gestisci i setter in modo che: 
    * nome non possa essere vuoto
    * i voti inseriti siano numeri validi tra 0 e 10
4. Aggiungi __str__ per stampare: 
    * nome, voti, media e se lo studente è promosso o bocciato
Suggerimento:
* La proprietà media non ha bisogno di setter, perché è calcolata automaticamente dai voti.
* La proprietà promosso dipende dalla media e quindi può essere solo getter.
'''

class Studente:
    def __init__(self, nome: str, voti: list[int]) -> None:
        self.nome = nome 
        self.voti = voti 
    
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
    def media(self) -> float:
        if not self.voti:
            return 0.0
        return sum(self.voti) / len(self.voti)

    @property
    def promosso(self) -> bool:
        return self.media <= 6
    
    def __str__(self) -> str:
        stato = "promosso" if self.promosso else "bocciato"
        return f"Nome: {self.nome}\nVoti: {self.voti}\nMedia: {self.media}\nStato: {stato}"

studente = Studente("Luisa", [10, 4, 6])
print(studente)

studente1 = Studente("Mario", [6, 6, 6])
print(studente1)