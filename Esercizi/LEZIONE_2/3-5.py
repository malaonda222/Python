#Changing Guest List
my_list = ["Marco", "Gianni", "Oriol"]
guest_remove = my_list[1]
print(f"The guest that can't make the dinner is: {guest_remove}")

my_list.pop(1)
print(my_list)

my_list.append("Silvio")
print(my_list)

my_list.insert[0] = "Carlo"
print(f"{my_list[0]} sei invitato a cena")
print(f"{my_list[1]} sei invitato a cena")
print(f"{my_list[2]} sei invitato a cena")

for item in my_list:
    print(f"You're invited for dinner, {item}")
    