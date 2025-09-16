'''
Esercizio 11 - Conto Bancario
Tema: Gestione di dati sensibili con proprietà.
Obiettivo: Creare una classe che rappresenti un conto bancario con controllo sugli accessi e sulle operazioni.
Traccia:
1. Crea una classe ContoBancario con gli attributi:
    * titolare (stringa, non vuota)
    * saldo (float o int, inizialmente ≥ 0)
2. Usa @property per gestire saldo, impedendo valori negativi.
3. Implementa i metodi:
    * deposita(importo) → aumenta il saldo se l’importo è positivo.
    * preleva(importo) → diminuisce il saldo se l’importo è valido e non superiore al saldo disponibile.
4. Aggiungi il metodo __str__ che mostra il nome del titolare e il saldo corrente.
Suggerimento: nel setter di saldo, assicurati che non possa mai andare sotto zero.
'''

class ContoBancario:
    def __init__(self, titolare: str, saldo: int|float) -> None:
        self.titolare = titolare 
        self.saldo = saldo

    @property
    def saldo(self) -> int|float:
        return self._saldo 
    
    @saldo.setter 
    def saldo(self, saldo: int|float) -> None:
        if saldo < 0: 
            raise ValueError("Errore.")
        self._saldo = saldo 

    @property
    def titolare(self) -> str:
        return self._titolare
    
    @titolare.setter 
    def titolare(self, titolare: str) -> None:
        if not titolare.strip():
            raise ValueError("Errore.")
        self._titolare = titolare

    def deposita(self, importo: int|float) -> int|float:
        if importo <= 0:
            raise ValueError("Errore. Importo deve essere positivo")
        self.saldo += importo 
  
    def preleva(self, importo: float|int) -> None:
        if importo <= 0:
            raise ValueError("Errore. Importo deve essere positivo")
        if importo > self.saldo:
            raise ValueError("Errore. Saldo insufficiente")
        self.saldo -= importo 
        
    def __str__(self) -> str:
        return f"Titolare: {self.titolare}\nSaldo: {self.saldo}"
    

conto = ContoBancario("Gianni", 800)
conto.deposita(100)
conto.preleva(80)
print(conto)