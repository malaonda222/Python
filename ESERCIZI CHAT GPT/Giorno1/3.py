'''Esercizio 3 - Anagrammi
Scrivi una funzione sono_anagrammi(str1, str2) che controlla se due stringhe sono anagrammi (ignorando spazi e maiuscole).
Esempio: sono_anagrammi("Roma", "Amor") → True'''


def sono_anagrammi(str1: str, str2: str) -> bool:
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if sorted(str1) == sorted(str2):
        return True 
    else:
        return False 

print(sono_anagrammi("Roma", "Amor"))
print(sono_anagrammi("Asino", "Siano"))
print(sono_anagrammi("Parola", "Parole"))