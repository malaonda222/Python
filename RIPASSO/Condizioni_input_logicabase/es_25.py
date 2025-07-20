'''Scrivi una funzione are_anagrams(str1, str2) che ritorna True se le due stringhe 
sono anagrammi (stesse lettere in quantità uguale, ma ordine diverso).'''

def are_anagrams(str1, str2) -> bool:
    if len(str1) != len(str2):
        return False 
    str1_pulita = sorted(str1.replace(" ", "").lower())
    str2_pulita = sorted(str2.replace(" ", "").lower())
    if str1_pulita == str2_pulita:
        return True


print(are_anagrams("listen", "Silent"))