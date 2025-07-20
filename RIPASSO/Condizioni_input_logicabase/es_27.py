def longest_unique_substrings(s: str) -> str:
    sottostringa_massima = ""
    for i in range(len(s)):
        sottostringa_corrente = ""
        for j in range(i, len(s)):
            if s[j] in sottostringa_corrente:
                break 
            else:
                sottostringa_corrente += s[j]
        if len(sottostringa_corrente) > len(sottostringa_massima):
            sottostringa_massima = sottostringa_corrente
    return sottostringa_massima 

print(longest_unique_substrings("abcabcbb"))
print(longest_unique_substrings("dreffvgbhjkl"))