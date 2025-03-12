# Assegnare un tutor
n_tutor = 10
attesa = 0

while True:
    studente = input("Inserisci il tuo nome: ").lower()
    if n_tutor > 0:
        n_tutor -= 1
        print(f"Gentile studente, il tutor è stato assegnato con successo.")
    else:
        attesa += 1
        print("Gentile studente, le comunichiamo che è stato inserito nella lista di attesa.")
    
    if n_tutor == 0 and attesa > 50:
        print("I tutor sono stati tutti assegnati a uno studente e la lista di attesa è piena.")
        break
