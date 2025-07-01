'''Sistema di valutazione scolastica:
Crea una funzione che accetti come input il nome di uno studente e i suoi punteggi 
nelle diverse materie. La funzione calcola il punteggio medio e stampa il nome dello 
studente, la media e un messaggio che indica se lo studente ha superato 
l'esame (media >= 60) o meno.
Creare un ciclo for per scorrere un elenco di studenti e punteggi, 
chiamando la funzione per ogni studente.'''

def media_studente(nome: str, punteggi: dict[str, int]) -> None:
    media: float = sum(punteggi.values())/len(punteggi)
    if media >= 60:
        stato: str = "Passato"
    else:
        stato: str = "Bocciato"
    
    print(f"Studente: {nome}\nMedia: {media:.2f}\nStato: {stato}")

    #creare una lista di studenti rappresentata da una tupla contenente un nome e un dizionario di oggetti punteggi
studenti: list[tuple[str, dict[str, int]]] = [
    ("Elena", {"Matematica": 75, "Scienze": 80, "Inglese": 59}),
    ("Riccardo", {"Matematica": 50, "Scienze": 45, "Inglese": 55}),
    ("Paolo", {"Matematica": 90, "Science": 95, "Inglese": 85})
    ]
for nome, punteggi in studenti:
    media_studente(nome, punteggi) 

