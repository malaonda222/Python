from string import punctuation

def count_unique_words(text: str) -> dict[str, int]:
    punteggiatura = ".,;:!?()[]{}\"'`«»<>-_—…"
    tokens = text.split(" ")
    new_dict:dict[str, int] = {}
    for token in tokens:
        new_token = token.lower().strip(punteggiatura)
        if new_token == "":
            continue
        if new_token not in new_dict:
            new_dict[new_token] = 1
        else:
            new_dict[new_token] += 1
    return new_dict

# text1 = "Oggi è una bella giornata; quando è una bella giornata, usciamo per una passeggiata."
# print(count_unique_words(text1))

# text2 = "Python è un linguaggio di programmazione. La programmazione in Python è interessante."
# print(count_unique_words(text2))


def count(text: str) -> dict[str, int]:
    d: dict[str, int] = {}
    l_text: str = text.lower()
    tokens: list[str] = l_text.split(" ")
    for token in tokens:
        c_token: str = ""
        for c in token:
            if c.isalpha() or c.isdigit():
                c_token += c
        if not c_token:
            continue
        if c_token in d:
            d[c_token] += 1
        else:
            d[c_token] = 1
    return d 

text3 = "Oggi è una bella giornata; quando è una bella giornata, usciamo per una passeggiata."
print(count(text3))

text4 = " "
print(count(text4))






def frequenza(stringa: str) -> dict[str, int]:
    punteggiatura = ".,;:!?()[]{}\"'`«»<>-_—…"
    new_dict1: dict[str, int] = {}
    tokens = stringa.split(" ")
    for token in tokens:
        new_token = token.lower().strip(punteggiatura)
        if new_token == "":
            continue 
        if new_token not in new_dict1:
            new_dict1[new_token] = 1
        else:
            new_dict1[new_token] += 1
    return new_dict1

text10 = "Hello, world! Hello... PYTHON? world."
print(frequenza(text10))