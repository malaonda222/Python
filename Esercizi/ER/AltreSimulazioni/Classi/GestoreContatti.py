'''Esercizio: Gestore di Contatti (ContactManager)

Scrivi una classe chiamata ContactManager che gestisca una rubrica di contatti.

Ogni contatto ha:
nome (stringa)
telefono (stringa)
email (stringa)

La classe deve fornire i seguenti metodi:

add_contact(contact_id: str, nome: str, telefono: str, email: str) -> dict | str
➤ Aggiunge un contatto nuovo.
Se contact_id è già presente, restituisce "Errore, contatto già esistente."

update_phone(contact_id: str, nuovo_telefono: str) -> dict | str
➤ Modifica il numero di telefono di un contatto.
Se il contatto non esiste, restituisce "Errore, contatto non trovato."

update_email(contact_id: str, nuova_email: str) -> dict | str
➤ Modifica l’email del contatto.

remove_contact(contact_id: str) -> dict | str
➤ Rimuove un contatto e restituisce i suoi dati.
Se non trovato, restituisce "Errore, contatto non trovato."

get_contact(contact_id: str) -> dict | str
➤ Restituisce il contatto richiesto.

list_contacts() -> list[str]
➤ Restituisce la lista degli ID dei contatti salvati.

find_by_name(nome: str) -> dict | str
➤ Restituisce tutti i contatti che corrispondono al nome indicato (puoi anche cercare in modo case-insensitive).
'''

class ContactManager:
    def __init__(self) -> None:
        self.contacts: dict[str, dict] = {}
    
    def add_contact(self, contact_id: str, nome: str, telefono: str, email:str) -> dict|str:
        if contact_id in self.contacts:
            return f"Errore. Contatto con ID {contact_id} già presente nella lista dei contatti"
        else:
            self.contacts[contact_id] = {"nome": nome, "telefono": telefono, "email": email}
            return {contact_id: self.contacts[contact_id]}
    
    def update_phone(self, contact_id: str, nuovo_telefono: str) -> dict|str:
        if contact_id not in self.contacts:
            return f"Il contatto con ID {contact_id} non è presente nei contatti"
        else:
            self.contacts[contact_id]["telefono"] = nuovo_telefono
            return {contact_id: self.contacts[contact_id]}
        
    def remove_contact(self, contact_id: str) -> dict|str:
        if contact_id not in self.contacts:
            return f"Il contatto con ID {contact_id} non è presente nei contatti"
        else:
            rimosso = self.contacts.pop(contact_id)
            return {contact_id: rimosso}
    
    def get_contact(self, contact_id: str) -> dict|str:
        if contact_id not in self.contacts:
            return f"Il contatto con ID {contact_id} non è presente nei contatti"   
        else:
            return {contact_id: self.contacts[contact_id]}
    
    def list_contacts(self) -> list[str]:
        if not self.contacts:
            return []
        else:
            return list(self.contacts.keys())

    def find_by_name(self, nome: str) -> dict|str:
        if not self.contacts:
            return "Non è presente nessun contatto"
        else:
            dizionario_contatti = {}
            for contact_id, contatto in self.contacts.items():
                if contatto["nome"].lower() == nome.lower():
                    contatto_trovato = {contact_id: self.contacts[contact_id]}
                    dizionario_contatti.update(contatto_trovato)
                # oppure 
                # dizionario_contatti[contact_id] = contatto
            if dizionario_contatti:
                return dizionario_contatti
            else:
                return "Nessun contatto trovato con questo nome"
            

manager = ContactManager()
 
manager.add_contact("c001", "Mario", "3331234567", "mario@email.it")
manager.add_contact("c002", "Lucia Bianchi", "3459876543", "lucia@email.it")
manager.add_contact("c003", "mario", "3209999999", "m.verdi@email.it")
 
print(manager.find_by_name("mario"))


    