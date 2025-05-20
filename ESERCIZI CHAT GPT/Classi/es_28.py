'''Contatto: nome, telefono
Rubrica: 
Attributo: lista di contatti
Metodi:
aggiungi_contatto(contatto)
cerca(nome)
mostra_tutti()'''

class Contatto:
    def __init__(self, nome: str, telefono: str):
        self.nome = nome
        self.telefono = telefono 
    
    def __str__(self):
        return f"Nome: {self.nome}\nContatto telefonico: {self.telefono}"
    
class Rubrica:
    def __init__(self):
        self.contatti = []

    def aggiungi_contatto(self, contatto: str):
        self.contatti.append(contatto)
        print(f"Contatto \"{contatto.nome}\" aggiunto alla rubrica.")
    
    def cerca_nome(self, nome: str):
        trovati = [contatto for contatto in self.contatti if contatto.nome.lower() == nome.lower()]
        if trovati:
            print(f"Contatto \"{nome}\" trovato.")
        else:
            print(f"Contatto \"{nome}\" non presente in rubrica.")
        
    def mostra_nomi(self):
        if not self.contatti:
            print("La rubrica è vuota.")
        else:
            for contatto in self.contatti:
                print(f"{contatto}, ")

contatto1 = Contatto("Mimmo", "+90 45374988")
contatto2 = Contatto("Giuseppe", "+45 377469999")
contatto3 = Contatto("Riccardo", "+39 466667890")
rubrica = Rubrica()
rubrica.aggiungi_contatto(contatto1)
rubrica.aggiungi_contatto(contatto2)
rubrica.aggiungi_contatto(contatto3)
rubrica.mostra_nomi()
rubrica.cerca_nome("Riccardo")