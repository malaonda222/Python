my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
print(f"Original dictionary: {my_dict}")

#remove key-value pair
del my_dict["profession"]
print(f"Updated dictionary after removing 'profession': {my_dict}")

#get items
for key, value in my_dict.items():
    print(f"{key}: {value}")

def check_key_exists(dictionary, key_to_check):
    return key_to_check in dictionary

key1 = 'age'
print(f"Does the {key1} exist? {check_key_exists(my_dict, key1)}")