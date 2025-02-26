giorno = int(input("Inserisci un giorno del mese: "))
mese = int(input("Inserisci un mese dell'anno: "))

data = (giorno, mese)
match data:
    case (1, 1):
        print("Output: Il 01/01 è Capodanno")
    case (14, 2):
        print("Output: Il 14/02 è San Valentino")
    case (2, 6):
        print("Output: Festa della Repubblica")
    case (15, 8):
        print("Ferragosto")
    case (31, 10):
        print("Output: uuh Halloween")
    case (25, 12):
        print("Output: Il 25/12 è Natale")
    case (8, 9):
        print("Il 08/09 è il compleanno Marco")
    case _:
        print("Nessuna festività importante in questa data")