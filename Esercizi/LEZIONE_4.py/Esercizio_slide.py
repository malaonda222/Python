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

# funzione
def sum(a:int, b:int):
    result:int = 0
    for i in range(a, b+1):
        result = result+i
    return result

mysum = sum(1, 10)
print(f"Sum from 1 to 10 is: {sum(1, 10)}")
print(f"Sum from 20 to 37 is: {sum(20, 37)}")
print(f"Sum from 35 to 50 is: {sum(35, 50)}")


def subtract(c:int, d:int):
    sottrazione:int = c - d
    return sottrazione

myresult = subtract(4, 1)
print(myresult) #oppure print(subtract(4, 1))
print(f"Subtract between the two values is: {subtract(10, 4)}")
print(subtract(int(input("Inserisci il primo numero: ")), int(input("Inserisi il secondo numero: "))))

def hello() -> None:
    print("Hello")

hello()
print(type(hello()))

def operations(a:int, b:int) -> tuple[int, int]:
    sum_result:int = a+b 
    diff_result:int = a-b 
    return sum_result, diff_result

sum_value, diff_value = operations(10, 5)
print("Sum:", sum_value)
print("Difference", diff_value)
