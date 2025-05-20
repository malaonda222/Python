#l = [1, 5, 9, 10]
#x = l.pop() # toglie il valore e lo restituisce
#print(x)

#x = l.remove(5)# toglie il valore e non restituisce niente
#print(x)
#print(l)

#if 5 in l:
    #l.remove(5)

l = [1, 5, 9, 10, 16, 98, "a"]
#for i in range(len(l)-1, -1, -1):
    #print(i) 
for i in range(len(l)-1, -1, -1):
    print(f"Sto rimuovendo l'elemento all'indice {i}")
    l.remove(l[i])

while len(l) > 0:
    x = l.pop()
    print("Ho rimosso", x)


l = [1, 5, 9, 10, 16, 98, "a"]

# Funzione .get

#1. Quando la chiave esiste
diz = {1:"a", 2:"b", 3:"c"}
print(diz.get(1))

#2. Quando la chiave non esiste
diz = {1:"a", 2:"b", 3:"c"}
print(diz.get(4))

#3. Quando la chiave non esiste e si passa un valore di default
diz = {1:"a", 2:"b", 3:"c"}
print(diz.get(4,"Chiave non esistente"))


# Funzione .union
