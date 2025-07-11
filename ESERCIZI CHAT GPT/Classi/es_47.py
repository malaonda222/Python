class Studente:
    def __init__(self, nome: str, eta: int) -> None:
        self.nome = nome 
        self.eta = eta 
        self.voti: dict[str, list[int]]= {}

    def aggiungi_voto(self, materia: str, voto: int) -> None:
        if voto < 0 or voto > 10:
            raise ValueError("Il voto deve essere compreso tra 0 e 10")
        if materia not in self.voti:
            self.voti[materia] = []
        self.voti[materia].append(voto)
    
    def media(self) -> float:
        totale_voti = 0
        numero_voti = 0
        for lista_voti in self.voti.values():
            totale_voti += sum(lista_voti)
            numero_voti += len(lista_voti)

        if numero_voti == 0:
            return 0.0 
        
        media = totale_voti / numero_voti
        return media 
    
    def materia(self) -> list:
        lista_materie = []
        for key in self.voti.keys():
            lista_materie.append(key)
        return lista_materie
    
    def __str__(self) -> str:
        return f"Studente: {self.nome} - Media: {self.media()}"

if __name__ == "__main__":
    s1: Studente = Studente("Luigi", 16)
    s2: Studente = Studente("Mario", 11)

    s1.aggiungi_voto("matematica", 8)
    s1.aggiungi_voto("italiano", 10)
    s1.aggiungi_voto("matematica", 5)
    s1.aggiungi_voto("matematica", 6)
    s1.aggiungi_voto("geografia", 4)

    s2.aggiungi_voto("matematica", 8)
    s2.aggiungi_voto("italiano", 10)
    s2.aggiungi_voto("matematica", 5)
    s2.aggiungi_voto("matematica", 6)
    s2.aggiungi_voto("geografia", 4)
    s2.aggiungi_voto("biologia", 9)

    print(f"La media dello studente {s1.nome} è: {s1.media()}")
    print(f"La media dello studente {s2.nome} è: {s2.media()}")

    print(f"Le materie per cui {s1.nome} ha un voto sono: {s1.materia()}")
    print(f"Le materie per cui {s2.nome} ha un voto sono: {s2.materia()}")

    print(s1)
    print(s2)