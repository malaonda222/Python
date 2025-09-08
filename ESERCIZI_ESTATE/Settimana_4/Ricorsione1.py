def rec_fattoriale(n: int) -> int:
    if n == 0:
        return 1
    if n < 0:
        return "Errore"
    else:
        return (n * rec_fattoriale(n - 1))

print(rec_fattoriale(5))
print(rec_fattoriale(-5))
