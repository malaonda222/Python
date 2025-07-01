'''Esercizio 7'''
def check_parentheses(expression:str) -> bool:
    bilanciamento = 0 

    for item in expression:
        if item == '(':
            bilanciamento += 1
        elif item == ')':
            bilanciamento -= 1
    
        if bilanciamento < 0:
            return False 
    
    if bilanciamento == 0:
        return True
