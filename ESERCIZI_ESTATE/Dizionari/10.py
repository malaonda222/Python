'''Crea un dizionario in cui ogni chiave è il nome di un dipartimento in un'azienda 
(ad esempio, "Marketing", "IT", "Vendite"), e ogni valore è un altro dizionario con le 
informazioni dei dipendenti di quel dipartimento (nome, ruolo, salario). 
Scrivi una funzione che calcoli il salario medio di ogni dipartimento.'''


def calcola_salario(dizio: dict[str, dict[str, dict]]) -> dict:
    salari_medi = {}
    for dipartimento, dipendenti in dizio.items():
        somma_salario = 0
        num_dipendenti = 0
        for dipendente, informazioni in dipendenti.items():
            somma_salario += informazioni["salario"]
            num_dipendenti += 1 
        
        if num_dipendenti > 0:
            salari_medi[dipartimento] = somma_salario/num_dipendenti
    return salari_medi




dizio = {
    "Marketing": {
        "Alice": {"ruolo": "Manager", "salario": 3500},
        "Bob": {"ruolo": "Junior", "salario": 2500}
    },
    "IT": {
        "Charlie": {"ruolo": "Developer", "salario": 4000},
        "David": {"ruolo": "Support", "salario": 2800}
    },
    "Vendite": {
        "Eve": {"ruolo": "Sales Rep", "salario": 3000},
        "Frank": {"ruolo": "Sales Manager", "salario": 5000}
    }
}
salari_medi = calcola_salario(dizio)
print(salari_medi)