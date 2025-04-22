'''Scrivi una funzione che prenda in input una lista di dizionari 
che rappresentano voti di studenti e aggrega i voti per studente 
in un nuovo dizionario.'''

def aggrega_voti(voti:list[dict]) -> dict[str:list[int]]:
    nuovo_dict = {}
    for item in voti:
        nome = item["nome"]
        voto = item["voto"]
        if nome not in nuovo_dict:
            nuovo_dict[nome] = []
        nuovo_dict[nome].append(voto) 
    return nuovo_dict