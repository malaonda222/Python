sum:int = 0
for x in range (1, 11):
    sum+=x
print(f"La somma dei numeri da 1 a 10 è: {sum}")

sum:int = 0
for x in range (20, 38):
    sum+=x
print("La somma dei numeri da 20 a 37 è", sum)

sum:int = 0
for x in range (35, 50):
    sum+=x
print(f"La somma dei numeri da 35 a 49 è: {sum}")

# Funzione per calcolare la somma tra due numeri interi
def sum(a:int, b:int):
    result:int = 0
    for i in range(a, b+1):
        result = result+i
    return result

mysum = sum(1, 10)
print(f"Sum from 1 to 10 is: {sum(1, 10)}")
print(f"Sum from 20 to 37 is: {sum(20, 37)}")
print(f"Sum from 35 to 50 is: {sum(35, 50)}")