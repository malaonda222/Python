import json 
import requests

BASE_URL = "http://127.0.0.1:5000"

if __name__ == "__main__":
    headers = {
        "Content_type": "application/json",
        "Accept": "application/json"
    }


#GET e stampa / verifica il contenuto della risposta
response = requests.get(f"{BASE_URL}/", headers=headers)
print('Risposta GET', response.status_code, response.json())

#GET /vehicles e controlla che la lista non sia vuota
response = requests.get(f"{BASE_URL}/vehicles", headers=headers)
print("\nGET /vehicles (controlla che la lista non sia vuota):")
print(f"Status code: {response.status_code}")

if response.status_code == 200:
    vehicles = response.json()
    if vehicles:
        print("La lista dei veicoli non è vuota")
        print(f"Veicoli: {vehicles}")
    else:
        print("La lista dei veicoli è vuota")
else:
    print(f"Codice di stato della richiesta: {response.status_code}")


# POST /vehicles per aggiungere un nuovo veicolo
new_plate_id = "SSSLLL9"
post_body = {
    "type": "car", 
    "plate_id": new_plate_id,
    "model": "Fiat 500 Cabrio",
    "driver_name": "Mario Verdi",
    "registration_year": 2023,
    "status": "available",
    "doors": 5,
    "is_cabrio": True
}
response = requests.post(
    f"{BASE_URL}/vehicles", 
    headers=headers, 
    data=json.dumps(post_body))

print('Risposta POST/vehicles', response.status_code, response.json())


# GET /vehicles/<plate_id> per verificare che sia stato creato
response = requests.get(f"{BASE_URL}/vehicles/{new_plate_id}", headers=headers)
print('Risposta GET', response.status_code, response.json())

# PATCH /vehicles/<plate_id>/status per aggiornare lo stato
patch_body = {"status": "rented"}
response = requests.patch(
    f"{BASE_URL}/vehicles/{new_plate_id}/status", 
    headers=headers,
    data=json.dumps(patch_body))

print('Risposta PATCH/vehicles/<plate_id>', response.status_code, response.json())

# PUT /vehicles/<plate_id> per sostituire le info del veicolo
put_body = {
    "type": "van",
    "plate_id": new_plate_id,
    "model": "Fiat Doblo",
    "driver_name": "Gianluca Bini",
    "registration_year": 2021,
    "status": "rented",
    "max_load_kg": 1200,
    "require_special_license": True 
}
response = requests.put(
    f"{BASE_URL}/vehicles/{new_plate_id}",
    headers=headers,
    data=json.dumps(put_body)
)
print('Risposta PUT/vehicles/<plate_id>', response.status_code, response.json())

# DELETE /vehicles/<plate_id> per eliminarlo
response = requests.delete(f"{BASE_URL}/vehicles", {new_plate_id}, headers=headers)
print('Risposta DELETE/vehicles', response.status_code, response.json())

# GET /vehicles/<plate_id> per verificare che non esista più (status 404)
response = requests.get(f"{BASE_URL}/vehicles/{new_plate_id}", headers=headers)
print('Risposta GET/vehicles/<plate_id>', response.status_code, response.json())

# GET /vehicles/<plate_id>/prep-time/2.0 (stima preparazione)
response = requests.get(f"{BASE_URL}/vehicles/{new_plate_id}/prep-time/2.0", headers=headers)
print('Risposta GET/vehicles/<plate_id>/prep-time/2.0', response.json())

