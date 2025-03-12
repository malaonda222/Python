# Sandwich

def sandwich(*args):
    riepilogo = []
    for item in args:
        riepilogo.append(item)
        
    print(f"Il sandwich ordinato contiene: {', '.join(riepilogo)}")

sandwich('Uova', 'Cipolla', 'Formaggio')
sandwich('Manzo', 'Maionese')
sandwich('Pollo', 'Senape', 'Cetriolini')

def sandwich(*args):
    riepilogo = []
    for item in args:
        riepilogo.append(item)
        riepilogo_virgolette = ['"{}"'.format(item) for item in riepilogo]

    print(f"Il sandwich ordinato contiene: {', '.join(riepilogo_virgolette)}")

    
sandwich('Uova', 'Cipolla', 'Formaggio')
sandwich('Manzo', 'Maionese')
sandwich('Pollo', 'Senape', 'Cetriolini')

