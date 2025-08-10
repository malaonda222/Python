'''Crea un dizionario che rappresenti un contatto telefonico 
(nome, numero di telefono). Scrivi una funzione che verifica se un 
determinato nome è presente nel dizionario. Se il nome esiste, 
restituisci il numero di telefono, altrimenti, restituisci un messaggio 
che dice "Contatto non trovato".'''

def crea_dizionario(nome: str, numero: str) -> dict:
    diz: dict = {
        "nome": nome,
        "numero": numero
    }
    return diz 

def verifica_nome(diz: dict, nome: str):
    if diz["nome"] == nome:
        return f"Il numero di {nome} è: {diz['numero']}"
    else:
        return f"Contatto non trovato"
    

contatto = crea_dizionario("Lisa", "34920478563")
print(verifica_nome(contatto, "Lisa"))
    
