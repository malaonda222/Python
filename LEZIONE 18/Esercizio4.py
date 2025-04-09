class Data:
    def __init__ (self, data_str:list):
        try:
            giorno, mese, anno = map(int, data_str.split('.'))
            if anno < 1900 or anno > 2100:
                raise ValueError(f"l'anno {anno} non è valido.")
            if not (1 <= mese <= 12):
                raise ValueError(f"il mese {mese} non è valido.")
            if not (1 <= giorno <= 31):
                raise ValueError(f"il giorno {giorno} non è valido.")
            self.giorno = giorno
            self.mese = mese
            self.anno = anno
        except ValueError as e:
            raise ValueError(f"Errore nella data: {e}")

    def __str__(self):
        return f"{self.giorno}.{self.mese}.{self.anno}"

class DataBaseData:        

    def __init__(self):
        self.database = []

    def aggiungi_data(self, data_str):
        try:
            nuova_data = Data(data_str)
            if nuova_data not in self.database:
                self.database.append(nuova_data)
                print(f"La data {nuova_data} è stata aggiunta con successo nel database.")
            else:
                print(f"La data {nuova_data} è già presente nel database.")
        except ValueError as e:
            print(e) 
    
    def elimina_data(self, data_str):
        try:
            data_ricercata = Data(data_str)
            if data_ricercata in self.database:
                self.database.remove(data_ricercata)
                print(f"La data {data_ricercata} è stata eliminata dal database.")
            else:
                print(f"La data {data_ricercata} non è stata trovata nel database e quindi non è possibile eliminarla.")
        except ValueError as e:
            print(e)

    def modifica_data(self, vecchia_data_str, nuova_data_str):
        try:
            vecchia_data = Data(vecchia_data_str)
            nuova_data = Data(nuova_data_str)
            if vecchia_data in self.database:
                self.database.remove(vecchia_data)
                self.database.append(nuova_data)
                print(f"La vecchia data {vecchia_data} è stata modificata con la nuova data {nuova_data}")
            else:
                print(f"La data {vecchia_data} non è stata trovata nel database e quindi non è stato possibile modificarla.")
        except ValueError as e:
            print(e)

    def query_data(self, data_str):
        try:
            query = Data(data_str)
            if query in self.database:
                print(f"La data {query} è presente nel database.")
            else:
                print(f"La data {query} non è presente nel database.")
        except ValueError as e:
            print(e)

    def visualizza_date(self):
        if self.database:
            print("Tutte le date presenti nel database:")
            for data in self.database:
                print(data)
        else:
            print("Il database è vuoto.")

if __name__ == "__main__":

    db = DataBaseData()
    db.aggiungi_data("18.10.2024")
    db.aggiungi_data("22.10.2024")
    db.aggiungi_data("32.05.2021")
    db.aggiungi_data("28.28.2018")
    db.aggiungi_data("14.10.24")
    db.elimina_data("22.10.2024")

    db.modifica_data("18.10.2024", "25.01.2024")

    db.visualizza_date()