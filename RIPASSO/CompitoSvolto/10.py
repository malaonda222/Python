'''Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall'utente.

Il programma deve:

1. acquisire una sequenza di numeri interi, terminando l'inserimento quando l'utente digita 0 (che non deve essere considerato nei calcoli);
2. calcolare e visualizzare la somma di tutti i numeri pari inseriti;
3. calcolare e visualizzare la media di tutti i numeri dispari inseriti;
4. determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista); 
5. se più numeri hanno la stessa frequenza massima, visualizzarli tutti.

Output:
Somma dei numeri pari: 10
Media dei numeri dispari: 5.67
Numero più frequente: 7 (2 volte)'''

# lista_numeri = []
# while True:
#     valore = float(input("Inserisci un numero intero: "))
#     if valore % 1 != 0:
#         print("Errore. Inserire un numero intero")
#     if valore == 0:
#         break 
#     else:
#         valore = int(valore)
#         lista_numeri.append(valore)

lista_numeri = []
somma_pari = 0
somma_dispari = 0
lista_dispari = []

while True:
    valore = input("Inserisci un numero intero: ")
    try:
        valore = int(valore)
        if valore == 0:
            break
        else:
            lista_numeri.append(valore)
    except ValueError:
        print("Inserire un numero intero")
print(lista_numeri)

for numero in lista_numeri:
    if numero % 2 == 0:
        somma_pari += numero
    else:
        somma_dispari += numero
        lista_dispari.append(numero)

if len(lista_dispari) > 0:
    media = somma_dispari / len(lista_dispari)
else:
    media = 0

frequenze = {}
for numero in lista_numeri:
    if numero not in frequenze:
        frequenze[numero] = 1
    else:
        frequenze[numero] += 1 
max_frequenza = max(frequenze.values())


numeri_frequenti = []
for num, freq in frequenze.items():
    if freq == max_frequenza:
        numeri_frequenti.append(num)

print(f"Somma dei numeri pari: {somma_pari}")
print(f"Media dei numeri dispari: {media:.2f}")
print(f"Numero più frequente: {numeri_frequenti} ({max_frequenza} volte)")
