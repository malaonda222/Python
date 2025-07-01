class ContactManager:
    def __init__(self, contacts: dict[str, list[str]] = None):
        if contacts is None:
            contacts = {}
        self.contacts = contacts 

    def create_contact(self, name: str, phone_numbers: list[str]):
        if name in self.contacts:
            raise ValueError("Errore: il contatto esiste già.")
        else:
            self.contacts[name] = phone_numbers
            return {name: phone_numbers}

    def add_phone_number(self, contact_name: str, phone_number: str):
        if contact_name not in self.contacts:
            raise ValueError("Errore: il contatto non esiste.")
        if phone_number in self.contacts[contact_name]:
            raise ValueError("Errore: il numero di telefono esiste già.")
        self.contacts[contact_name].append(phone_number)
        return {contact_name: self.contacts[contact_name]}
            
    def remove_phone_number(self, contact_name: str, phone_number: str):
        if contact_name not in self.contacts:
            raise ValueError("Errore: il contatto non esiste.")
        if phone_number not in self.contacts[contact_name]:
            raise ValueError("Errore: il numero di telefono non è presente.")
        self.contacts[contact_name].remove(phone_number)
        return {contact_name: self.contacts[contact_name]}
    
    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str):
        if contact_name not in self.contacts:
            raise ValueError("Errore: il contatto non esiste.")
        if old_phone_number not in self.contacts[contact_name]:
            raise ValueError("Errore: il numero di telefono non è presente.")
        self.contacts[contact_name].remove(old_phone_number)
        self.contacts[contact_name].append(new_phone_number)
        return {contact_name: self.contacts[contact_name]}
    
    def list_contacts(self): 
        if not self.contacts:
            return "La lista dei contatti è vuota."
        else:
            return list(self.contacts.keys()) 
    
    def list_phone_numbers(self, contact_name: str) -> list[str]:
        if contact_name not in self.contacts:
            raise ValueError("Errore: il contatto non esiste.")
        else:
            return self.contacts[contact_name]
    
    def search_contact_by_phone_number(self, phone_number: str):
        contatti_trovati: list = []
        for nome, numeri in self.contacts.items():
            if phone_number == numeri:
                contatti_trovati.append({nome: numeri})
            
        if not contatti_trovati:
            raise ValueError("Errore: nessun contatto trovato con questo numero di telefono.")
          
        return contatti_trovati