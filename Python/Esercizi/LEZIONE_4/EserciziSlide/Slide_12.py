# Funzione per calcolare la sottrazione tra due numeri interi

def subtract(c:int, d:int):
    sottrazione:int = c - d
    return sottrazione

myresult = subtract(4, 1)
print(myresult) #oppure print(subtract(4, 1))
print(f"Subtract between the two values is: {subtract(10, 4)}")
print(subtract(int(input("Inserisci il primo numero: ")), int(input("Inserisi il secondo numero: "))))
