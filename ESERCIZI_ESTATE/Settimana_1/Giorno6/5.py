'''Simula un bancomat: richiedi un pin finché non è corretto.'''

pin: str = "19986245"
while True:
    input_utente = input("Inserire il pin a 8 cifre: ")
    if len(input_utente) != len(pin):
        print("Errore. Inserire nuovamente il pin!")
        continue
    if input_utente == pin:
        print("Pin corretto!")
        break 
    else:
        print("Inserire di nuovo il pin!")


pin: int = 19986245
while True:
    try:
        input_utente = int(input("Inserire il pin: "))
        if len(str(input_utente)) != len(str(pin)):
            print("Errore. Il pin deve essere lungo 8 cifre!")
            continue
        if input_utente == pin:
            print("Pin corretto!")
    except ValueError:
        print("Prego, inserire un pin valido (solo cifre)")