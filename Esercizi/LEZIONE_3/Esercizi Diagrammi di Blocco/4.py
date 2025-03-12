# Assegnare un tutor
n_tutor = 10
attesa = 0

while True:
    studente = input("Inserisci il tuo nome: ").title()
    if n_tutor > 0:
        n_tutor -= 1
        print("Tutor assegnato con successo.")
    else:
        attesa += 1
        print("Studente in lista di attesa.")
    if n_tutor == 0 and attesa > 50:
        break
