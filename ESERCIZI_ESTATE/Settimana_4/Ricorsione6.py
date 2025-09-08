def potenza(base: int, esponente: int) -> int:
    if base == 0 and esponente == 0:
        raise ValueError('0 elevato alla 0 è indefinito')
    if esponente == 0:
        return 1
    if base == 0:
        return 0
    else:
        return base * potenza(base, esponente - 1)
    
print(potenza(2, 3))