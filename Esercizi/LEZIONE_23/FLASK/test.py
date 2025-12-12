from flask import request
import json 

if __name__ == "__main__":
    headers = {             #serve per descrivere la tipologia del dato utilizzato 
        'Content-type': 'application/json', #il valore cambia in base al formato 
        'Accept': 'application/json' #il valore cambia in base al formato
    }

    # Esempio di GET
    response = request.get(
        url= 'http://localhost:5000/libri',
        headers=headers
    )
    print('Risposta GET:', response.json()) #stampo nel terminale il contenuto del json che corrisponde alla risposta della chiamata get
    
    
    # Esempio di POST
    payload = {
        'nome': 'Marco',
        'cognome': 'Cascio'
    }
    # Versione senza dumps
    response_post = request.post(
        url='http://localhost:5000/api/utenti', #esempio di endpoint 
        json=payload,
        headers=headers
    )

    # Versione con dumps
    response_post = request.post(
        url='http://localhost:5000/api/utenti',
        data=json.dumps(payload),
        headers=headers
    )
    print('Risposta POST:', response_post.json())

