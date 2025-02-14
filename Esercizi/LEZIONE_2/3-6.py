#More Guests
my_list = ["Rebecca", "Miriam", "Oriol"]
my_list.extend(["Flavio", "Giuseppe", "Giordano"])
print(my_list)

print(f"A cena adesso saremo in 6: {my_list}")
my_list.insert(0, "Lisa")
my_list.insert(3, "Dante")
my_list.append("Michelangelo")

feminine: list = ["lisa", "rebecca", "miriam"]
print(my_list)

for nome in my_list:
    final = "a" if nome.lower() in feminine else "o"
    print(f"Ciao {nome}, sei invitat{final} per cena venerdì 20/07!")
# b = sorted(a)