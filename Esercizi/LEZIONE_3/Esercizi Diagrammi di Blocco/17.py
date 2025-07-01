# Sistema di gestione delle temperature

import math 
t_max = -math.inf
day_max = 0
t_min = math.inf
day_min = 0
count_norma = 0
t_media = 0
i = 1

while i <= 7:
    temp = int(input("Inserisci una temperatura: "))
    t_media += temp
    if temp > t_max:
        t_max = temp
        day_max = i
    if temp < t_min:
        t_min = temp
        day_min = i 

    if temp >= 10 and temp <= 30:
        count_norma += 1
        if count_norma == 7: 
            print("Temperature nella norma.")
            i = i + 1
        else:
            i = i + 1
        
    else: 
        if temp < 5 or temp > 35:
            print("Allerta temperatura.")
            i = i + 1
        else:
            i = i + 1

t_media = t_media / 7
print(f"La temperatura media è: {t_media}.")
print(f"La temperatura massima è: {t_max}.")
print(f"La temperatura minima è: {t_min}.")
print(f"Il giorno con la temperatura più alta è: {day_max}.")
print(f"Il giorno con la temperatura più bassa è: {day_min}.")

