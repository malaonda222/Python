class Studente:
    def __init__(self, nome, cognome, corso_di_studi): #scopo di init è quello di costruire gli oggetti
        self.nome = nome
        self.cognome = cognome
        self.corso_di_studi = corso_di_studi

    def scheda_personale(self):
        return f"Scheda studente: \n Nome: {self.nome} \n Cognome: {self.cognome} \n Corso di studi: {self.corso_di_studi}"

studente_uno = Studente("Py", "Mike", "programmazione")
studente_due = Studente("Marta", "Stannis", "Lingue")

print(studente_uno.scheda_personale())
print(studente_due.scheda_personale())

print(Studente.scheda_personale(studente_uno))
