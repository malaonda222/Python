import re

def isDNA(sequenza: str) -> bool:
    if re.fullmatch(r'[AGCT]+', sequenza):
        return True 
    else:
        return False 


def biologia(s1: str, s2: str):
    if isDNA(s1) == False and isDNA(s2) == False:
        raise ValueError("Sequenze non valide", 0)
    else:
        max_sovrapposizione = ""
        max_len = 0
        min_len = min(len(s1), len(s2))

        for i in range(1, min_len + 1):
            if s1[-i:] == s2[:i]:
                max_sovrapposizione += s2[:i]
                max_len = i

        print(s1)
        print(" " * (len(s1) - max_len) + s2)
        print(f"La massima lunghezza è {max_len}\n")


s1 = "CAGCTGATCGATGCTAGCCTG"
s2 = "AGCCTGTTGCACCTAGA"
biologia(s1, s2)

s3= "TTGACCAGGTCA"
s4= "AACCGGTTAA"
biologia(s3, s4)

s5 = "GGTACCGTGA"
s6 = "CGTGAACCTT"
biologia(s5, s6)

s7 = "AAGCTTACG"
s8 = "ACGTTCGA"
biologia(s7, s8)

s9 = "TTACGAGTACGCTAGT"
s10 = "ACGCTAGTCCGA"
biologia(s9, s10)
