'''Crea una classe MacchinaLotteria che contenga un insieme di numeri e lettere.
Richieste:
Inizializza un attributo pool contenente 10 numeri (da 0 a 9) e 5 lettere (es. da 'A' a 'E').
Implementa un metodo estrai_biglietto() che seleziona 4 elementi casuali dal pool e li 
restituisce come lista.
Implementa un metodo mostra_biglietto_vincente() che stampa un messaggio con il biglietto 
vincente.'''

import random
from string import ascii_uppercase

class MacchinaLotteria:
    def __init__(self) -> None:
        numeri = [str(num) for num in range(10)]
        lettere = list(ascii_uppercase[:5])
        self.pool = numeri + lettere
    
    def estrai_biglietto(self):
        biglietto = random.sample(self.pool, 4)
        print(f"Biglietto estratto: {biglietto}")
        return biglietto
    
    def mostra_biglietto_vincente(self):
        biglietto_vincente = random.sample(self.pool, 4)
        print(f"Biglietto vincente: {biglietto_vincente}")
        return biglietto_vincente
    
    def simula_fino_a_vittoria(self, mio_biglietto: list[str]):
        tentativi = 0
        while True:
            biglietto = random.sample(self.pool, 4)
            tentativi += 1
            if biglietto == mio_biglietto:
                break
        return tentativi, biglietto

    
lotteria = MacchinaLotteria()
estratto = lotteria.estrai_biglietto()
vincente = lotteria.mostra_biglietto_vincente()

mio_biglietto = random.sample(lotteria.pool, 4)
tentativi, biglietto_vincente = lotteria.simula_fino_a_vittoria(mio_biglietto)

print(f"Il tuo biglietto: {mio_biglietto}")
print(f"Biglietto vincente: {biglietto_vincente}")
print(f"Tentativi: {tentativi}")