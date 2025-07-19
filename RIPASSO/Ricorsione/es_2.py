'''
Traccia:
Scrivi una funzione chiamata somma_ricorsiva(n: int) -> int che calcoli la somma dei 
numeri da 1 a n in modo ricorsivo.
 
La somma si definisce così:
* Caso base:
somma_ricorsiva(1) = 1
* Passo ricorsivo:
somma_ricorsiva(n) = n + somma_ricorsiva(n - 1) per n > 1
 
Requisiti:
Gestisci correttamente il caso base (n == 1)
* Richiama la funzione solo se n > 1
 
Aggiungi una funzione test_somma() che:
* Chiede all’utente un intero positivo n
* Verifica che n >= 1
* Calcola e stampa la somma da 1 a n usando la funzione ricorsiva
 
Suggerimento:
Puoi strutturarlo in modo simile all’esercizio del fattoriale.
'''

def somma_ricorsiva(n: int) -> int:
    if n == 1:
        return 1
    if n <= 0:
        return 0
    return n + somma_ricorsiva(n - 1)

def test_somma():
    try: 
        valore = input("Inserisci il numero: ")
        if valore >= 1:
            risultato = somma_ricorsiva(valore)
            print(f"La somma ricorsiva del numero {valore} è: {risultato}")
        else:
            print("Inserisci un numero maggiore o uguale a 1!")
    
    except ValueError:
        print("Errore. Input non valido, inserisci un numero intero positivo")


test_somma()