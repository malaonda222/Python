'''Obiettivo:
Scrivi una funzione che prenda una stringa come input e restituisca una nuova stringa 
contenente solo le lettere alfabetiche (A-Z, a-z), rimuovendo qualsiasi altro carattere (numeri, punteggiatura, spazi, ecc.).

Esempio:
Input: "Ciao, come va? 123!"
Output: "Ciaocomeva"

Indicazioni:
Rimuovi tutti i caratteri che non sono lettere.
Mantieni solo i caratteri alfabetici.
La stringa può contenere maiuscole, minuscole, numeri e simboli.'''


def rimuovi_caratteri_speciali(stringa: str) -> str:
    if not stringa:
        return "Errore, stringa vuota"
    
    nuova_lista = []
    for carattere in stringa:
        if carattere.isalpha():
            nuova_lista.append(carattere)
    nuova_stringa = "".join(nuova_lista)
    return nuova_stringa


print(rimuovi_caratteri_speciali("??? Ciao!! Com va?"))


def rimuovi_caratteri_speciali(stringa: str) -> str:
    if not stringa:
        return "Errore, stringa vuota"
    nuova_lista = "".join([carattere for carattere in stringa if carattere.isalpha()])
    return nuova_lista