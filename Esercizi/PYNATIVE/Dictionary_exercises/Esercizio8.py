# Rename a key of a dictionary
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sample_dict.pop("city")
print(sample_dict)

sample_dict["location"] = "New York"
print(sample_dict)