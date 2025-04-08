def somma_elementi(lista_x: list[int], lista_y: list[int]) -> list[int]:

    lista_completa = []

    for item in range(len(lista_x)):
        lista_completa.append(lista_x[item] + lista_y[item])
    
    return lista_completa

print(somma_elementi([1,1,1],[1,1,1]))