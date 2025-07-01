numeri = [5, 2, 9, 1, 5, 6]

numeri.sort()
print("Crescente:", numeri)

numeri.sort(reverse=True)
print("Descrescente:", numeri)

print("-------------------------------")

parole = ["Python", "è", "facile", "da", "imparare"]
parole.reverse()
print(parole)

invertita = parole[::-1]
print(invertita)

print("--------------------------------")

frutti = ["mela", "banana", "ciliegia"]
frutti.append("arancia")
print(frutti)
frutti.remove("banana")
print(frutti)
frutti.pop(-1)
print(frutti)

print("--------------------------------")

colori = ["rosso", "verde", "blu", "giallo", "viola"]
print(colori[:3])
print(colori[-2:])

print("--------------------------------")

a = [3, 1, 4]
b = [5, 2, 0]
c = a + b 
c.sort()
print(c)