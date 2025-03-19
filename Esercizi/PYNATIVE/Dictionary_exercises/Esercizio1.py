# Convert two list into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res_dict = dict(zip(keys, values))
print(res_dict)




nomi = ["Lisa", "Elena", "Miriam"]
età = 28, 27, 18

# risultato = dict(zip(nomi, età))
# print(risultato)

risultato1 = dict()
for i in range(len(nomi)):
    risultato1.update({nomi[i]: età[i]})

print(risultato1)