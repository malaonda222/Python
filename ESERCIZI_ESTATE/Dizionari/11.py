'''Crea un dizionario con i nomi degli studenti come chiavi e i punteggi come valori. 
Scrivi un programma che ordini il dizionario in ordine crescente di punteggio.'''

def ordina_dizionario(dizionario: dict[str, int]) -> dict:
    return sorted(dizionario.values())

#più corretto cosi:
def ordina_dizionario2(dizionario: dict[str, int]) -> dict:
    dizionario_ordinato = dict(sorted(dizionario.items(), key=lambda item: item[1]))
    return dizionario_ordinato

studenti = {
    "Alice": 88,
    "Luca": 75,
    "Marco": 92,
    "Giulia": 85,
    "Sara": 78
}

print(ordina_dizionario(studenti))
print(ordina_dizionario2(studenti))