'''Analisi JSON: Ecco un oggetto JSON relativo a una prenotazione di campo da tennis: 

Content-Type: application/json
{
   'id': 12,
   'cliente': 'Luca Neri', 
   'campo': 3, 
   'data': '2025-03-20', 
   'ora': '18:00', 
   'durata_ore': 2
}
Individua la risorsa e utilizza i metodi HTTP per crea una nuova prenotazione 
con i dati forniti, modificare l'intera prenotazione, e creare una
nuova prenotazione con dati differenti. Indica anche il codice di stato corretto. '''

#Creare una nuova prenotazione
'''Metodo HTTP: POST
   Endpoint: /prenotazioni
   Codice di stato: 201 Created 
   
   Request:
   POST https://api.esempio.it/prenotazioni
   Content-Type: application/json

   {
      "id": 12,
      "cliente": "Luca Neri", 
      "campo': 3, 
      "data": "2025-03-20", 
      "ora": "18:00", 
      "durata_ore": 2
   }
   
   Response:
   HTTP/1.1 201 Created
   {
   "message": "Prenotazione creata con successo",
   "prenotazione": {
      "id": 12,
      "cliente": "Luca Neri",
      "campo": 3,
      "data": "2025-03-20",
      "ora": "18:00",
      "durata_ore": 2
      }
   }
'''



'''Metodo HTTP: PUT
   Endpoint: /prenotazioni/12
   Codice di stato: 200, 404
   
   Request:
   POST https://api.esempio.it/prenotazioni/12
   Content-Type: application/json
   
   {
      "id": 12,
      "cliente": "Luca Neri",
      "campo": 3,
      "data": "2025-03-20",
      "ora": "18:00",
      "durata_ore": 2
   }

   Response:
   HTTP/1.1 200 OK
   {
   "message": "Prenotazione aggiornata con successo",
   "prenotazione": {
      "id": 12,
      "cliente": "Luca Neri",
      "campo": 4,
      "data": "2024-08-15",
      "ora": "19:00",
      "durata_ore": 3
      }
   }

   Response (Errore 404):
   HTTP/1.1 404 Not Found
   {
      "message": "Campo non trovato, impossibile creare la prenotazione"
   }
'''



'''Metodo HTTP: POST
   Endpoint: /prenotazioni
   Codice di stato: 201, 400
   
   Request: 
   POST https://api.esempio.it/prenotazioni
   Content-Type: application/json

   {
      "id": 20,
      "cliente": "Gianna Bianchi", 
      "campo": 8, 
      'data': "2025-04-26", 
      "ora": "15:00", 
      "durata_ore": 1
   }

   Response:
   HTTP/1.1 201 Created
   {
   "message": "Prenotazione creata con successo",
   "prenotazione": {
      "id": 20,
      "cliente": "Gianna Bianchi", 
      "campo": 8, 
      'data': "2025-04-26", 
      "ora": "15:00", 
      "durata_ore": 1
   }
   '''

'''Metodo HTTP: POST
   Endpoint: /prenotazioni
   Codice di stato: 400
   
   Request: 
   POST https://api.esempio.it/prenotazioni
   Content-Type: application/json

   {
      "id": 20,
      "cliente": "", 
      "campo": 8, 
      'data': "2025-04-26", 
      "ora": "15:00", 
      "durata_ore": 1
   }

   Response (Errore 400):
   HTTP/1.1 400 Bad Request
   {
      "message": "I dati inseriti contengono anomalie"
   }
'''