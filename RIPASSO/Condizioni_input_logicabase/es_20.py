''' 
Traccia:
Scrivi una funzione conta_lettere_speciali() -> None che:
* Chieda all’utente di inserire una frase.
* Converta tutta la frase in minuscolo.
* Conti quante volte compaiono le lettere 'a', 'e' e 'z' nella frase.
* Stampi il risultato con un messaggio chiaro
'''

def conta_lettere_speciali():
    input_utente = input("Inserisci una frase: ")
    input_utente_minuscolo = input_utente.lower()
    cont_a = 0
    cont_e = 0
    cont_z = 0
    for element in input_utente_minuscolo:
        if element == "a":
            cont_a += 1
        elif element == "e":
            cont_e += 1
        elif element == "z":
            cont_z += 1
        elif element == " ":
            continue
        else:
            continue
    print(f"Numero di a nella frase: {cont_a}\nNumero di e nella frase. {cont_e}\nNumero di z nella frase: {cont_z}")

conta_lettere_speciali()