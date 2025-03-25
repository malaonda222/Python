'''Scrivi una funzione chiamata calsius_to_fahrenheit che converte una temperatura da 
gradi Celsius a Fahrenheit. Formula: F = (C*9.5) + 32'''

def celsius_to_fahrenheit(celsius:int):
    fahrenheit = (celsius*(9/5)) + 32
    return fahrenheit

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))
