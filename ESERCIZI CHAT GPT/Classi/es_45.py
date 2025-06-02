class Veicolo:
    def __init__(self, targa: str, marca: str, tipo: str):
        self.targa = targa
        self.marca = marca 
        self.tipo = tipo 
    
    def __str__(self):
        return f"Targa: {self.targa}\nMarca: {self.marca}\nTipo: {self.tipo}"
    

class Garage:
    def __init__(self):
        self.veicoli = []

    def aggiungi_veicolo(self, veicolo: Veicolo):
        self.veicoli.append(veicolo)
    
    def rimuovi_veicolo(self, veicolo: Veicolo):
        if veicolo in self.veicoli:
            self.veicoli.remove(veicolo)
            return "Veicolo rimosso."
        return "Veicolo non presente nella parcheggio."
    
    def trova_veicoli_per_tipo(self, tipo: str):
        lista_tipo = list()
        for veicolo in self.veicoli:
            if veicolo.tipo in tipo:
                lista_tipo.append(veicolo)
        return lista_tipo
    
    def trova_veicolo_tipo(self, tipo: str):
        return [v for v in self.veicoli if v.tipo == tipo]