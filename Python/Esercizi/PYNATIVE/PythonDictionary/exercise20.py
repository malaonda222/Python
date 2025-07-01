def unique_values(input_dict):
    values = list(input_dict.values())
    return len(values) == len(set(values))



dict1 = {'a': 1, 'b': 2, 'c': 3} 
print(unique_values(dict1))

dict2 = {'x': 10, 'y': 20, 'z': 10} 
print(unique_values(dict2))

dict3 = {}
print(unique_values(dict3))
