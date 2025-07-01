'''
1) crea un file json usando i comandi touch e nano. Leggete il file 
appena creato e stampate un valore.
2) crea un file json da Python salvando un dizionario a vostra scelta.
3) crea un file json usando touch e nano che contenga codici fiscali come chiavi e come valori 
dizionari che contengono nome, cognome, età della persona (almeno due persone) e modificare 
il json aggiungendo una persona. 
'''

# 1
import json
PATH: str = "Esercizi/Lezione_15/esercizio1.json"
mode: str = "r"

with open(PATH, mode=mode) as file:
    config: dict = json.load(file)
    print(config["chiave1"])


# 2
import json
PATH: str = "Esercizi/LEZIONE_15/config_2.json"
mode: str = "w" 

with open(PATH, mode=mode) as file:
    config: dict = {"Citta": "Roma", "Provincia": "Lazio", "Nazione": "Italia"}
    json.dump(config, file, indent=4)


# 3
import json 
PATH: str = "Esercizi/LEZIONE_15/codice_fiscale.json"
mode: str = "w"
config: dict = {}

with open(PATH, mode= "r") as file:
    config = json.load(file)

config["BDDLSI98S62D612X"] = {"nome": "Lisa", "cognome": "Bandinelli", "eta": "77"}

with open(PATH, mode="w") as file:
    json.dump(config, file, indent=4)

