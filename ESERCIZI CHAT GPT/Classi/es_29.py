class ContoBancario:
    def __init__(self):
        self.saldo = 0
    
    def deposita(self, importo: float):
        if importo > 0:
            self.saldo += importo 
            print(f"Hai depositato {importo} euro. Il saldo attuale è di {self.saldo} euro.") 
        else:
            print("L'importo da depositare deve essere positivo.")
    
    def preleva(self, importo:float):
        if importo > self.saldo:
            print(f"Fondi insufficienti. Prelievo riuscito.")
        elif importo <= 0:
            print(f"L'importo deve essere positivo.")
        else:
            self.saldo -= importo
            print(f"Prelievo di euro {importo} effettuato. Il saldo attuale è di {self.saldo} euro.")

    def mostra_saldo(self):
        if not self.saldo:
            print("Il saldo è di 0 euro.")
        else:
            print(f"Saldo attuale: {self.saldo} euro.")


conto = ContoBancario()
conto.mostra_saldo()
conto.deposita(100)
conto.deposita(800)
conto.preleva(200)
conto.mostra_saldo()
            
