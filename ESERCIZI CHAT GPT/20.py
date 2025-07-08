def rimuovi_duplicati_consecutivi(lista: list) -> list:
    nuova_lista = []
    for i in range(len(lista)):
        if i == 0:
            nuova_lista.append(lista[i])
        if lista[i] != lista[(i - 1)]:
            nuova_lista.append(lista[i])
    return nuova_lista
       

print(rimuovi_duplicati_consecutivi([1,1,2,2,2,3,1,1]))