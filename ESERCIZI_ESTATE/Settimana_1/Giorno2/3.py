'''Rimuovi tutti gli spazi da una stringa.'''

def rimuovi_spazi(stringa1: str) -> str:
    nuova_stringa = stringa1.replace(" ", "")
    return nuova_stringa

print(rimuovi_spazi("Oggi è una bella giornata !"))
print(rimuovi_spazi("Ciao come ti chiami? ?"))




def rimuovi_tutti_spazi(stringa: str) -> str:
    return stringa.replace(" ", "")


print(rimuovi_tutti_spazi("Stringa senza spazi"))