# User profile

# def build_profile(first_name: str, last_name: str, **kwargs) -> str:
#     output = f"{first_name} {last_name}, "
    
#     counter = 0 #serve sapere quale è l'ultima iterazione per non mettere la virgola
#     for key, value in kwargs.items():
#         output += f"{key} {value}"
#         if counter < len(kwargs) -1:
#             output += ", "
#         counter += 1

#     return output

# output = build_profile("Eric", "Crow", age=45, hair="brown", weight=72, height=180, eyes="blue")
# print(output)


# def build_profiles(nome, cognome, **infos):
#     profilo = (f"{nome} {cognome}")

#     for key, value in infos.items():
#         profilo += (f", {key} {value}")
#     return profilo

# profilo = build_profiles(f"Lisa", "Bandinelli", age=26, hair="black", weight=62)
# print(profilo)

# def info_utente(nome:str, cognome:str, **profiles):
#     profilo = (f"{nome}, {cognome}")
#     for key, value in profiles.items():
#         profilo += f", {key} {value}"
#     return profilo

# profilo_utente = info_utente("Virginia", "Bianchi", age=28, città="Firenze")
# print(profilo_utente)



def build_profile(nome: str, cognome: str, **kwargs):
    
    riepilogo = f"{nome} {cognome}"
    for key, value in kwargs.items():
        riepilogo += f", {key} {value}" 
    return riepilogo 

profilo_utente = build_profile("Lisa", "Bi", età=29, sport="pallavolo")
print(profilo_utente)
    
