class Ticket:
    def __init__(self, ticket_id: str, movie: str, seat: str) -> None:
        self.ticket_id: str = ticket_id 
        self.movie: str = movie 
        self.seat: str = seat 
        self.is_booked: bool = False 
    
    def book(self) -> None:
        if not self.is_booked:
            self.is_booked = True 
        else:
            print(f"Il biglietto per '{self.movie}' posto '{self.seat}' è già prenotato.")
    
    def cancel(self) -> None:
        if self.is_booked:
            self.is_booked = False 
        else:
            print(f"Il biglietto per '{self.movie}' posto '{self.seat}' non risulta prenotato")


class Viewer:
    def __init__(self, viewer_id: str, name: str) -> None:
        self.viewer_id: str = viewer_id
        self.name: str = name 
        self.booked_tickets: list[Ticket] = []
    
    def book_ticket(self, ticket: Ticket) -> None:
        if not ticket.is_booked:
            self.booked_tickets.append(ticket)
            ticket.book()
        else:
            print(f"Il biglietto per '{ticket.movie}' non è disponibile")
    
    def cancel_ticket(self, ticket: Ticket) -> None:
        if ticket in self.booked_tickets:
            self.booked_tickets.remove(ticket)
            ticket.cancel()
        else:
            print(f"Il biglietto per '{ticket.movie}' non è stato prenotato da questo spettatore")
    

class Cinema: 
    def __init__(self) -> None:
        self.tickets: dict[str, Ticket] = {}
        self.viewers: dict[str, Viewer] = {}

    def add_ticket(self, ticket_id: str, movie: str, seat: str) -> None:
        if ticket_id in self.tickets:
            print(f"Il biglietto con ID '{ticket_id}' esiste già")
        else:
            self.tickets[ticket_id] = Ticket(ticket_id, movie, seat)
    
    def register_viewer(self, viewer_id: str, name: str) -> None:
        if viewer_id in self.viewers:
            print(f"Lo spettatore con ID '{viewer_id}' è già registrato")
        else:
            self.viewers[viewer_id] = Viewer(viewer_id, name)
    
    def book_ticket(self, viewer_id: str, ticket_id: str) -> None:
        if viewer_id in self.viewers and ticket_id in self.tickets:
            viewer = self.viewers[viewer_id]
            ticket = self.tickets[ticket_id]
            viewer.book_ticket(ticket)
        else:
            print("Spettatore o biglietto non trovato")
    
    def cancel_ticket(self, viewer_id: str, ticket_id: str) -> None:
        if viewer_id in self.viewers and ticket_id in self.tickets:
            viewer = self.viewers[viewer_id]
            ticket = self.tickets[ticket_id]
            viewer.cancel_ticket(ticket)
        else:
            print("Spettatore o biglietto non trovato")
    
    def list_available_tickets(self) -> list[str]:
        if not self.tickets:
            return []
        else:
            return [ticket_id for ticket_id, ticket in self.tickets.items() if not ticket.is_booked]
    
    def list_viewer_booking(self, viewer_id: str) -> list[str]|str:
        if viewer_id not in self.viewers:
            return "Errore: spettatore non trovato"
        else:
            viewer = self.viewers[viewer_id]
            return [ticket.ticket_id for ticket in viewer.booked_tickets]
