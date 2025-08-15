'''Scrivi una funzione chiamata voto_medio_sotto che, data una lista di studenti (ognuno rappresentato da un dizionario con chiavi "nome" e 
"voti" — lista di numeri) e una soglia numerica, ritorni un dizionario che associa a ogni studente la media dei voti strettamente inferiori alla soglia.

Se uno studente non ha voti inferiori alla soglia, il valore associato sarà None.'''


def voto_medio_sotto(studenti: list[dict[str, list[int]]], soglia: int) -> dict[str, float] | None:
    new_dizionario = {}
    for studente in studenti:
        nome = studente["nome"]
        voti = studente["voti"]
        lista_inferiori = []
        for voto in voti:
            if voto < soglia:
                lista_inferiori.append(voto)
        if lista_inferiori:
            media = sum(lista_inferiori)/(len(lista_inferiori))
            new_dizionario[nome] = media 
        else:
            new_dizionario[nome] = None 

    return new_dizionario