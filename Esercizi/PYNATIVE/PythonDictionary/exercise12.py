sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

for key in keys:
    if key in sample_dict:
        sample_dict.pop(key)
print(sample_dict)
