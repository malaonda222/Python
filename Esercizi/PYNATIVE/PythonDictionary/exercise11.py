sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

new_dict = {}

for key in keys:
    new_dict.update({key: sample_dict[key]})
print(new_dict)

