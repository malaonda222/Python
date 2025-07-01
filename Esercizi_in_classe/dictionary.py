mydict:dict = {
    "Pizza":10.00, 
    "Pasta":20.00, 
    "Lasagna":30.00
    }

print("Primo Modo - Chiave, Valore")
for key, value in mydict.items():
    print(f"{key}: {value}")

print("Secondo Modo - Chiavi e valori:")
for key in mydict:
    print(f"{key}: {mydict[key]}")
    
print("Terzo Modo - solo valori:")
for key in mydict:
    print(mydict[key])
 
print("Quarto Modo - solo chiavi:")  
for key in mydict:
    print(key)