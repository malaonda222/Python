import json
import requests 

BASE_URL = "https://127.0.0.1:5000"

headers = {
    "Content-type": "application/json",
    "Accept": "application/json"
}

# GET / e stampa / verifica il contenuto della risposta
response = requests.get(f"{BASE_URL}/", headers=headers)
print('Risposta GET/', response.status_code, response.json())

# GET /devices e controlla che la lista non sia vuota
response = requests.get(f"{BASE_URL}/devices", headers=headers)
print('Risposta GET/devices', response.status_code, response.json())

if response.status_code == 200:
    devices = response.json()
    if not devices:
        print("La lista dei dispositivi è vuota")
    else:
        print(f"La lista dei dispositivi è lunga {len(devices)}")
else:
    print(f"Risposta richiesta errore {response.status_code}")

# POST /devices per aggiungere un nuovo dispositivo
new_sn = "SN-103"
post_body = {
    "type":"camera",
    "serial_number":new_sn,
    "brand": "Philips", 
    "room": "Living Room",
    "installation_year": 2023,
    "status": "online",
    "resolution": "4K",
    "night_version": True
}
response = requests.post(
    f"{BASE_URL}/devices",
    headers=headers,
    data=json.dumps(post_body)
)
print('Risposta POST/devices', response.status_code, response.json())

# GET /devices/<serial_number> per verificare che sia stato creato il nuovo dispositivo nel sistema
response = requests.get(f"{BASE_URL}/devices/{new_sn}", headers=headers)
print('Risposta GET/devices/<serial_number>', response.status_code, response.json())

# PATCH /devices/<serial_number>/status per aggiornare lo stato
patch_body = {
    "status": "offline"
}
response = requests.patch(
    f"{BASE_URL}/devices/{new_sn}/status",
    headers=headers,
    data=json.dumps(patch_body)
)
print('Risposta PATCH/devices/<serial_number>/status', response.status_code, response.json())

# PUT /devices/<serial_number> per sostituire le info del dispositivo
put_body = {
    "type":"camera",
    "serial_number":new_sn,
    "brand":"Samsung",
    "room":"Bedroom",
    "installation_year":2025,
    "reoslution": "4K",
    "night_version":False
}
response = requests.put(
    f"{BASE_URL}/devices/{new_sn}", 
    headers=headers,
    data=json.dumps(put_body)
)
print('Risposta PUT/devices/<serial_number>', response.status_code, response.json())
 
# DELETE /devices/<serial_number> per eliminarlo
response = requests.delete(f"{BASE_URL}/devices/{new_sn}", headers=headers)
print('Risposta Delete/devices/<serial_number>', response.status_code, response.json())

# GET /devices/<serial_number> per verificare che non esista più (status 404)
response = requests.get(f"{BASE_URL}/devices/{new_sn}", headers=headers)
print('Risposta DELETE/devices/<serial_number>', response.status_code, response.json())

