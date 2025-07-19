'''Tema: Condizioni multiple e contatori
Obiettivo:
Classificare una serie di età inserite dall’utente in tre gruppi:
* Minorenni (< 18 anni)
* Maggiorenni (18-64 anni)
* Anziani (65+ anni)'''

def classifica_eta() -> None:
    while True:
        numero = input("Inserisci un numero: ")
        if numero.isdigit():
            numero = int(numero)
            if numero < 18:
                print("Minorenne")
            if 18 <= numero <= 64: 
                print("Maggiorenni")
            else:
                print("Anziani")
        else:
            print("Errore. Devi inserire un numero intero positivo")

classifica_eta()    