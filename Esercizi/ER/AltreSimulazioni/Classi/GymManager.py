class GymManager:
    def __init__(self) -> None:
        self.attrezzature: dict[str, dict] = {}
        self.membri: dict [str, dict] = {}

    def add_member(self, member_id: str, nome: str, email: str, iscrizione: str, abbonamento_attivo: bool = True) -> dict|str:
        if member_id in self.membri:
            return "Errore, membro già registrato." 
        else:
            self.membri[member_id] = {"nome": nome, "email": email, "iscrizione": iscrizione, "abbonamento attivo": abbonamento_attivo}
            return {member_id: self.membri[member_id]}
    
    def remove_member(self, member_id: str) -> dict|str:
        if member_id not in self.members:
            return "Errore, membro non trovato"
        else:
            rimosso = self.membri.pop(member_id)
            return {member_id: rimosso}
    
    def update_membership(self, member_id: str, abbonamento_attivo: bool) -> dict|str:
        if member_id not in self.membri:
            return "Errore, membro non trovato"
        else:
            self.membri[member_id]["abbonamento attivo"] = abbonamento_attivo
            return {member_id: self.membri[member_id]}
    
    def add_equipment(self, equipment_id: str, nome: str, quantita: int) -> dict|str:
        if equipment_id in self.attrezzature:
            return "Errore, attezzatura già presente"
        else:
            self.attrezzature[equipment_id] = {"nome": nome, "quantita": quantita, "disponibile": quantita}
            return {equipment_id: self.attrezzature[equipment_id]}

    def remove_equipment(self, equipment_id: str) -> dict|str:
        if equipment_id in self.attrezzature:
            return "Errore, attrezzatura non trovata"
        else:
            rimossa = self.attrezzature.pop(equipment_id)
            return {equipment_id: rimossa}
    
    def update_equipment(self, equipment_id: str, nuova_quantita: int) -> dict|str:
        if equipment_id not in self.attrezzature:
            return "Errore, attrezzatura non trovata"
        else:
            self.attrezzature[equipment_id]["quantita"] = nuova_quantita
            return {equipment_id: self.attrezzature[equipment_id]}
    
    def list_members(self) -> list[str]:
        return list(self.membri.keys())
    
    def list_equipments(self) -> list[str]:
        return list(self.attrezzature.keys())
    
    def find_member_by_name(self, nome: str) -> dict|str:
        if not self.membri:
            return "La lista dei contatti è vuota"
        else:
            risultati = {}
            for member_id, membro in self.membri.items():
                if membro["nome"].lower() == nome.lower():
                    risultati[member_id] = membro 
            if not risultati:
                return "Nessun membro trovato con questo nome"
            else:
                return risultati
    
    def find_equipment_by_name(self, nome: str) -> dict|str:
        if not self.attrezzature:
            return "La lista delle attrezzature è vuota"
        else:
            risultati = {}
            for equipment_id, equipment in self.attrezzature.items():
                if equipment["nome"].upper() == nome.upper():
                    risultati[equipment_id] = equipment
            if not risultati:
                return "Nessuna attrezzatura trovata con questo nome"
            else:
                return risultati 
            