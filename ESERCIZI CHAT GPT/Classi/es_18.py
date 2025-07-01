'''
Classe Auto
Classe Auto con:
Attributi: marca, modello, anno
Metodo: scheda() che stampa:
"Auto: Fiat Panda (2010)"
'''

'''
Esercizio: Gestione di una lista di auto
Obiettivo:
Crea 3 oggetti Auto con marche, modelli e anni diversi.
Inseriscili in una lista chiamata parco_auto.
Scorri la lista e stampa le schede di tutte le auto usando un ciclo.
'''

class Auto:
    def __init__(self, marca:str, modello:str, anno:int):
        self.marca = marca 
        self.modello = modello 
        self.anno = anno
    
    def scheda(self):
        print(f"Auto: {self.marca} {self.modello} ({self.anno})")
    
    
auto1 = Auto("Fiat", "Panda", 2010)
# auto1.scheda()

auto2 = Auto("Mercedes", "CD1", 2020)
# auto2.scheda()

auto3 = Auto("Kia", "Rio", 2006)
# auto3.scheda()

parco_auto = [auto1, auto2, auto3]
for auto in parco_auto:
    auto.scheda()


