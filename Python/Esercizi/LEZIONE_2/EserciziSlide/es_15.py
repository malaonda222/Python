alphabet = ["a", "b", "c", "d", "e"]
first_letter = [0]
last_letter = [-1]

first_three = alphabet[:3]
last_three = alphabet[-3:]

alphabet.append("f")
alphabet.append("g")
alphabet.append("h")
last_three = alphabet[-3:]
alphabet.pop(-1) 
# oppure alphabet.remove("h")
print(alphabet)