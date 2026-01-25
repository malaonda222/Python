import json 
import requests

BASE_URL = "https://127.0.0.1:5000"

headers= {
    "Content-type": "application/json",
    "Accept": "application/json"
}

# GET / e stampa / verifica il contenuto della risposta
response = requests.get(f"{BASE_URL}/", headers=headers)
print('Risposta GET/', response.status_code, response.json())

# GET /vehicles e controlla che la lista non sia vuota
response = requests.get(f"{BASE_URL}/vehicles", headers=headers)
print('Risposta GET/vehicles', response.status_code, response.json())

if response.status_code == 200:
    vehicles = response.json()
    if not vehicles:
        print("La lista dei veicoli è vuota")
    else:
        print(f"La lista dei veicoli è lunga {len(vehicles)}")
else:
    print(f"La richiesta non è andata a buon fine: {response.status_cose}")

# POST /vehicles per aggiungere un nuovo veicolo
new_plate_id = "LO908KI"
post_body = {
    "type":"car",
    "plate_id":new_plate_id,
    "model":"Fiat 500X",
    "driver_name":"Fabio Mori",
    "registration_year":2023,
    "status":"rented",
    "door":5,
    "is_cabrio":True
}
response = requests.post(
    f"{BASE_URL}/vehicles",
    headers=headers,
    data=json.dumps(post_body)
)
print('Risposta POST/vehicles', response.status_code, response.json())

# GET /vehicles/<plate_id> per verificare che sia stato creato
response = requests.get(f"{BASE_URL}/vehicles/{new_plate_id}", headers=headers)
print('Risposta GET7vehicles/<plate_id>', response.status_code, response.json())

# PATCH /vehicles/<plate_id>/status per aggiornare lo stato
patch_body = {
    "status": "available"
}
response = requests.patch(
    f"{BASE_URL}/vehicles/{new_plate_id}/status",
    headers=headers,
    data=json.dumps(patch_body)
)
print("Risposta PATCH/vehicles/<plate_id>/status", response.status_code, response.json())

# PUT /vehicles/<plate_id> per sostituire le info del veicolo
put_body = {
    "type":"car",
    "plate_id": new_plate_id,
    "model":"Fiat 600",
    "driver_name":"Fabio Morandi",
    "registration_year":2023,
    "status":"rented",
    "door":5,
    "is_cabrio":True
}
response = requests.put(
    f"{BASE_URL}/vehicles/{new_plate_id}",
    headers=headers,
    data=json.dumps(put_body)
)
print('Risposta PUT/vehicles/<plate_id>', response.status_code, response.json())

# DELETE /vehicles/<plate_id> per eliminarlo
response = requests.delete(f"{BASE_URL}/vehicles/{new_plate_id}", headers=headers)
print('Risposta DELETE/vehicles/<plate_id>', response.status_code, response.json())

# GET /vehicles/<plate_id> per verificare che non esista più (status 404)
response = requests.get(f"{BASE_URL}/vehicles/{new_plate_id}", headers=headers)
print('Risposta GET/vehicles/<plate_id>', response.status_code, response.json())

