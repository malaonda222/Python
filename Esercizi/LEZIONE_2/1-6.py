
ITS_Bakery_menu:dict = {"Pizza": 9.00,
                        "Pasta": 10.50, 
                        "Zuppa": 7.00,
                        "Hamburger": 15.50,
                        "Cotoletta": 10.00,
                        "Salmone": 20.20,
                        "Patatine fritte": 5.50,
                        "Patate al forno": 5.50,
                        "Verdura del giorno": 7.00,
                        "Cheesecake": 6.00,
                        "Tirsamisu": 6.00,
                        "Focaccia con Nutella": 6.00,
                        "Coca Cola": 3.50,
                        "Acqua": 1.50,
                        "Vino": 5.00}

ordine:dict = {"Zuppa": 7.00, "Salmone": 20.20, "Verdure del giorno": 7.00, "Cheesecake": 6.00, "Vino": 5.00}

totale_da_pagare = 0

totale_da_pagare += ordine["Zuppa"]
totale_da_pagare += ordine["Salmone"]
totale_da_pagare += ordine["Verdure del giorno"]
totale_da_pagare += ordine["Cheesecake"]
totale_da_pagare += ordine["Vino"]

# ordine_totale = zuppa_price + salmone_price + verdure_del_giorno_price + cheesecake_price + vino_price
print(f"Il cliente dovrà pagare {totale_da_pagare} euro")