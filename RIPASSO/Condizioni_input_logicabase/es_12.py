'''
Obiettivo: Scrivere una funzione che chiede all’utente una sequenza di numeri interi 
(finché non scrive "stop"), e verifica ogni coppia di numeri consecutivi per vedere 
se almeno uno dei due è pari. Alla fine, stampa quante coppie soddisfano questa 
condizione.
'''

def chiedi_numeri():
    lista_numeri = []
    while True:
        valore = input("Inserisci un numero intero: ")
        if valore.lower() == 'stop':
            break 
        try:
            valore = int(valore)
            lista_numeri.append(valore)
        except ValueError:
            return "Inserisci un numero intero oppure 'stop' per terminare" 
        continue 

    conta_coppie = 0
    for i in range(len(lista_numeri)-1):
        if lista_numeri[i] % 2 == 0 or lista_numeri[i+1] % 2 == 0:
            conta_coppie += 1 
        
    return f"Numero di coppie con almeno un numero pari: {conta_coppie}"

print(chiedi_numeri())