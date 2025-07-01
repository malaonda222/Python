'''Validazione dell'età per l'attività'''
eta = int(input("Inserisci la tua età: "))
if eta >= 18 and eta <= 65:
    print("Puoi partecipare all'attività.")
else:
    if eta < 18:
        print("Non puoi partecipare all'attività perché non hai raggiunto l'età minima richiesta.")
    else:
        print("Non puoi partecipare all'attività perché hai superato l'età massima consentita.")


match eta:
    case eta if eta >= 18 and eta <= 65:
        print("Puoi partecipare all'attività.")
    case eta if eta < 18:
        print("Non puoi partecipare all'attività perché non hai raggiunto l'età minima richiesta.")
    case _:
        print("Non puoi partecipare all'attività perché hai superato l'età massima consentita.")

