'''
Traccia:
Implementa la funzione def conta_carattere(s: str, c: str) -> int, 
che restituisce il numero di occorrenze del carattere c nella stringa s.
'''

def conta_carattere(s: str, c: str) -> int:
    if s == "":
        return 0
    if s[0] == c:
        return 1 + conta_carattere(s[1:], c)
    else:
        return conta_carattere(s[1:], c)

print(conta_carattere("ccciiiaaaooo", "c"))