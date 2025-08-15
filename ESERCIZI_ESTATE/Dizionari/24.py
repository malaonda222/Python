'''Nome dell’esercizio: studenti_senza_voti_sotto
 
Traccia:
Scrivi una funzione chiamata studenti_senza_voti_sotto che, 
data una lista di studenti e una soglia numerica, ritorni una 
lista con i nomi degli studenti per i quali tutti i voti sono maggiori o uguali alla soglia.'''


def studenti_senza_voti_sotto(students: list[dict[str, int]], soglia: int) -> list[str]:
    new_list = []
    for studente in students:
        for voto in studente["voti"]:
            if voto >= soglia:
                if studente not in new_list:
                    new_list.append(studente["nome"])
                    break
    return new_list  

def studenti_senza_voti_sotto(students: list[dict[str, int]], soglia: int) -> list[str]:
    return [studente["nome"] for studente in students if all(voto >= 18 for voto in studente["voti"])]      



studenti = [{"nome": "Anna", "voti": [15, 18, 22, 10]},
{"nome": "Luca", "voti": [20, 17, 19, 13]},
{"nome": "Sara", "voti": [12, 16, 14]}
]
print(studenti_senza_voti_sotto(studenti, 18))
