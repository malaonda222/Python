'''Definisci una prima funzione chiamata create_contact che prende in input il nome di una persona (obbligatorio), l’indirizzo email (opzionale) 
e il numero di telefono (opzionale). La funzione deve restituire un dizionario contenente le seguenti chiavi: "profile" (associata al nome), "email" e "telefono". 
Se email o telefono non vengono forniti, il loro valore sarà None.

Definisci poi una seconda funzione chiamata update_contact che prende in input un dizionario contenente un contatto, il nome del contatto (solo come riferimento, 
non deve essere modificato), un nuovo indirizzo email (opzionale) e un nuovo numero di telefono (opzionale). La funzione deve aggiornare il dizionario solo 
se vengono forniti nuovi valori per email o telefono, e restituire il dizionario aggiornato.'''


def create_contact(nome: str, email = None, telefono = None) -> dict[str]:
    dizionario: dict = {
        "profile": nome,
        "email": email, 
        "telefono": telefono
    }
    return dizionario

def update_contact(dizionario: dict, nome: str, email: str = None, telefono: str = None) -> dict[str]:
    if dizionario.get("profile") == nome:
        if email is not None:
            dizionario["email"] = email 
        if telefono is not None:
            dizionario["telefono"] = telefono
    else:
        return f"Il profilo {nome} non è presente nella lista dei contatti"
    return dizionario

contatto = create_contact("Mario Rossi", "mario@gmail.com", None)
print((contatto))
print(update_contact(contatto, "Mario Rossi", telefono="05519896256"))
