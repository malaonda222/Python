class ContactManager:
    def __init__(self):
        self.contacts: dict[str, list[str]] = {}
    
    def create_contact(self, name: str, phone_numbers: list[str]) -> dict[str, list[str]]:
        '''Permette di creare un nuovo contatto da aggiungere alla rubrica'''
        if type(phone_numbers) != list:
            raise ValueError("Input non valido.")
        if name not in self.contacts:
            self.contacts[name] = phone_numbers
        else:
            raise ValueError("Errore: il contatto esiste già.")
        return {name: phone_numbers}
    
    def add_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:
        '''Permette di aggiungere un numero di telefono a un contatto'''
        if contact_name not in self.contacts:
            raise ValueError("Errore: il contatto non esiste nel dizionario.")
        if phone_number in self.contacts[contact_name]:
            raise ValueError("Errore: il numero di telefono non esiste.")
        self.contacts[contact_name].append(phone_number)
        return {contact_name: self.contacts[contact_name]}
    
    #oppure 
    #if contact_name in self.contacts:
        #if phone_number not in self.contacts[contact_name]:
            #self.contacts[contatc_name].append(phone_number)
        #else:
            #raise ValueError("Errore: il numero di telefono esiste già.")
    #else:
        #raise ValueError("Erore: il contatto non è all'interno del dizionario.")
    
    def remove_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:
        if contact_name not in self.contacts:
            raise ValueError("Errore: il contatto non esiste.")
        if phone_number not in self.contacts[contact_name]:
            raise ValueError("Errore: il numero di telefono non è presente.")
        self.contacts[contact_name].remove(phone_number)
        return {contact_name: self.contacts[contact_name]}
    
    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str) -> dict[str, list[str]]:
        if contact_name not in self.contacts:
            raise ValueError("Errore: il contatto non esiste.")
        if old_phone_number not in self.contacts[contact_name]:
            raise ValueError("Errore: il numero di telefono non è presente.")
        self.contacts[contact_name].remove(old_phone_number)
        self.contacts[contact_name].append(new_phone_number)
        return {contact_name: self.contacts[contact_name]}
    
    def list_contacts(self) -> list[str]:
        return list(self.contacts.keys())
        
    def list_phone_numbers(self, contact_name: str) -> list[str]:
        if contact_name not in self.contacts:
            raise ValueError("Errore: il contatto non esiste.")
        return self.contacts[contact_name]
    
    def search_contact_by_phone_number(self, phone_number: str) -> list[str]:
        contatti_trovati: list = []
        for contact, phone_numbers in self.contacts.items():
            if phone_number in phone_numbers:
                contatti_trovati.append(contact)
        
        if not contatti_trovati:
            raise ValueError("Errore: nessun contatto possiede questo numero di telefono.")
        
        return f"Il numero di telefono \"{phone_number}\" si trova nei seguenti contatti: {contatti_trovati}" 


if __name__ == "__main__":
    rubrica: ContactManager = ContactManager()
    rubrica.create_contact(name="Flavio", phone_numbers=["38475960887", "35475896999", "4785148965447"])
    rubrica.create_contact(name="Marco", phone_numbers=["38475960887", "589924566478"])
    rubrica.create_contact(name="Giovanni", phone_numbers=["38475960887", "4785148965447"])

    rubrica.add_phone_number("Flavio", "14526639998")

    print(rubrica.list_contacts())
    print(rubrica.list_phone_numbers("Flavio"))

    rubrica.remove_phone_number("Giovanni", "38475960887")
    print(rubrica.list_phone_numbers("Giovanni"))

    rubrica.update_phone_number("Marco", "589924566478", "53666654485")
    print(rubrica.list_phone_numbers("Marco"))

    print(rubrica.search_contact_by_phone_number("38475960887"))

    


    # rubrica.remove_phone_number("Flavio", "38475960887")

    # rubrica.remove_phone_number("Marco", "589924566478")

    # rubrica.update_phone_number("Flavio", "35475896999", "55669656584")
    # rubrica.update_phone_number("Flavio", "4785148965447", "46322569933")

    # print(rubrica.list_phone_numbers())

    # rubrica.list_phone_numbers("Giovanni")

    # rubrica.search_contact_by_phone_number("46322569933")
    # rubrica.search_contact_by_phone_number("38475960887")


    


    
    


    


