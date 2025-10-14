class SlideTicket:
    def __init__(self, ticket_id: str, slide_name: str, time_slot: str) -> None:
        self.ticket_id: str = ticket_id
        self.slide_name: str = slide_name
        self.time_slot: str = time_slot
        self.is_reserved: bool = False 
    
    def reserve(self) -> None:
        if not self.is_reserved:
            self.is_reserved = True 
        else:
            print(f"Il biglietto per lo scivolo '{self.slide_name}' alle '{self.time_slot}' è già riservato.")
        
    def cancel(self) -> None:
        if self.is_reserved:
            self.is_reserved = False 
        else:
            print(f"Il biglietto per lo scivolo '{self.slide_name}' alle '{self.time_slot}' non risulta riservato.")
        

class Visitor:
    def __init__(self, visitor_id: str, name: str) -> None:
        self.visitor_id: str = visitor_id
        self.name: str = name 
        self.reserved_tickets: list[SlideTicket] = []

    def reserve_ticket(self, ticket: SlideTicket) -> None:
        if not ticket.is_reserved:
            self.reserved_tickets.append(ticket)
            ticket.reserve()
        else:
            return f"Il biglietto per lo scivolo '{ticket.slide_name}' non è disponibile."

    def cancel_ticket(self, ticket: SlideTicket) -> None:
        if ticket in self.reserved_tickets:
            self.reserved_tickets.remove(ticket)
            ticket.cancel()
        else:
            print(f"Il biglietto per lo scivolo '{ticket.slide_name}' non è stato riservato da questo visitatore.")


class WaterPark:
    def __init__(self) -> None:
        self.tickets: dict[str, SlideTicket] = {}
        self.visitors: dict[str, Visitor] = {}

    def add_ticket(self, ticket_id: str, slide_name: str, time_slot: str) -> None:
        if ticket_id in self.tickets:
            print(f"l biglietto con ID '{ticket_id}' esiste già.")
        else:
            self.tickets[ticket_id] = SlideTicket(ticket_id, slide_name, time_slot)
            return {ticket_id: self.tickets[ticket_id]}

    def register_visitor(self, visitor_id: str, name: str) -> None:
        if visitor_id in self.visitors:
            print(f"Il visitatore con ID '{visitor_id}' è già registrato.")
        else:
            self.visitors[visitor_id] = Visitor(visitor_id, name)
            return {visitor_id: self.visitors[visitor_id]}
    
    def reserve_ticket(self, visitor_id: str, ticket_id: str) -> None:
        if visitor_id in self.visitors and ticket_id in self.tickets:
            visitor = self.visitors[visitor_id]
            ticket = self.tickets[ticket_id]
            visitor.reserve_ticket(ticket)
        else:
            print(f"Visitatore o biglietto non trovato.")
    
    def cancel_ticket(self, visitor_id: str, ticket_id: str) -> None:
        if visitor_id in self.visitors and ticket_id in self.tickets:
            visitor = self.visitors[visitor_id]
            ticket = self.tickets[ticket_id]
            visitor.cancel_ticket(ticket)
        else:
            print("Visitatore o biglietto non trovato.")
    
    def list_available_tickets(self) -> list[str]:
        return [ticket_id for ticket_id, ticket in self.tickets.items() if not ticket.is_reserved]
    
    def list_visitor_reservations(self, visitor_id: str) -> list[str] | str:
        if visitor_id in self.visitors:
            return [ticket.ticket_id for ticket in self.visitors[visitor_id].reserved_tickets]
        else:
            return "Errore: visitatore non trovato."
        
    