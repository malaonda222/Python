'''4. Progetta una mini API: un’agenzia di viaggi deve gestire destinazioni, clienti 
e prenotazioni. Definisci 5 endpoint REST (metodo + URI + esempio di risposta JSON).'''


#ottenere elenco delle prenotazioni
'''Metodo HTTP: GET
    Endpoint: /prenotazioni
    Codice di stato: 200 OK
    
    Request:
    GET https://api.agenzia_viaggi.it/prenotazioni

    Response:
    HTTP/1.1 200 OK
    {
        "message": "Fornita lista delle prenotazioni",
        "prenotazioni": ....
    }
    '''


#creazione di un cliente 
'''Metodo HTTP: POST
    Endpoint: /clienti
    Codice di stato: 201 Created

    Request:
    POST https://api.agenzia_viaggi.it/clienti
    Content-Type: application/json

    {
        "id": 11,
        "nome": "Luigi",
        "cognome": "Monti,
        "email": "lu.mo@gmail.com",
        "telefono": "+393332645198"
    }

    Response:
    HTTP/1.1 201 Created
    {
        "message": "Cliente creato con successo",
        "informazioni": {
            "id": 11,
            "nome": "Luigi",
            "cognome": "Monti,
            "email": "lu.mo@gmail.com",
            "telefono": "+393332645198"
        }
    }
'''


#modifica parziale di un viaggio(id)
'''Metodo HTTP: PATCH
    Endpoint: /viaggi/3
    Codice di stato: 200 OK, 404 Not Found
    
    Request:
    PATCH https://api.agenzia_viaggi.it/viaggi/3
    Content-Type: application/json

    {
        "id": 3,
        "data_partenza": "2025-03-06"
        "data_ritorno": "2025-03-10",
        "n_giorni": 4
    }

    Response:
    HTTP/1.1 200 OK
    {
    "message": "Viaggio modificato con successo",
    "viaggio": {
        "id": 3,
        "data_partenza": "2025-03-06"
        "data_ritorno": "2025-03-10",
        "n_giorni": 4
        }
    }

    Response:
    HTTP/1.1 404 Not Found
    {
        "message": "Viaggio id non trovato"
    }
'''


#aggiungere una nuova destinazione
'''Metodo HTTP: POST
    Endpoint: /destinazioni
    Codice di stato: 201 Created
    
    Request:
    POST https://api.agenzia_viaggi.it/destinazioni
    Content-Type: application/json 


    {
        "id": 10,
        "nome": "Sudafrica",
        "Paese": "Africa",
        "descrizione": "Popolo affascinante e paesaggi mozzafiato"
    }

    Response:
    HTTP/1.1 201 Created 
    {
    "message": "Destinazione aggiunta con successo"
    "destinazione": {
        "id": 10,
        "nome": "Sudafrica",
        "Paese": "Africa",
        "descrizione": "Popolo affascinante e paesaggi mozzafiato"
        }
    }
'''

#modifica totale di una prenotazione
'''Metodo HTTP: PUT
    Endpoint: /prenotazioni/4
    Codice di stato: 200 OK, 404 Not Found
    
    Request:
    PUT https://api.agenzia_viaggi.it/prenotazioni/4
    Content-Type: application/json 
    
    {
        "id": 4,
        "username": "Mario Rossi",
        "destinazione": "Sevilla"
    }
    
    Response:
    HTTP/1.1 200 OK
    {
    "message": "Prenotazione modificata con successo"
    "prenotazione": {
        "id": 4,
        "username": "Mario Rossi",
        "destinazione": "Sevilla"
        }
    }
    
    Response:
    HTTP/1.1 404 Not Found
    {
        "message": "Prenotazione non trovata"
    }
'''