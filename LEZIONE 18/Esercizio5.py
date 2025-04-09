import unittest

class FormulaError(Exception):
      pass

def calcolatrice_interattiva():
    while True:
        try:
            input_str = input("Inserire una formula composta da un numero, un operatore (+ o -) e un altro numero: ")
            if input_str.lower() == "quit":
                print("Errore. Il programma termina.")
                break
        
            input_str = input_str.split()
            
            if len(input_str) != 3:
                raise FormulaError("L'input deve esssere composto solo da 3 elementi.")
    
            try:
                numero_1 = float(input_str[0])
                numero_2 = float(input_str[2])
            except ValueError:
                raise FormulaError("I numeri devono essere convertibili in float.")

            operatore = input_str[1]
            if operatore not in ('+', '-'):
                raise FormulaError("Il secondo elemento (operatore) deve essere "+" o "-".")

            if operatore == "+":
                somma = numero_1 + numero_2
                print(somma)
            if operatore == "-":
                sottrazione = numero_1 - numero_2
                print(sottrazione)
            
        except FormulaError as e:
            print(f"Errore: {e}")


calcolatrice_interattiva()
            
