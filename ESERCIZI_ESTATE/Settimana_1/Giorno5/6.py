'''Logica: Scrivi una funzione che verifica se un numero è primo.'''


def verifica_se_primo() -> str:
    try:
        n = int(float(input("Inserisci un numero: ")))
        if n <= 1:
            print("Errore. Il numero non è primo!")
        for i in range(2, int(n**0.5) +1):
            if n % i == 0:
                return "Il numero non è primo"
        return "Numero primo"
    except ValueError:
        print("Il valore deve essere un numero!")

    
    
print(verifica_se_primo())


