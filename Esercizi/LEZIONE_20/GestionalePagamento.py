from datetime import datetime

class Pagamento:
    def __init__(self) -> None:    
        self.__importo = 0.0

    def setImporto(self, importo: float) -> None:
        if not isinstance(importo, (int, float)) or importo < 0:
            raise ValueError("Importo inserito non valido.")
        else:
            self.__importo = float(importo) 
    
    def getImporto(self) -> float:
        return self.__importo 
    
    def dettagliPagamento(self) -> None:
        print(f"Importo del pagamento: €{self.__importo:.2f}")


class PagamentoContanti(Pagamento):
    def dettagliPagamento(self) -> str:
        super().dettagliPagamento()
        print("Pagamento in contanti")
    
    def inPezziDa(self):
        importo = self.getImporto()
        pezzi = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.01]
        conteggio = {}
        for pezzo in pezzi:
            if importo >= pezzo:
                conteggio[pezzo] = importo // pezzo # numero di pezzi di questo taglio
                print(f"{conteggio[pezzo]} pezzi da €{pezzo:.2f}")
                importo = round(importo - conteggio[pezzo] * pezzo, 2) # aggiorn l'importo rimanente da pagare
            else:
                conteggio[pezzo] = 0
        
        lista_dict = []
        for key, value in conteggio.items():
            if value == 0.0:
                continue
            else:
                lista_dict.append({key: value})
        return lista_dict


class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, titolare_carta: str, data_scadenza: str, numero_carta: str) -> None:
        super().__init__()
        self.setTitolareCarta(titolare_carta)
        self.setDataScadenza(data_scadenza)
        self.setNumeroCarta(numero_carta)

    def setTitolareCarta(self, titolare_carta: str) -> None:
        if not isinstance(titolare_carta, str) or titolare_carta.strip() == "":
            raise ValueError("Errore. Titolare carta non valido")
        else:
            self.titolare_carta = titolare_carta
    
    def setDataScadenza(self, data_scadenza: str) -> None:
        if not isinstance(data_scadenza, str):
            raise ValueError("Data inserita non valida")
        else:
            self.data_scadenza = data_scadenza

    def setNumeroCarta(self, numero_carta: int) -> None:
        if not isinstance(numero_carta, int):
            raise ValueError("Numero carta non valido")
        else:
            self.numero_carta = numero_carta
        
    def getTitolareCarta(self) -> str:
        return self.titolare_carta
    
    def getDataScadenza(self) -> datetime:
        return self.data_scadenza

    def getNumeroCarta(self) -> int:
        return self.numero_carta

    def dettagliPagamento(self):
        super().dettagliPagamento()
        print("Pagamento con carta di credito")
        print(f"Titolare carta: {self.getTitolareCarta()}\n"\
              f"Data scadenza: {self.getDataScadenza()}\n"\
                f"Numero carta: {self.getNumeroCarta()}")



if __name__ == '__main__':
    pagamento_in_contanti1 = PagamentoContanti()
    pagamento_in_contanti1.setImporto(229)
    pagamento_in_contanti1.dettagliPagamento()
    print(pagamento_in_contanti1.inPezziDa())
    print()
    pagamento_in_contanti2 = PagamentoContanti()
    pagamento_in_contanti2.setImporto(11)
    pagamento_in_contanti2.dettagliPagamento()
    print(pagamento_in_contanti2.inPezziDa())
    print()
    pagamento_carta1 = PagamentoCartaDiCredito("Mario Rossi", "01/23", 65432107654321)
    pagamento_carta1.setImporto(92.09)
    pagamento_carta1.dettagliPagamento()
    print()
    pagamento_carta2 = PagamentoCartaDiCredito("Luigi Bianchi", "12/24", 1234567890123456)
    pagamento_carta2.setImporto(45.29)
    pagamento_carta2.dettagliPagamento()