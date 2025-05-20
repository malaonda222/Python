import Esercizi.LEZIONE_4.EserciziObbligatori.printing_functions as printing_functions #si richiama tutto il modulo e per stampare bisogna inserire dopo il print il nome del modulo.funzione()
print(printing_functions.somma1(3, 2))
print(printing_functions.substraction(9, 6))


from Esercizi.LEZIONE_4.EserciziObbligatori.printing_functions import somma1
print(somma1(3, 8))


from Esercizi.LEZIONE_4.EserciziObbligatori.printing_functions import somma1 as som 
print(som(4, 9))


import Esercizi.LEZIONE_4.EserciziObbligatori.printing_functions as pf
print(pf.substraction(10, 4))
print(pf.somma1(5, 9))


from Esercizi.LEZIONE_4.EserciziObbligatori.printing_functions import * #si richiama tutto il modulo e nel print basta fare riferimento alla funzione print(funzione())
print(somma1(3, 2))
print(substraction(8, 6))


