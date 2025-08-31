from datetime import date 

def data_valida(anno: int, mese: int, giorno: int) -> bool:
    try:
        _ = date(giorno, mese, anno)
        return True
    except ValueError:
        return False 
    
print(data_valida(31, 4, 2023))