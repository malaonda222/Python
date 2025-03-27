'''Esercizio 10'''

def merge_dictionaries(dict1:dict, dict2:dict) -> dict:
    dict3 = dict(dict1, **dict2)
    for key, value in dict3.items():
        if key in dict1 and key in dict2:
            dict3[key] = dict1[key] + dict2[key]
    return dict3



def merge_dictionaries(dict1:dict, dict2:dict) -> dict:

    for key, value in dict2.items():
        if key in dict1:
            dict1[key] += value 
        else:
            dict1[key] = value 
    return dict1

print(merge_dictionaries({'x': 5, 'y': 10, 'z' : 4}, {'x': 7, 'y' : 3, 'c' : 31}))








        
