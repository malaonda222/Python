class Studente:
    def __init__(self, nome: str):
        self.nome = nome 
        self.presenze = []

    def aggiungi_presenza(self, presente: bool):
        self.presenze.append(presente)
    
    def percentuale_presenze(self):
        if not self.presenze:
            return 0.0 
        presenze_totali = len(self.presenze)
        giorni_presenti = self.presenze.count(True)
        percentuale = (giorni_presenti / presenze_totali) * 100
        return round(percentuale, 2)

class Corso:
    def __init__(self, nome_corso: str):
        self.nome_corso = nome_corso
        self.studenti = list()

    def aggiungi_studente(self, studente: Studente):
        self.studenti.append(studente)

    def media_presenze(self):
        if not self.studenti:
            return 0.0
        somma = sum(studente.percentuale_presenze() for studente in self.studenti)
        return round(somma / len(self.studenti), 2)


class Registro:
    def __init__(self):
        self.diz_corsi = {}

    def aggiungi_corso(self, corso: Corso):
        if corso not in self.diz_corsi:
            self.diz_corsi[corso.nome_corso] = corso
        else:
            print("Il corso è già presente nel registro")
    
    def presenza_totale(self, nome_corso: str):
        corso = self.diz_corsi.get(nome_corso)
        if not corso:
            return 0.0
        return corso.media_presenze()
    
    def elenco_studenti(self, nome_corso: str):
        corso = self.diz_corsi.get(nome_corso)
        if not corso:
            return list()
        return [studente.nome for studente in corso.studenti]

studente1 = Studente("Gianni")
studente1.aggiungi_presenza(True)
studente1.aggiungi_presenza(True)
print(studente1.presenze)
print(studente1.percentuale_presenze())