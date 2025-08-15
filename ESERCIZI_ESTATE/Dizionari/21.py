'''La funzione si chiamerà ad esempio voto_minimo_sopra_con_conteggio e dovrà, per ogni studente:
    Trovare i voti ≥ soglia
    Se ce ne sono:
        Restituire una tupla: (voto_minimo, numero_voti_superiori_o_uguali)
    Altrimenti:
        Restituire None'''

def voto_minimo_sopra_con_conteggio(studenti: list[dict[str, list[int]]], soglia: int) -> dict[str, tuple[int, int]] | None:
    new_dict = {}
    for studente in studenti:
        nome = studente["nome"]
        voti = studente["voti"]
        lista_voti_superiori = [voto for voto in voti if voto >= soglia]
        if lista_voti_superiori:
            voto_minimo = min(lista_voti_superiori)
            numero_voti_superiori_o_uguali = len(lista_voti_superiori)
            new_dict[nome] = (voto_minimo, numero_voti_superiori_o_uguali)
        else:
            new_dict[nome] = None 
    return new_dict



studenti = [
    {"nome": "Luca", "voti": [22, 19, 30]},      # ≥18 → [22, 19, 30] → min=19, len=3
    {"nome": "Anna", "voti": [15, 18, 17]},      # ≥18 → [18]         → min=18, len=1
    {"nome": "Sara", "voti": [20, 21, 19]},      # ≥18 → [20,21,19]   → min=19, len=3
]

print(voto_minimo_sopra_con_conteggio(studenti, 20))