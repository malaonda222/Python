class DeliveryManager:
    def __init__(self) -> None:
        self.deliveries: dict[str, dict] = {}
    
    def add_delivery(self, delivery_id: str, destinazione: str) -> dict | str:
        if delivery_id in self.deliveries:
            return "Errore: spedizione già registrata"
        else:
            self.deliveries[delivery_id] = {"destinazione": destinazione, "inviato": False}
            return {delivery_id: self.deliveries[delivery_id]}
        
    def mark_as_sent(self, delivery_id: str) -> dict | str:
        if delivery_id not in self.deliveries:
            return "Errore: spedizione non trovata."
        else:
            self.deliveries[delivery_id]["inviato"] = True 
            return {delivery_id: self.deliveries[delivery_id]}
        
    def update_destination(self, delivery_id: str, nuova_destinazione: str) -> dict | str:
        if delivery_id not in self.deliveries:
            return "Errore: spedizione non trovata."
        else:
            self.deliveries[delivery_id]["destinazione"] = nuova_destinazione
            return {delivery_id: self.deliveries[delivery_id]}
        
    def cancel_delivery(self, delivery_id: str) -> dict | str:
        if delivery_id not in self.deliveries:
            return "Errore: spedizione non trovata."
        else:
            self.deliveries[delivery_id]["inviato"] = False 
            return {delivery_id: self.deliveries[delivery_id]}
    
    def remove_delivery(self, delivery_id: str) -> dict | str:
        if delivery_id not in self.deliveries:
            return "Errore: spedizione non trovata."
        else:
            rimossa = self.deliveries.pop(delivery_id)
            return {delivery_id: rimossa}
        
    def list_deliveries(self) -> list[str]:
        return list(self.deliveries.keys())
    
    def get_delivery(self, delivery_id: str) -> dict | str:
        if delivery_id not in self.deliveries:
            return "Errore: spedizione non trovata."
        else:
            return {delivery_id: self.deliveries[delivery_id]}
        

d = DeliveryManager()
 
print(d.add_delivery("D001", "Milano"))
print(d.add_delivery("D002", "Roma"))
print(d.mark_as_sent("D001"))
print(d.update_destination("D002", "Napoli"))
print(d.cancel_delivery("D001"))
print(d.get_delivery("D001"))
print(d.remove_delivery("D002"))
print(d.list_deliveries())