'''Indovina il numero: scrivi un programma che usa un ciclo while per chiedere all'utente
di indovinare un numero tra 1 e 10. Continua a chiedere fino a quando l'utente indovina'''

numero_da_indovinare = 6
trovato = False
while not trovato: 
    numero = int(input("Indovina il numero segreto compreso tra 1 e 10: "))
    if numero == numero_da_indovinare:
        print("Hai indovinato il numero segreto!")
        trovato = True
    else:
        print("Numero segreto non indovintato. Ritenta.")


numero_segreto = 7
while True:
    num = int(input("Indovina il numero segreto compreso tra 1 e 10: "))
    if num == numero_segreto:
        print(f"Hai indovinato il numero segreto!")
        break
    else:
        print("Ritenta.")


segreto = 8
lista_tentativi = []
while True:
    n = int(input("Indovina il numero segreto compreso tra 1 e 10: "))
    if n in lista_tentativi:
        print("Hai già inserito questo numero, ritenta.")
        continue
    else: 
        lista_tentativi.append(n)

        if n == segreto:
            print(f"Hai indovinato il numero segreto!")
            break
        else:
            print("Ritenta.")  