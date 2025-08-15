'''Nome dell’esercizio: miglior_voto_per_materia
 
Traccia:
Ogni studente è rappresentato come un dizionario con nome e un sotto-dizionario 
materie dove le chiavi sono i nomi delle materie e i valori sono le liste di voti.
Scrivi una funzione miglior_voto_per_materia che ritorni un dizionario {materia: voto_massimo} 
considerando tutti gli studenti.
 
studenti = [
    {"nome": "Marco", "materie": {"matematica": [18, 25], "storia": [28, 30]}},
    {"nome": "Giulia", "materie": {"matematica": [22, 24], "storia": [26, 27]}},
    {"nome": "Elena", "materie": {"matematica": [30, 29], "storia": [25, 26]}},
]
 
Suggerimento: Puoi iterare su tutti gli studenti e aggiornare il dizionario delle 
materie man mano che trovi voti più alti.'''