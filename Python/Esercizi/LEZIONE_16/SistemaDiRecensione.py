class Media:
    def __init__(self, title: str, reviews: list[int] = None) -> None:
        self.title = title 
        if reviews is not None:
            self.reviews = reviews
        else:
            self.reviews = list()
    
    def set_title(self, title: str) -> None:
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Il titolo deve essere una stringa non vuota.")
        self.title = title 
    
    def get_title(self) -> str:
        return self.title 
    
    def aggiungiValutazione(self, voto: int) -> None:
        if isinstance(voto, int) and 1 <= voto <= 5:
            self.reviews.append(voto)
        else:
            raise ValueError("Il voto inserito non è valido.")
        
    def getMedia(self) -> float:
        if not self.reviews:
            return 0.0
        somma_recensioni = sum(self.reviews)
        voto_media = somma_recensioni / len(self.reviews)
        return voto_media
        
    def getRate(self) -> str:
        if not self.reviews:
            return "Nessuna valutazione disponibile."

        media_arrotondata = round(self.getMedia())

        match media_arrotondata:
            case 1:
                return "Terribile"
            case 2:
                return "Brutto"
            case 3:
                return "Normale"
            case 4:
                return "Bello"
            case 5:
                return "Grandioso"
            case _:
                return "Valutazione sconosciuta"

    def ratePercentage(self, voto: int) -> float:
        if not self.reviews:
            return 0.0
        if voto < 1 or voto > 5:
            raise ValueError("Il voto deve essere tra 1 e 5")
        cont_voto = 0
        for element in self.reviews:
            if element == voto:
                cont_voto += 1
        percentuale = ((cont_voto / len(self.reviews)) * 100)
        return f"{percentuale:.2f}"

    def recensione(self) -> None:
        print(f"Titolo del film: {self.get_title()}")
        print(f"Voto Medio: {self.getMedia()}")
        print(f"Giudizio: {self.getRate()}")
        print(f"Terribile: {self.ratePercentage(1)}%")
        print(f"Terribile: {self.ratePercentage(2)}%")
        print(f"Terribile: {self.ratePercentage(3)}%")
        print(f"Terribile: {self.ratePercentage(4)}%")
        print(f"Terribile: {self.ratePercentage(5)}%")


class Film(Media):
    def __init__(self, title: str) -> None:
        super().__init__(title) 
    
    def __str__(self) -> str:
        return f"Il film scelto è '{self.title}'"


if __name__ == "__main__":
    f1 = Film("Titanic")
    f1.aggiungiValutazione(5)
    f1.aggiungiValutazione(3)
    f1.aggiungiValutazione(4)
    f1.aggiungiValutazione(2)
    f1.aggiungiValutazione(1)
    f1.aggiungiValutazione(1)
    f1.aggiungiValutazione(1)
    print(f1)
    f1.recensione()

    print()

    f2 = Film("One Day")
    f2.aggiungiValutazione(3)
    f2.aggiungiValutazione(4)
    f2.aggiungiValutazione(2)
    f2.aggiungiValutazione(4)
    f2.aggiungiValutazione(3)
    f2.aggiungiValutazione(2)
    f2.aggiungiValutazione(5)
    print(f2)
    f2.recensione()

    print()
    print(f2.ratePercentage(4))
    print(f1.ratePercentage(3))