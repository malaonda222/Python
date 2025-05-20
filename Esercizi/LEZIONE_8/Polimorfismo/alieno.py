class Alieno:
    '''Di un alieno ci interessa sapere la galassia di provenienza'''
#Inizializzare un oggetto della classe alieno 
    def __init__(self, galaxy: str):
        self.setGalaxy(galaxy)
    
    def setGalaxy(self, galaxy:str) -> None:
        if not isinstance(galaxy, str) or galaxy.strip() == "":
            raise ValueError("Errore. La galassia di provenienza deve essere una stringa e non può essere una stringa vuota.")   
        else:
            self.galaxy = galaxy 
    
    def getGalaxy(self) -> str:
        return self.galaxy
    
    def speak(self) -> None:
        print("asdgirlodd")
    
    def __str__(self) -> str:
        return f"\nAlieno proveniente dalla galassia {self.getGalaxy()}.\n"
    



    
