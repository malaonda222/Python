import json 
import requests 

BASE_URL = "https://127.0.0.1:5000"

if __name__ == "__main__":
    headers = {
        "Content_type": "application/json", 
        "Accept": "application/json"
    }

# GET / e stampa / verifica il contenuto della risposta
response = requests.get(f"{BASE_URL}/", headers=headers)
print('Risposta GET/', response.status_code, response.json())

# GET /devices e controlla che la lista non sia vuota
response = requests.get(f"{BASE_URL}/devices", headers=headers)
print('Risposta GET/devices', response.json())

# POST /devices per aggiungere un nuovo dispositivo
new_device = "SN-307"
body_post = {
    "type": "camera",
    "serial_number": new_device,
    "brand": "Philips",
    "room": "Bathroom",
    "instalation_year": 2023,
    "status": "online", 
    "resolution": "4K",
    "night_version": True
}

response = requests.post(
    f"{BASE_URL}/devices",
    headers=headers,
    data = json.dumps(body_post)
)
print('Richiesta POST/devices (nuovo dispositivo bagno)', response.json())

# GET /devices/<serial_number> per verificare che sia stato creato il nuovo dispositivo nel sistema
response = requests.get(f"{BASE_URL}/devices/{new_device}", headers=headers)
print('Risposta GET/devices7<serial_number>', response.json())

# PATCH /devices/<serial_number>/status per aggiornare lo stato
patch_body = {"status": "updating"}
response = requests.patch(
    f"{BASE_URL}/devices/{new_device}/status",
    headers=headers,
    data = json.dumps(patch_body)
)
print('Risposta PATCH/devices/<serial_number>/status', response.json())

# PUT /devices/<serial_number> per sostituire le info del dispositivo
put_body = {
    "type": "bulb",
    "serial_number": new_device,
    "brand": "IKEA",
    "room": "Livingroom",
    "installation_year": 2023,
    "status": "offline",
    "brightness": 1200,
    "color_capability": False 
}
response = requests.put(
    f"{BASE_URL}/devices/{new_device}",
    headers=headers,
    data = json.dumps(put_body)
)
print('Risposta PUT/devices/<serial_number>', response.json())

# GET /devices/<serial_number>/diagnostic/1.5 (stima diagnostica)
response = requests.get(f"{BASE_URL}/devices/{new_device}/diagnostic/1.5", headers=headers)
print('Risposta GET/devices/<serial_number>/diagnostic/1.5', response.json())

# DELETE /devices/<serial_number> per eliminarlo
response = requests.delete(f"{BASE_URL}/devices/{new_device}", headers=headers)
print('Risposta DELETE7devices/<serial_number>', response.json())

# GET /devices/<serial_number> per verificare che non esista più (status 404)
response = requests.get(f"{BASE_URL}/devices/{new_device}", headers=headers)
print('Risposta GET/devices/<serial_number> (dopo delete)', response.json())





