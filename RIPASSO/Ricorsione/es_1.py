'''
Traccia:
Scrivi una funzione chiamata fattoriale(n: int) -> int che calcola il 
fattoriale di un numero intero n in modo ricorsivo.
 
Il fattoriale di un numero intero positivo n si definisce così:
* fattoriale(0) = 1 (caso base)
* fattoriale(n) = n * fattoriale(n - 1) per n > 0
 
La funzione deve:
* Gestire il caso base correttamente.
* Applicare la ricorsione solo per n > 0.
* Infine, crea una funzione test_fattoriale() che:
* Chiede all’utente un numero intero ≥ 0,
* Calcola e stampa il suo fattoriale usando la funzione ricorsiva.
 
Suggerimento:
Ricorda di validare l’input in test_fattoriale() per evitare numeri negativi.
'''
 
def fattoriale(n: int) -> int:
    if n == 0:
        return 1
    return n * fattoriale(n -1)

def test_fattoriale():
    numero = input("Inserisci un numero maggiore o uguale a 0: ")
    if numero.isdigit():
        numero_int = int(numero)
        risultato = fattoriale(numero_int)
        print(f"Il fattoriale del numero {numero_int} è: {risultato}")
    else:
        print("Inserisci un numero positivo o uguale a zero!")

test_fattoriale()