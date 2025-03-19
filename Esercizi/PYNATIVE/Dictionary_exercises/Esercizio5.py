# Extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract:
keys = ["name", "salary"]

for key, value in sample_dict.items():
    if key == "name" or key == "salary":
        print(f"Chiave: {key}, Valore: {value}")

newDict = {k: sample_dict[k] for k in keys}
print(newDict)

result = dict()
for k in keys:
    result.update({k: sample_dict[k]})
print(result)