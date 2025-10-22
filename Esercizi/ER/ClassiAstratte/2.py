'''Esercizio 2 - Interfaccia di pagamento
Obiettivo: Capire come le classi astratte possano definire interfacce comuni per oggetti diversi.
Nome dell’esercizio: MetodoPagamento
Traccia:
Crea una classe astratta MetodoPagamento con:
un metodo astratto paga(importo)
Crea due sottoclassi:
CartaCredito → stampa "Pagato {importo}€ con carta di credito."
PayPal → stampa "Pagato {importo}€ con PayPal."
Crea una funzione elabora_pagamento(metodo, importo) che accetti un’istanza di MetodoPagamento e chiami paga() su di essa.
Testa la funzione con entrambe le classi.
Suggerimento: controlla con isinstance() che il metodo passato sia una sottoclasse valida.'''

from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    @abstractmethod
    def paga(self, importo: float) -> float:
        pass 

class CartaCredito(MetodoPagamento):
    def paga(self, importo: float) -> None:
        print(f"Pagato € {importo} con carta di credito.")

class PayPal(MetodoPagamento):
    def paga(self, importo: float) -> None:
        print(f"Pagato € {importo} con PayPal.")


def elabora_pagamento(metodo: MetodoPagamento, importo: float):
    if not isinstance(metodo, MetodoPagamento):
        raise ValueError("Errore. Metodo di pagamento non valido.")
    else:
        return metodo.paga(importo)


elabora_pagamento(CartaCredito(), 100.30)
elabora_pagamento(PayPal(), 340.70)