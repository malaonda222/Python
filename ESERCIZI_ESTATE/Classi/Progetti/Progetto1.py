'''
1 class Studente: 
Attributi:
nome (stringa)
cognome (stringa)
voti (lista di interi)
Metodi:
aggiungi_voto(voto) → aggiunge un voto alla lista
calcola_media() → ritorna la media aritmetica dei voti

2 Sottoclassi di Studente:
StudenteLaurea
Eredita da Studente
Usa il metodo calcola_media() come definito nella classe base (media aritmetica semplice)

StudenteMaster
Eredita da Studente
Override di calcola_media():
ogni voto vale doppio, quindi la media è ponderata

3. Classe Corso
Attributi:
nome_corso (stringa)
studenti (lista di oggetti Studente)
Metodi:
aggiungi_studente(studente) → aggiunge uno studente alla lista
mostra_studenti() → stampa nome, cognome e media (usando calcola_media() che è polimorfico)

4. Polimorfismo
Crea un oggetto Corso.
Crea almeno:
un'istanza di StudenteLaurea
un'istanza di StudenteMaster
Aggiungi voti a entrambi.
Iscrivili allo stesso corso.
Chiama mostra_studenti() → dimostrerà che calcola_media() si comporta diversamente in base alla sottoclasse.
'''
class Studente:
    def __init__(self, nome: str, cognome: str) -> None:
        self.setNome(nome)
        self.setCognome(cognome)
        self.setVoti([])
    
    def setNome(self, nome: str) -> None:
        if not isinstance(nome, str):
            raise ValueError("Errore. Il nome deve essere una stringa")
        self.__nome = nome 
    
    def setCognome(self, cognome: str) -> None:
        if not isinstance(cognome, str):
            raise ValueError("Errore. Il cognome deve essere una stringa")
        self.__cognome = cognome 

    def setVoti(self, voti: list[int]) -> None:
        self.__voti = voti

    def getNome(self) -> str:
        return self.__nome 
    
    def getCognome(self) -> str:
        return self.__cognome 
    
    def getVoti(self) -> list:
        return self.__voti

    def aggiungi_voto(self, voto: int) -> None:
        self.__voti.append(voto)
    
    def calcola_media(self) -> float:
        voti = self.getVoti()
        if not voti:
            return "Media: 0"
        else: 
            return sum(voti) / len(voti)

class StudenteLaurea(Studente):
    def __init__(self, nome: str, cognome: str) -> None:
        super().__init__(nome, cognome)
    
    def calcola_media(self):
        return super().calcola_media()
    
class StudenteMaster(Studente):
    def __init__(self, nome: str, cognome: str) -> None:
        super().__init__(nome, cognome)
    
    def calcola_media(self):
        voti = self.getVoti()
        peso = 3
        if not voti:
            return 0
        somma_ponderata = sum(voto * 2 for voto in voti)
        somma_pesi = peso * len(voti)
        return somma_ponderata/somma_pesi  
    
class Corso:
    def __init__(self, nome_corso: str) -> None:
        self.setNomeCorso(nome_corso)
        self.setStudenti([])
    
    def setNomeCorso(self, nome_corso: str) -> None:
        if not isinstance(nome_corso, str):
            raise ValueError("Errore. Il nome del corso deve essere una stringa")
        self.__nome_corso = nome_corso
    
    def setStudenti(self, studenti: list[Studente]) -> None:
        self.__studenti = studenti 

    def getNomeCorso(self) -> str:
        return self.__nome_corso

    def getStudenti(self) -> list[Studente]:
        return self.__studenti 

    def aggiungi_studente(self, studente: Studente) -> None:
        self.__studenti.append(studente)
    
    def mostra_studenti(self) -> None:
        if not self.__studenti:
            return "Nessuno studente iscritto"
        else:
            for studente in self.__studenti:
                print(f"Nome: {studente.getNome()} - Cognome: {studente.getCognome()} - Media: {studente.calcola_media()}")



studentelaurea1 = StudenteLaurea("Gianni", "Bini")
studentemaster1 = StudenteMaster("Riccardo", "Baldini")

studentelaurea1.aggiungi_voto(18)
studentelaurea1.aggiungi_voto(30)
studentelaurea1.aggiungi_voto(24)

studentemaster1.aggiungi_voto(18)
studentemaster1.aggiungi_voto(30)
studentemaster1.aggiungi_voto(24)

python = Corso("Python")

python.aggiungi_studente(studentemaster1)
python.aggiungi_studente(studentelaurea1)

python.mostra_studenti()
