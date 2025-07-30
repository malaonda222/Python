'''Traccia:
Scrivi una funzione estrai_promossi(studenti: dict, soglia: int = 21) -> list[str] che restituisce 
una lista di nomi di studenti che hanno superato la soglia in tutte le materie.'''

def promossi(studenti: dict[str, dict[str, int]], soglia: int = 21) -> list[str]:
    lista_promossi = []
    for nome_studente, materie in studenti.items():
        if all(voto > soglia for voto in materie.values()):
            lista_promossi.append(nome_studente)
    return lista_promossi


studenti = {
    "Anna": {"matematica": 28, "storia": 30},
    "Luca": {"matematica": 18, "storia": 24},
    "Marta": {"matematica": 22, "storia": 19},
}

print(promossi(studenti))


def promosso(students: dict[str, dict[str, int]], target: int = 21) -> list[str]:
    lista_promosso = []
    for nome_studente, materie in students.items():
        promosso = True 
        for voto in materie.values():
            if voto <= target:
                promosso = False 
                break
        if promosso:
            lista_promosso.append(nome_studente)
    return lista_promosso


students = {
    "Giuseppe": {"tedesco": 30, "arte": 30},
    "Luca": {"tedesco": 18, "arte": 20},
    "Marta": {"tedesco": 21, "arte": 30},
}

print(promosso(students))



def estrai_promossi(stud: dict[str, dict[str, int]], sogl: int = 21) -> list[str]:
    lista_promossi = [] 
    for nome_studente, materie in stud.items():
        promosso = True
        for voto in materie.values():
            if voto <= sogl:
                promosso = False 
                break
        if promosso:
            lista_promossi.append(nome_studente)
    return lista_promossi



stud = {
    "Giuseppe": {"tedesco": 30, "arte": 30},
    "Luca": {"tedesco": 18, "arte": 20},
    "Marta": {"tedesco": 21, "arte": 30},
}

print(estrai_promossi(stud))