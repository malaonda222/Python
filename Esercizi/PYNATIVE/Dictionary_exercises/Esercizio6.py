sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)


sample_dict = {k: sample_dict[k] for k in sample_dict.keys() - keys}
print(sample_dict)


for key, value in sample_dict.items():
    if key == "name" or key == "salary":
        sample_dict.pop()
    print(sample_dict)