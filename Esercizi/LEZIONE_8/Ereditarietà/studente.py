from Esercizi.LEZIONE_8.Ereditarietà.persona import Persona #la classe studente è una specializzazione della classe Persona

class Studente(Persona):
    def __init__(self):
        self.getAge