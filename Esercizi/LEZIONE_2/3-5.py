#Changing Guest List
my_list = ["Rebecca", "Gianni", "Oriol"]
guest_remove = my_list[1]
print(f"The guest that can't make the dinner is: {guest_remove}")

my_list.pop(1)
print(my_list)

my_list.append("Miriam")
print(my_list)

for item in my_list:
    print(f"You're invited for dinner, {item}")
    