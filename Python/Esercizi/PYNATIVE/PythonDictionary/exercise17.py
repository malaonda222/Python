def invert_dictionary(input_dict):
    inverted_dict1 = {}
    for key, value in input_dict.items():
        inverted_dict1[value] = key
    return inverted_dict1

original_dict1 = {'a': 1, 'b': 2, 'c': 3}
print(original_dict1)
print(invert_dictionary(original_dict1))