def somma_elementi(lista_x: list[int], lista_y: list[int]) -> list[int]:

    lista_completa = []

    for item in range(len(lista_x)):
        lista_completa.append(lista_x[item] + lista_y[item])
    
    return lista_completa

print(somma_elementi([1,1,1],[1,1,1]))


def somma_elementi(x:list[int], y:list[int]) -> list[int]:
    """Restituisce una lista risultante dalla somma elemento per elemento delle due liste x e y.
    Si assume che le due liste abbiano la stessa lunghezza."""
    result:list[int] = []
    for i in range(len(x)):
        result.append(x[i] + y[i])  # Somma i valori corrispondenti e li aggiunge alla lista risultato
    return result
