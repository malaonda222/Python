file = open("LEZIONE_15/example.txt", "a") 
#r vuol dire read 
print(file)
file.close()

file = open("LEZIONE_15/example.txt", "a") 

try:
    pass
finally:
    file.close()

#oppure 
 
with open("LEZIONE_15/example.txt", "a") as file:
    stringa: str = "Ciao"
    file.write(stringa)
    pass 

with open("LEZIONE_15/example.txt", "r+") as file:
    print(file.read())

def connect(host, port, timeout):
    pass


PATH: str = "Esercizi/LEZIONE_15/config.json"  #dichiariamo una costante in cui ci scriviamo il pat del json
mode: str = "r"


with open(PATH, mode=mode) as file:
    config: dict = json.load(file) #funzione load restituisce un dizionario
    print(config)

    nome_applicazione: str = config["appName"] 

    host: str = config["server"]["host"]
    port: str = str(config["server"]["port"])
    timeout: str = config["server"]["timeout"]

    connect(ip=host, port=port, timeout=timeout)

    print(nome_applicazione)

import json 
PATH: str = "Esercizi/LEZIONE_15/config_1.json" #si crea un file json nuovo
mode: str = "w" #vogliamo scrivere nel file 
config: dict = {}

with open(PATH, mode="r") as file:#prendere json, trasformare in dizionario e modificare
    config = json.load(file) #abbiamo solo letto 

config["server"]["host"] = "facebook.com"
config["server"]["port"] = 5000 #abbiamo fatto la modifica sotto forma di dizionario salvato nella RAM 
                                

with open(PATH, mode="w") as file: #sovrascrivere quello che abbiamo sul disco sul text io wrapper

    json.dump(config, file, indent=4) 

