#Shrinking Guest List
my_list = ["Lisa", "Rebecca", "Miriam", "Dante", "Oriol", "Michelangelo"]
print(f"Cari {my_list}, purtroppo non abbiamo spazio per tutti, solo due persone potranno venire a cena")

guest_removed_1 = my_list.pop(2)
print(f"Purtroppo {guest_removed_1}, non sei tra gli invitati a cena!")

guest_removed_2 = my_list.pop(1)
print(f"Purtroppo {guest_removed_2}, non sei tra gli invitati a cena!")

guest_removed_3 = my_list.pop(2)
print(f"Purtroppo {guest_removed_3}, non sei tra gli invitati a cena!")

guest_removed_4 = my_list.pop(-1)
print(f"Purtroppo {guest_removed_4}, non sei tra gli invitati a cena!")

print(my_list)
for nome in my_list:
    print(f"Caro {nome} ci vediamo venerdì a cena!")

    
