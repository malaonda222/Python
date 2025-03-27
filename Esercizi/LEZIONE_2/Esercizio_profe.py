'''Data una stringa contenente solo i caratteri '(' e ')', restituire True se le parentesi sono "bilanciate" e False altrimenti.
Ad esempio: 

bilanciate("((()))") -> True
bilanciate("(()") -> False
bilanciate("()()()") -> True
bilanciate("))((") -> False
bilanciate("(()())") -> True'''

parentesi = input("Inserisci una sequenza di presentesi: ")
risultato = 0
contatore = 0

for x in parentesi:
    if contatore >= 0:
        if x == "(":
            contatore += 1
        
        elif x == ")":
            contatore -= 1
        
        else:
            risultato = False

if contatore == 0:
    risultato = True

else: 
    risultato = False

print(f'bilanciate("{parentesi}") -> {risultato}')




