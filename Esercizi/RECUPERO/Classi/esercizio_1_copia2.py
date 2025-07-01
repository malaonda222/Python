class ContactManager:
    def __init__(self) -> None:
        self.contacts = dict[str, list[str]]

    def create_contact(self, name: str, phone_numbers: list[str]) -> dict[str, list[str]]:
        if type(phone_numbers) != list:
            raise ValueError("Input non valido.")
        if name not in self.contacts:
            self.contacts[name] = phone_numbers
        else:
            raise ValueError("Il contatto esiste già.")
        return {name: phone_numbers}

    def add_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:
        if type(phone_number) != str:
            raise ValueError("Input non valido. Inserire una stringa.")
        if contact_name in self.contacts:
            if phone_number not in self.contacts[phone_number]:
                self.contacts[contact_name].append(phone_number)
            else:
                raise ValueError("Il numero di telefono esiste già.")
        else:
            raise ValueError("Il contatto non esiste.")
        return {contact_name: self.contacts[contact_name]}    

    def remove_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:
        if not isinstance(phone_number, str):
            raise ValueError("Il numero deve essere una stringa.")
        if contact_name in self.contacts:
            if phone_number in self.contacts[contact_name]:
                self.contacts[contact_name].remove(phone_number)
            else:   
                raise ValueError("Errore: il numero di telefono non è presente.")
        else:
            raise ValueError("Errore: il contatto non esiste.")
        return {contact_name: self.contacts[contact_name]}
    
    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number) -> dict[str, list[str]]:
        if not isinstance(old_phone_number, str) or not isinstance(new_phone_number, str):
            raise ValueError("Entrambi i numeri di telefono devono essere stringhe.")
        if contact_name in self.contacts:
            if old_phone_number in self.contacts[contact_name]:
                self.contacts[contact_name].remove(old_phone_number)
                if new_phone_number not in self.contacts[contact_name]:
                    self.contacts[contact_name].append(new_phone_number)
                else:
                    raise ValueError("Il nuovo numero che vuole inserire esiste già.")
            else:
                raise ValueError("Errore: il numero di telefono non è presente.")
        else:
            raise ValueError("Errore: il contatto non esiste.")
        return {contact_name: self.contacts[contact_name]}
    
    def list_contacts(self) -> list[str]:
        lista_chiavi = []
        for key in self.contacts.keys():
            lista_chiavi.append(key)
        return lista_chiavi
    
    def list_phone_numbers(self, contact_name: str) -> list[str]:
        if contact_name not in self.contacts:
            raise ValueError("Errore: il contatto non esiste.")
        else:
            return self.contacts[contact_name]
        
    def search_contact_by_phone_number(self, phone_number: str) -> list[str]:
        contatti_trovati = []
        for contact, phone_numbers in self.contacts.items():
            if phone_number in phone_numbers:
                contatti_trovati.append(contact)
        if not contatti_trovati:
            raise ValueError("Nessun contatto trovato con questo numero di telefono.")
        
        return contatti_trovati
    
