from abc import ABC, abstractmethod

class ContoBase(ABC):
    def __init__(self, intestatario: str, saldo: float) -> None:
        self.intestatario = intestatario
        self.saldo = saldo 
    
    @property
    def intestatario(self) -> str:
        return self._intestatario 
    
    @intestatario.setter 
    def intestatario(self, intestatario: str) -> None:
        if not isinstance(intestatario, str) or not intestatario.strip():
            raise ValueError("Errore. Input non valido")
        self._intestatario = intestatario 
    
    @property
    def saldo(self) -> float:
        return self._saldo 
    
    @saldo.setter 
    def saldo(self, saldo: float|int) -> None:
        if not isinstance(saldo, (int|float)) or saldo < 0:
            raise ValueError("Errore. Input non valido")
        self._saldo = saldo 
    
    @abstractmethod
    def preleva(self, importo: float) -> None:
        pass 

    def deposita(self, importo: int|float) -> None:
        if not isinstance(importo, (int, float)) or importo <= 0:
            raise ValueError("Errore. Importo non valido")
        self.saldo += importo 
        print("Somma versata")

    @abstractmethod
    def __str__(self) -> str:
        pass
    
class ContoCorrente(ContoBase):    
    def preleva(self, importo: float) -> None:
        if importo > self.saldo:
            raise ValueError("Errore. Saldo insufficiente")
        self.saldo -= importo 
        print("Denaro prelevato")

    def __str__(self) -> str:
        return f"Intestatario: {self.intestatario}\nImporto attuale su conto corrente: {self.saldo:.2f}"
    
class ContoRisparmio(ContoBase):
    def __init__(self, intestatario: str, saldo: float, interesse: float) -> None:
        super().__init__(intestatario, saldo)
        self.interesse = interesse 

    @property
    def interesse(self) -> float:
        return self._interesse 
    
    @interesse.setter 
    def interesse(self, interesse: int|float) -> None:
        if not isinstance(interesse, (int, float)) or interesse < 0:
            raise ValueError("Errore. Interesse inserito non valido")
        self._interesse = interesse 
    
    def preleva(self, importo: float) -> None:
        if importo > self.saldo:
            raise ValueError("Errore. Saldo insufficiente")
        self.saldo -= importo
        print("Denaro prelevato")
    
    def applica_interesse(self, giorni: int) -> float|int:
        if giorni < 0:
            raise ValueError("Giorni non validi")
        interesse_maturato = self.saldo * self.interesse * giorni / 36500
        self.saldo += interesse_maturato
        print(f"Interesse di {interesse_maturato:.2f} applicato")
        return interesse_maturato
    
    def __str__(self) -> str:
        return f"Intestatario: {self.intestatario}\nImporto attuale su conto risparmio: {self.saldo:.2f}"
    
class Banca:
    def __init__(self, nome_banca: str, conti: list = None) -> None:
        self.nome_banca = nome_banca
        self._conti = conti if conti else []

    @property
    def nome_banca(self) -> str:
        return self._nome_banca 
    
    @nome_banca.setter 
    def nome_banca(self, nome_banca: str) -> None:
        if not isinstance(nome_banca, str) or not nome_banca.strip():
            raise ValueError("Errore. Il nome della banca non è valido")
        self._nome_banca = nome_banca
    
    @property
    def conti(self) -> list:
        return self._conti
    
    def aggiungi_conto(self, conto: ContoBase) -> None:
        if not isinstance(conto, ContoBase):
            raise ValueError("Conto non valido")
        self._conti.append(conto)
     
    def mostra_conti(self) -> None:
        if not self._conti:
            print(f"Nessun conto presente")
            return 
        print(f"Conti nella banca: '{self.nome_banca}':\n")
        for conto in self._conti:
            print(conto, "\n")

contocorrente = ContoCorrente("Mario Rossi", 3000)
contorisparmio = ContoRisparmio("Rino Grano", 900, 1.5)
print(contocorrente)
print()
print(contorisparmio)

contocorrente.deposita(90)
contorisparmio.deposita(100)
print(contocorrente)
print()
print(contorisparmio)

contocorrente.preleva(800)
contorisparmio.preleva(90)
print(contocorrente)
print()
print(contorisparmio)
contorisparmio.applica_interesse(5)
print()
bmp = Banca("BMP", [])
bmp.aggiungi_conto(contocorrente)
bmp.aggiungi_conto(contorisparmio)
bmp.mostra_conti()



