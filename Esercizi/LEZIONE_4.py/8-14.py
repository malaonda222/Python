# # Cars
# def car(manufacturer:str, model:str, **kwargs):
#     output = {
#         "manufacturer": manufacturer,
#         "model": model
#     }
    
#     for key, value in kwargs.items():
#         output[key] = value
        
#     return output

# my_car = car(f"Fiat", "500", colour="red", tow_package=True)
# print(my_car)

# your_car = car(f"Kia", "Rio", colour="black", tow_package=False)
# print(your_car)





def automobile(produttore:str, modello: str, **kwargs):
    macchina = {
        "manufacturer": produttore,
        "model": modello
}
    for key, value in kwargs.items():
        macchina[key] = value
    return macchina
    
my_car = automobile("Volkswagen", "A1", colour="black", tow_package=True)
print(my_car)