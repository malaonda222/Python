from abc import ABC, abstractmethod 

class Persona(ABC):
    
    def __init__(self, nome: str, età: int):
        self.nome = nome
        self.età = età

    @abstractmethod
    def get_role(self):
        pass 

    def __str__(self): 
        return f"Nome: {self.nome}\nEtà: {self.età}\nRuolo:{self.get_role()}"
                               

class Student(Persona):

    def __init__(self, nome: str, età: int, studente_id: int):
        super.__init__(nome, età)
        self.studente_id = studente_id
        self.corsi = []

    def get_role(self):
        print("Studente")
    
    def iscrivere(self, corso: str):
        if corso not in self.corsi:
            self.corsi.append(corso)
            corso.add_student(self)
            print(f"Lo studente {self.nome} è stato iscritto al corso {corso}.")
        else:
            print(f"Lo studente {self.nome} risulta già iscritto al cosro {corso}.")

    def __str__(self):
        return super().__str__() + f" | ID: {self.studente_id}"
        # return f"Studente: {self.nome}\nID: {self.studente_id}\nCorsi: {", ".join(self.corsi) if self.corsi else "Nessun corso"}"

class Dipartimento:
    def __init__(self, nome_dipartimento: str):
        self.nome_dipartimento = nome_dipartimento
        self.corsi = []
        self.professori = []

    def add_course(self, corso: str):
        if corso not in self.corsi:
            self.corsi.append(corso)
            print("Corso aggiunto al dipartimento.")
        else:
            print("Il corso è già presente nel dipartimento.")

    def add_professor(self, professore: str):
        if professore not in self.professori:
            self.professori.append(professore)
            print("Professore aggiunto con successo.")
        else:
            print("Il professore risulta già aggiunto.")
        
    def __str__(self):
        corsi_nomi = ", ".join(c.nome_corso for c in self.corsi) or "Nessun corso."
        prof_nomi = ", ".join(d.nome for d in self.dipartimenti) or "Nessun dipartimento."
        return (
            f"Dipartimento: {self.nome_dipartimento}"
            f"Corsi: {corsi_nomi}\n"
            f"Professori: {prof_nomi}"
        )

class Professore(Persona):
    def __init__(self, nome:str, età: int, professore_id: int, dipartimento: Dipartimento):
        super().__init__(nome, età)
        self.professore_id = professore_id
        self.corsi = []
        self.dipartimento = dipartimento 

        dipartimento.add_professore(self)

    def get_role(self):
        print("Professore")
    
    def assign_to_course(self, professore: str, corso: str):
        if corso not in self.corsi:
            self.corsi.append(corso)
            corso.set_professor(self)
    
    def __str__(self):
        return super().__str__ + f" ID Professore: {self.professore_id}\nDipartimento: {self.dipartimento.nome_dipartimento}"
    

class Corso:
    def __init__(self, nome_corso: str, codice_corso: int, professore: Professore):
        self.nome_corso = nome_corso
        self.codice_corso = codice_corso
        self.studenti = []
        self.professore = professore

    def add_student(self, studente: str, corso: str):
        if studente not in corso:
            self.studenti.append(studente)
            print(f"Studente {studente.studente_id} aggiunto al corso.")   
        else: 
            print("Lo studente risulta già iscritto al corso.")

    def set_professor(self, professore: str):
        self.professore = professore

    def __str__(self):
        prof_str = self.professore.nome if self.professore else "Nessun professore assegnato."
        studenti_nomi = ", ".join(s.nome for s in self.studenti) or "Nessuno studente"
        return (
            f"Corso: {self.nome_corso} (Codice: {self.codice_corso})\n"
            f"Professore: {prof_str}\n"
            f"Studenti iscritti: {studenti_nomi}\n"
        )
    

class Università:
    def __init__(self, nome: str):
        self.nome = nome 
        self.dipartimenti = []
        self.studenti = [] 

    def add_department(self, dipartimento: str):
        if dipartimento not in self.dipartimenti:
            self.dipartimenti.append(dipartimento)
            print("Dipartimento aggiunto all'università")
        else:
            print("Dipartimento già presente all'interno dell'università")

    def add_studente(self, studente: str):
        if studente not in self.studenti:
            self.studenti.append(studente)
            print("Studente aggiunto all'università")
        else:
            print("Strudente già presente all'interno dell'università")

    def __str__(self):
            dipart_nomi = ", ".join(d.nome_dipartimento for d in self.dipartimenti or "Nessun dipartimento")
            studenti_nomi = ", ".join(s.nome for s in self.studenti or "Nessuno studente")
            return (
            f"Università: {self.nome}\n\n"
            f"DIpartimenti: {dipart_nomi}\n\n"
            f"Studenti iscritti: {studenti_nomi}"
            )



if __name__ == "__main__":
    uni = Università("Università degli studi di Firenze")

    dip_info = Dipartimento("Lingue e letterature straniere")
    uni.add_department(dip_info)

    stud = Student("Danilo", 27, 1459623)
    uni.add_studente(stud) 

    print(uni)