class Frazione:
    def __init__(self, numeratore: int, denominatore: int) -> None:
        self.set_numeratore(numeratore) 
        self.set_denominatore(denominatore)
    
    def set_numeratore(self, numeratore: int) -> None:

        if isinstance(numeratore, int):
            self.__numeratore = numeratore
        else:
            self.__numeratore = 13
    
    def set_denominatore(self, denominatore: int) -> None:
        if isinstance(denominatore, int) and denominatore != 0:
            self.__denominatore = denominatore
        else:
            self.__denominatore = 5
    
    def get_numeratore(self) -> int:
        return self.__numeratore 

    def get_denominatore(self) -> int:
        return self.__denominatore
    
    def __str__(self) -> str:
        return f"{self.get_numeratore() }/ {self.get_denominatore()}"
    
    def value(self) -> float:
        divisione = self.get_numeratore() / self.get_denominatore()
        return round(divisione, 3)


def mcd(x: int, y: int) -> int:
    max_divisor = 1
   
    #supponiamo x > y
    end: int = x

    #se y > x, modifichiamo il valore di end
    if y > x:
        end = y 
    
    # troviamo i divisori comuni, ovvero i valori di i per cui la divisione x/i e la divisione di y/i danno entrambe resto 0 
    for i in range(1, end+1):
        if x % i == 0 and y % i == 0:
            if i > max_divisor:
                max_divisor = i 
    return max_divisor 

    
def semplifica(l: list[Frazione]) -> list:
    lista_semplificata = []
    for frazione in l:
        num = frazione.get_numeratore()
        den = frazione.get_denominatore()
        divisore = mcd(num, den)
        if divisore == 1:
            lista_semplificata.append(frazione)
        else:
            num_semplificato = num // divisore 
            den_semplificato = den // divisore 
            lista_semplificata.append(Frazione(num_semplificato, den_semplificato))
    return lista_semplificata
    

def fractionCompare(l: list[Frazione], lista_semplificata: list[Frazione]):
    for i in range(len(l)):
        print(f"Frazione originale: {l[i].value()} --- Valore frazione ridotta: {lista_semplificata[i].value()}")

if __name__ == "__main__":
    l = [
        Frazione(2.5, 0),
        Frazione(1, 2), 
        Frazione(2, 4),
        Frazione(3, 5),
        Frazione(6, 9),
        Frazione(4, 7),
        Frazione(24, 36),
        Frazione(12, 36), 
        Frazione(40, 60),
        Frazione(5, 11),
        Frazione(10, 45),
        Frazione(42, 78),
        Frazione(9, 15)
        ]

    l_s = semplifica(l)
    print(*l_s, sep = "\n")
    fractionCompare(l, l_s)