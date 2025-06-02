def conta_caratteri_frequenti(input_string):
    my_dict = {}
    for item in input_string:
        my_dict[item] = my_dict.get(item, 0) + 1
    return my_dict

string1 = 'Jessa'
string2 = "Massimiliano"
print(conta_caratteri_frequenti(string1))
print(conta_caratteri_frequenti(string2))


