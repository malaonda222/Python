'''Crea una classe Dado con un attributo facce, che abbia valore predefinito 6.
Richieste:
Scrivi un metodo lancia_dado() che restituisca un numero casuale compreso tra 1 e il 
numero di facce del dado.
Crea un dado a 6 facce e lancialo 10 volte.
Crea anche un dado a 10 facce e uno a 20 facce. Lanciali 10 volte ciascuno.'''

import random

class Dado:
    def __init__(self, facce: int = 6) -> None:
        self.facce = facce 
    
    def lancia_dado(self) -> int:
        return random.randint(1, self.facce) 

dado1 = Dado()
print("Lanci con il dado a 6 facce:")
for _ in range(10):
    print(dado1.lancia_dado())
print()
dado2 = Dado(facce=12)
print("Lanci con il dado da 12:")
for _ in range(10):
    print(dado2.lancia_dado())

