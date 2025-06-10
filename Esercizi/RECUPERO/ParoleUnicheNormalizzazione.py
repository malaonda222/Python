def count_unique_words(text: str) -> dict[str, int]:
    punteggiatura = ".,;:!?()[]{}\"'`«»<>-_—…"
    tokens = text.split()
    new_dict = {}
    for token in tokens:
        new_token = token.lower().strip(punteggiatura)
        if new_token == "":
            continue
        if new_token not in new_dict:
            new_dict[new_token] = 1
        else:
            new_dict[new_token] += 1
    return new_dict

text1 = "Oggi è una bella giornata; quando è una bella giornata, usciamo per una passeggiata."
print(count_unique_words(text1))

text2 = "Python è un linguaggio di programmazione. La programmazione in Python è interessante."
print(count_unique_words(text2))