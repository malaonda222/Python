import json 
import requests 

BASE_URL = "https://127.0.0.1:5000"

if __name__ == "__main__":
    headers = {
        "Content-Type": "application/json",
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
        print(f"La lista dei dispostivi è lunga {len(devices)}")
else:
    print(f"Risposta alla richiesta fallita {response.status_code}")

# POST /devices per aggiungere un nuovo dispositivo
new_device = "123ng"
post_body = {
    "device_id":new_device,
    "device_type":"smartphone",
    "model":"Samsung",
    "customer_name":"Bianca Bini",
    "purchase_year":2025,
    "status":"repairing",
    "has_protective_case":True,
    "storage_gb":265
}
response = requests.post(
    f"{BASE_URL}/devices", 
    headers=headers,
    data=json.dumps(post_body)
)
print('Risposta POST/devices', response.status_code, response.json())

# GET /devices/<nuovo_id> per verificare che sia stato creato
response = requests.get(f"{BASE_URL}/devices/{new_device}", headers=headers)
print(f'Risposta GET/devices/{new_device}', response.status_code, response.json())

# PATCH /devices/<nuovo_id>/status per aggiornare lo stato
patch_body = {"status": "repairing"}
response = requests.patch(
    f"{BASE_URL}/devices/{new_device}",
    headers=headers,
    data=json.dumps(patch_body)
)
print(f'Risposta PATCH/devices/{new_device}', response.status_code, response.json())

# PUT /devices/<nuovo_id> per sostituire le info del dispositivo
put_body = {
    "device_id":new_device,
    "device_type":"laptop",
    "model":"IPad Mini2",
    "customer_name":"Gianluca Goffi",
    "purchase_year":2026,
    "status":"delivered",
    "has_dedicated_gpu":True,
    "screen_size_inches":15.6
}
response = requests.put(
    f"{BASE_URL}/devices/{new_device}",
    headers=headers,
    data=json.dumps(put_body)
)
print(f'Risposta PUT/devices/{new_device}', response.status_code, response.json())

# DELETE /devices/<nuovo_id> per eliminarlo
response = requests.delete(f"{BASE_URL}/devices/{new_device}", headers=headers)
print(f'Risposta DELETE/devices/{new_device}', response.status_code, response.json())

# GET /devices/<nuovo_id> per verificare che non esista più (status 404)
response = requests.get(f"{BASE_URL}/devices/{new_device}", headers=headers)
print(f'Risposta GET/devices/{new_device}', response.status_code, response.json())

