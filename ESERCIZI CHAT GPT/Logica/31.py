'''Scrivere un programma che riceve in input una frase e la classifica in una 
delle seguenti categorie:
Domanda (es: "Come stai?")
Affermativa (es: "Oggi vado al mare.")
Negativa (es: "Non mi piace il gelato.")
Esclamativa (es: "Che bella giornata!")
Comando (es: "Chiudi la porta.")'''

def classifica_frase(stringa: str) -> str:
    stringa = stringa.strip()
    if stringa.endswith("?"):
        return "Domanda"
    if stringa.ednswith("!"):
        return "Esclamativa"
    parole_negative = ["mai", "non", "nessuno", "niente"]
    for parola in parole_negative:
        if parola in stringa:
            return "Negativa"
    parole = stringa.split()
    verbi_imperativi = ["chiudi", "apri", "siediti", "alza", "corri"]
    if parole and parole[0] in verbi_imperativi:
        return "Comando"
    return "Affermativa"

