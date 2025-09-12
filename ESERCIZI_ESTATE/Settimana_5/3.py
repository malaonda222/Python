'''Scrivere un programma che:
Chieda all’utente di inserire una serie di parole (una alla volta).
Salvi le parole in un file (una parola per riga).
Legga il file e stampi tutte le parole in maiuscolo.'''


def scrivi_e_leggi_parole():
    nome_file = "parole.txt"
    parole = []

    try: 
        num = int(input("Quante parole vuoi inserire? "))
    except ValueError:
        print("Devi inserire un numero intero.")
        return 
    
    for i in range(1, num + 1):
        parola = input(f"Inserisci la {i}° parola: ")
        parole.append(parola)
    
    with open(nome_file, 'w') as file:
        for parola in parole:
            file.write(parola + "\n")
    print("Parole salvate -> adesso le stampo in carattere maiuscolo: ")
    
    with open(nome_file, 'r') as file:
        for linea in file:
            print(linea.strip().upper())


scrivi_e_leggi_parole()