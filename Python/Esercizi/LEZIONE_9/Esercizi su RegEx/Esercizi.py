'''Riconoscere numeri'''
# 1.1.
'^\d+$'

# 1.2. 
'^-?\d+$'


'''Riconoscere parole'''
# 2.1.
'^[a-zA-Z]+$'

# 2.2.
'^[a-z]+$'

# 2.3.
'[a-zA-Z]{5,10}'


'''Email semplici'''
# 3.1. 
'^[a-zA-Z0-9._%-+]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
 
# 3.2. 
'^[a-zA-Z0-9._%-+]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(?:\.[a-zA-Z]{2,})?$'


'''CAP e codici'''
# 4.1.
'^\d{5}$'

# 4.2. 
'^[A-Z]{6}\d{2}[A-Z]\d{2}$'


'''Riconoscere le date'''
# 5.1. 
'\d{2}/\d{2}/\d{4}'

# 5.2.
'\d{2}-\d{2}-\d{4}'


'''Codici personalizzati'''
# 6.1. 
'[A-Z]{4}-[0-9]{4}-[A-Z]{2}'

# 6.2.
'^[A-Z0-9]{8}$'


'''Esercizi - Comprensione di RegEx'''
# 7.1. 
# Un carattere di AZ e almeno due caratteri tra az

# 7.2.
# Qualsiasi stringa che abbia 3 numeri-2 numeri-4 numeri

# 7.3.
# colour oppure color


'''Bonus - Errori comuni'''
# 8.1. 
# Cerca la minima quantità di corrispondenza 

# 8.2.
# Non si fa un controllo solo sulle lettere ma anche su caratteri non alfabetici. 


