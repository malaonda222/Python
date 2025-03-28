def vowelsCounter(my_string:str) -> int:
    if my_string == "":
        return 0
    else:
        if my_string[0] == "a" or my_string[0] == "e" or my_string[0] == "i" or my_string[0] == "o" or my_string[0] == "u":
        #oppure: if my_string[0] in "aeiouAEIOU" 
            return 1 + vowelsCounter(my_string[1:])
        else:
            return vowelsCounter(my_string[1:])
    
print(vowelsCounter("aiuto"))
print(vowelsCounter("servire"))
print(vowelsCounter("terriero"))