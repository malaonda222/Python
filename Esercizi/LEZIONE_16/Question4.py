class Specie:
    def __init__(self, nome: str, popolazione: int, tasso_crescita: float):
        self.nome = nome
        self.popolazione_attuale = popolazione 
        self.tasso_crescita = tasso_crescita
    
    def cresci(self):
        self.popolazione_attuale *= (1 + self.tasso_crescita/100)
        self.popolazione_attuale = int(self.popolazione_attuale)

    def anni_per_superare(self, altra_specie: "Specie") -> int:
        anni_necessari = 0
        while self.popolazione_attuale <= altra_specie.popolazione_attuale: 
            self.cresci()
            altra_specie.cresci()
            anni_necessari += 1
            if anni_necessari >= 1000:
                print("Limite anni raggiunto.")
        return anni_necessari

    def getDensita(self, area_kmq: float):
        anni_densita = 0 
        densita = self.popolazione_attuale / area_kmq
        while densita >= 1:
            self.cresci()
            densita = self.popolazione_attuale / area_kmq
            anni_densita += 1
        return anni_densita


class BufaloKlingon(Specie):
    def __init__(self, popolazione: int, tasso_crescita: float):
        super().__init__("Bufalo Klingon", popolazione, tasso_crescita) 

class Elefante(Specie):
    def __init__(self, popolazione: int, tasso_crescita: float):
        super().__init__("Elefante", popolazione, tasso_crescita)


# Creazione delle istanze delle specie
bufalo_klingon = BufaloKlingon(100, 15)  # Crea un'istanza di BufaloKlingon con popolazione 100 e tasso di crescita 15%
elefante = Elefante(10, 35)  # Crea un'istanza di Elefante con popolazione 10 e tasso di crescita 35%

# Calcolo degli anni necessari per superare
anni_necessari = elefante.anni_per_superare(bufalo_klingon)  # Calcola gli anni necessari affinché gli elefanti superino i bufali Klingon
print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}")

# Calcolo della densità di popolazione per i Bufali Klingon
anni_densita = bufalo_klingon.getDensita(1500)  # Calcola gli anni necessari per raggiungere una densità di 1 bufalo Klingon per km²
print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: {anni_densita}")