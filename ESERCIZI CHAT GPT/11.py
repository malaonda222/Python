def word_frequency(text: str) -> dict:
    my_dict = {}
    parole = text.split()
    for parola in parole:
        if parola not in my_dict:
            my_dict[parola] = 1 
        else:
            my_dict[parola] += 1 
    return my_dict 

print(word_frequency("ciao mondo ciao"))



