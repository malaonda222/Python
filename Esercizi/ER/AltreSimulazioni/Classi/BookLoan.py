class BookLoan:
    def __init__(self, loan_id: str, book_title: str, due_date: str) -> None:
        self.loan_id: str = loan_id
        self.book_title: str = book_title
        self.due_date: str = due_date
        self.is_loaned: bool = False 

    def borrow(self) -> None:
        if not self.is_loaned:
            self.is_loaned = True 
        else:
            print(f"Il libro '{self.book_title}' è già in prestito.")
    
    def return_book(self) -> None:
        if self.is_loaned:
            self.is_loaned = False 
        else:
            print(f"Il libro '{self.book_title}' non risulta in prestito.")
    
class Member:
    def __init__(self, member_id: str, name: str) -> None:
        self.member_id: str = member_id
        self.name: str = name 
        self.active_loans: list[BookLoan] = []
    
    def borrow_book(self, loan: BookLoan) -> None:
        if not loan.is_loaned:
            self.active_loans.append(loan)
            loan.borrow()
        else:
            print(f"Il libro '{loan.book_title}' non è disponibile per il prestito.")
    
    def return_book(self, loan: BookLoan) -> None:
        if loan in self.active_loans:
            self.active.remove(loan)
            loan.return_boook()
        else:
            print(f"Il libro '{loan.book_title}' non risulta tra i prestiti attivi del membro.")
    

class DigitalLibrary:
    def __init__(self) -> None:
        self.loans: dict[str, BookLoan] = {}
        self.members: dict[str, Member] = {}
    
    def add_loan(self, loan_id: str, book_title: str, due_date: str) -> None:
        if loan_id in self.loans:
            print(f"Il prestito con ID '{loan_id}' esiste già.")
        else:
            self.loans[loan_id] = BookLoan(loan_id, book_title, due_date)
    
    def register_member(self, member_id: str, name: str) -> None:
        if member_id in self.members:
            print(f"Il membro '{member_id}' è già registrato.")
        else:
            self.members[member_id] = Member(member_id, name)
    
    def borrow_book(self, member_id: str, loan_id: str) -> None:
        if member_id in self. members and loan_id in self.loans:
            member = self.members[member_id]
            loan = self.loans[loan_id]
            member.borrow_book(loan)
        else:
            print("Membro o prestito non trovato.")
    
    def return_book(self, member_id: str, loan_id: str) -> None:
        if member_id in self.members and loan_id in self.loans:
            member = self.members[member_id]
            loan = self.loans[loan_id]
            member.return_book(loan)
        else:
            print("Membro o prestito non trovato")
    
    def list_available_books(self) -> list[str]:
        return [loan_id for loan_id, loan in self.loans.items() if not loan.is_loaned]
        # oppure
        # lista_disponibili = []
        # for loan_id, loan in self.loans.items():
            # if not loan.is_loaned:
                # lista_disponibili.append(loan.loan_id)
        # if not lista_disponibili:
            #return "Lista vuota"
        # else:
            # return lista_disponibili

    def list_member_loans(self, member_id: str) -> list[str]|str:
        if member_id not in self.members:
            return "Errore, membro non trovato."
        else:
            member = self.members[member_id]
            # Se il membro esiste, restituisce una lista di loan_id attivi.
            return [loan.loan_id for loan in member.active_loans]    