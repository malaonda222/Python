'''Write a function check_length(), which takes a string as an argument.
Using if / else, check if the length of the string is bigger, smaller, or equal to 10 characters.'''

def check_lenght(stringa:str):
    if len(stringa)>10:
        print(f"La stringa \"{stringa}\" is longer than 10 characters")
    elif len(stringa)<10:
        print(f"La stringa \"{stringa}\" is shorter than 10 characters")
    else:
        print(f"La stringa \"{stringa}\" is 10 characters long")

check_lenght(input(f"Insert a string: "))
