class Temperatura:
    def __init__(self, giorno: str, valore: float):
        self.giorno = giorno 
        self.valore = valore 

class StazioneMeteo:
    def __init__(self):
        self.temperature_registrate = []
    
    def aggiungi_temperatura(self, temp: Temperatura):
        self.temperature_registrate.append(temp)
    
    def media_settimanale(self):
        if not self.temperature_registrate:
            return "Nessuna temperatura registrata"
        else:
            somma = sum(t.valore for t in self.temperature_registrate)
            media = somma / len(self.temperature_registrate)
            return round(media, 2)
        
    def giorno_piu_freddo(self):
        if not self.temperature_registrate:
            return "Nessuna temperatura registrata."
        temperatura_min = self.temperature_registrate[0]
        for temperatura in self.temperature_registrate:
            if temperatura.valore < temperatura_min.valore:
                temperatura_min = temperatura 
        return f"{temperatura_min.giorno} con {temperatura_min.valore}°C"
    
    def giorno_piu_caldo(self):
        if not self.temperature_registrate:
            return "Nessuna temperatura registrata."
        temperatura_max = self.temperature_registrate[0]
        for temperatura in self.temperature_registrate:
            if temperatura.valore > temperatura_max.valore:
                temperatura_max = temperatura
        return f"{temperatura_max.giorno} con {temperatura_max.valore}°C"