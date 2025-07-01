def memorizza_file(files: list[int]) -> None:
    spazio_totale_blocchi = 1000  # Spazio totale disponibile in blocchi
    percentuale = 0.8
    byte = 512
    
    for item in files:
        immagine_compressa = item * percentuale 
        numero_blocchi = round(immagine_compressa / byte)
        
        if numero_blocchi <= spazio_totale_blocchi:
            spazio_totale_blocchi -= numero_blocchi
            print(f"File di {item} byte compresso in {immagine_compressa} byte e memorizzato. Blocchi usati: {numero_blocchi}. Blocchi rimanenti: {spazio_totale_blocchi}.")
        
        else:
            print(f"Non è possibile memorizzare il file di {item} byte. Spazio insufficiente.")
            break


memorizza_file([1100, 20000, 1048576, 512, 5000])