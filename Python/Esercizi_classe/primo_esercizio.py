'''Inserire 6 numeri interi scelti dall'utente,
di questi sei numeri sommare solo i numeri pari'''

#Modo I (while)
print("Modo I while: ")
i:int = 1 
somma:int = 0
while i <= 6:
    #inserire un numero
    n:int = int(input("Digita un numero: "))
    if n % 2 == 0:
        somma += n
    i = i + 1 

print(f"somma: {somma}")

#Modo II (for)
print("Modo II for")
somma:int = 0
for i in range(6):
    n:int = int(input("Digitare un numero: "))
    if n % 2 == 0:
        somma += n
print(f"somma:{somma}")