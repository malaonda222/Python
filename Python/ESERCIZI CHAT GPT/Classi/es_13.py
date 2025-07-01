class CercatorediTesori:
    def __init__(self, mappa_tesoro:str):
        self.mappa_tesoro = mappa_tesoro
        
    def cerca_tesoro(self, posizione:int):
        if self.mappa_tesoro[posizione] == "X":
            return f"Tesoro trovato nella posizione {posizione}!"
        else:
            return f"Nessun tesoro trovato nella posizione {posizione}."

    def cerca_multipli_tesori(self):
        posizioni_tesori = []
        for i in range(len(self.mappa)):
            if self.mappa_tesori[i]:
                posizioni_tesori.append(i)
        return posizioni_tesori
    
    def aggiungi_tesoro(self, posizione):
        if self.mappa[posizione] != "X":
            self.mappa[posizione] = "X"
            return f"Tesoro aggiunto nella posizione {posizione}."
        else:
            return f"Un tesoro è già presente nella posizione {posizione}."



# test della classe CercatoreDiTesori  
cercatore = CercatorediTesori([0, 0, "X", "X", 0, 0])

# cercare un tesoro in una posizione
print(cercatore.cerca_tesoro(2))
print(cercatore.cerca_tesoro(2))

# cercare tutti le posizioni con i tesori
print(cercatore.cerca_multipli_tesori())

# aggiungere un tesoro in una posizione
print(cercatore.aggiungi_tesoro(5))
print(cercatore.mappa)

# tentare di aggiungere un tesoro in una posizione già occupata
print(cercatore.aggiungi_tesoro(2))