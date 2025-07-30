'''Hai un dizionario che rappresenta gli studenti e i loro voti in varie 
materie. Scrivi una funzione che restituisce, per ogni materia, il nome 
dello studente con il voto più alto.'''

def migliori_per_materia(studenti: dict[str, dict[str, int]]) -> dict[str, str]:
    valori_massimi = {}
    for nome_studente, materie in studenti.items():
        for materia, voto in materie.items():
            if materia not in valori_massimi or voto > valori_massimi[materia][1]:
                valori_massimi[materia] = (nome_studente, voto)

    risultati = {materia: nome_studente for materia, (nome_studente, voto) in valori_massimi.items()}
    return risultati
        


studenti = {
    "Anna": {"matematica": 28, "storia": 30, "inglese": 25},
    "Luca": {"matematica": 30, "storia": 27, "inglese": 29},
    "Marta": {"matematica": 26, "storia": 30, "inglese": 30},
}

print(migliori_per_materia(studenti))




def voto_migliore(students: dict[str, dict[str, int]]) -> dict[str, str]:
    voto_massimo = {}
    for studente, materie in students.items():
        for materia, voto in materie.items():
            if materia not in voto_massimo or voto > voto_massimo[materia][1]:
                voto_massimo[materia] = (studente, voto)

    return voto_massimo



students = {
    "Giulia": {"matematica": 28, "storia": 30, "inglese": 25},
    "Andrea": {"matematica": 30, "storia": 27, "inglese": 29},
    "Valentina": {"matematica": 26, "storia": 30, "inglese": 30},
}

print(voto_migliore(students))