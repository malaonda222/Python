# Sandwich

def sandwich(*args):
    riepilogo = []
    for item in args:
        riepilogo.append(item)
        
    print(f"Il sandwich ordinato contiene: {riepilogo}")

sandwich('Uova', 'Cipolla', 'Formaggio')
sandwich('Manzo', 'Maionese')
sandwich('Pollo', 'Senape', 'Cetriolini')