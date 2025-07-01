class Documento:
    def __init__(self, testo: str) -> None:
        self.setText(testo) 
    
    def getText(self) -> str:
        return self.testo 
    
    def setText(self, testo: str) -> None:
        if not isinstance(testo, str) or not testo.strip():
            raise ValueError("Input invalido.")
        self.testo = testo
    
    def isInText(self, parola: str) -> bool:
        if not isinstance(parola, str) or not parola.strip():
            raise ValueError("La parola da cercare deve essere una stringa.")
        return parola in self.testo
    

class Email(Documento):
    def __init__(self, mittente: str, destinatario: str, titolo_messaggio: str, corpo_messaggio: str) -> None:
        self.setMittente(mittente) 
        self.setDestinatario(destinatario)
        self.setTitoloMessaggio(titolo_messaggio)
        super().__init__(corpo_messaggio)

    def setMittente(self, mittente: str) -> None:
        if not isinstance(mittente, str) or not mittente.strip():
            raise ValueError("Input invalido.")
        self.mittente = mittente 

    def getMittente(self) -> str:
        return self.mittente 
    
    def setDestinatario(self, destinatario: str) -> None:
        if not isinstance(destinatario, str) or not destinatario.strip():
            raise ValueError("Input invalido.")
        self.destinatario = destinatario
    
    def getDestinatario(self) -> str:
        return self.destinatario 
    
    def setTitoloMessaggio(self, titolo_messaggio: str) -> None:
        if not isinstance(titolo_messaggio, str) or not titolo_messaggio.strip():
            raise ValueError("Input invalido.")
        self.titolo_messaggio = titolo_messaggio
    
    def getTitoloMessaggio(self) -> str:
        return self.titolo_messaggio
    
    def getText(self) -> str:
        return f"Da: {self.getMittente()}, A: {self.getDestinatario()}\nTitolo: {self.getTitoloMessaggio()}\nMessaggio: {super().getText()}"
    
    def writeToFile(self, path: str):
        with open(path, "w") as file:
            file.write(self.getText())
        
    
class File(Documento):
    def __init__(self, nomePercorso: str) -> None:
        self.path = nomePercorso
        contenuto = self.leggiTestoDaFile()
        super().__init__(contenuto)
    
    def getNomePercorso(self) -> str:
        return self.nomePercorso
    
    def leggiTestoDaFile(self):
        with open(self.path, "r") as file:
            return file.read() #ritorna il file sotto forma di stringa, readlines: lista dove ogni elemento è una linea, readline: ritorna singolamente ogni riga
    
    def getText(self) -> str:
        return f"Percorso: {self.getNomePercorso()}\nContenuto: {super.getText()}"


    
if __name__ == "__main__":
    test: Email = Email("bandinelli.lisa@gmail.com", "gigi@gmail.com", "Ciao", "Mi chiamo Nino")
    test.getText()
    test.writeToFile("./email.txt")
    print(test.getText())

    test2: File = File("./email.txt")
    print(test2.leggiTestoDaFile())




