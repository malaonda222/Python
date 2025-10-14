'''
Esercizio: Analisi dei voti degli studenti
Scrivi una funzione con il seguente header:
    * analyze_grades(grades: list[float]) -> dict[str, float]

che, data una lista di voti compresi tra 0 e 10, ritorni un dizionario con le seguenti chiavi: 
    * "highest" → il voto più alto nella lista
    * "lowest" → il voto più basso nella lista
    * "range" → la differenza tra voto massimo e voto minimo
    * "average" → la media aritmetica dei voti
 
Vincoli:
    * Non puoi usare funzioni built-in come min(), max(), sum() o librerie esterne.
    * Se la lista è vuota, la funzione deve sollevare un ValueError con il messaggio "lista vuota".
'''

def analyze_grades(grades: list[float]) -> dict[str, float]:
    if not grades:
        raise ValueError("Lista vuota")
    else:
        voto_massimo = grades[0]
        voto_minimo = grades[0]
        somma = 0.0
        for grade in grades:
            if grade > voto_massimo:
                voto_massimo = grade 
            elif grade < voto_minimo:
                voto_minimo = grade 
            somma += grade
        valore_range = voto_massimo - voto_minimo 
        average = somma/len(grades)
    
        return {
            "highest": voto_massimo, 
            "lowest": voto_minimo, 
            "range": valore_range, 
            "average": average
        }
    

print(analyze_grades([18.0, 26.5, 28.7, 25.0]))