def aggiungi_lista(lst, val):
    lst.append(val)

class MiaLista:
    def __init__(self): # chiamato automaticamente ogni volta che viene chiamato l'oggetto
        self.lst: list[int] = []

    def aggiungi(self, val:int):
        self.lst.append(val)
    
    def rimuovi(self, val):
        if val in self.lst:
            self.lst.remove(val)
        
    def __repr__(self):
        return f'{self.lst}'

mylist = MiaLista()
mylist.aggiungi(10)

mylist.aggiungi(11)

mylist.rimuovi(10)

print(mylist)

