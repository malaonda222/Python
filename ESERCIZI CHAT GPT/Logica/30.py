'''Scrivi una funzione analizza_voti(voti: list[int]) -> dict che:
    Riceve una lista di voti interi (da 0 a 30)
    Restituisce un dizionario con:
        "media": la media dei voti
        "minimo": il voto più basso
        "massimo": il voto più alto
        "promossi": numero di voti ≥ 18
        "bocciati": numero di voti < 18'''

def analizza_voti() -> dict:
    lista_numeri = []
    new_dict = {}
    i = 1
    while i <= 5:
        voto: int = int(input(f"Inserisci il {i}° numero: "))
        if voto < 0 or voto > 30:
            raise ValueError("Errore. Il numero deve essere compreso tra 0 e 30")
        else:
            lista_numeri.append(voto)
        i += 1
    print(lista_numeri)

    new_dict = {
        "media": round(sum(lista_numeri) / len(lista_numeri), 2),
        "minimo": min(lista_numeri),
        "massimo": max(lista_numeri),
        "promossi": len([i for i in lista_numeri if i >= 18]),
        "bocciati": len([i for i in lista_numeri if i < 18])
        }
    
    return new_dict



print(analizza_voti())