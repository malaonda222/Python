import json 
import requests 

BASE_URL = "https://127.0.0.1:5000"

headers = {
    "Content-type": "application/json",
    "Accept": "application/json"
}

# GET / e stampa/verifica il contenuto della risposta
response = requests.get(f"{BASE_URL}/", headers=headers)
print('Risposta GET/', response.status_code, response.json())

# GET /bookings e controlla che la lista non sia vuota
response = requests.get(f"{BASE_URL}/bookings", headers=headers)
print('Risposta GET/bookings', response.status_cose, response.json())

if response.status_code == 200:
    bookings = response.json()
    if not bookings:
        print("La lista delle prenotazioni è vuota")
    else:
        print(f"La lista delle prenotazioni è lunga {len(bookings)}")
else:
    print(f"Risposta di errore alla richiesta: {response.status_code}")

# POST /bookings per aggiungere una nuova prenotazione
new_bk = "BK-103"
post_body = {
    "type":"exam",
    "booking_id":new_bk,
    "patient_name":"Marta Gini",
    "doctor":"Paglia Lorenzo",
    "department":"ginecologia",
    "date":"2025-12-03",
    "time":"13.15", 
    "status":"scheduled", 
    "visit_reason":"dolore",
    "first_time":True
}
response = requests.post(
    f"{BASE_URL}/bookings/",
    headers=headers,
    data=json.dumps(post_body)
)
print('Risposta POST/bookings', response.status_code, response.json())

# GET /bookings/<booking_id> per verificare che sia stata creata
response = requests.get(f"{BASE_URL}/bookings/{new_bk}", headers=headers)
print('Risposta GET/bookings/<booking_id>', response.status_code, response.json())

# PATCH /bookings/<booking_id>/status per aggiornare lo stato
patch_body = {"status": "checked_in"}
response = requests.patch(
    f"{BASE_URL}/bookings/{new_bk}/status",
    headers=headers,
    data=json.dumps(patch_body)
)
print('Risposta PATCH/bookings/<booking_id>/status', response.status_code, response.json())

# PUT /bookings/<booking_id> per sostituire le info della prenotazione
put_body = {
    "type":"visit",
    "booking_id":new_bk,
    "patient_name":"Marta Guini",
    "doctor":"Paglia Lorenzo",
    "department":"ginecologia",
    "date":"2025-21-03",
    "time":"13.45", 
    "status":"scheduled", 
    "exam_type":"PAP-test",
    "requires_fasting":False
}
response = requests.put(
    f"{BASE_URL}/bookings/{new_bk}",
    headers=headers,
    data=json.dumps(put_body)
)
print('Risposta PUT/bookings/<booking_id>', response.status_code, response.json())

# DELETE /bookings/<booking_id> per eliminarla
response = requests.delete(f"{BASE_URL}/bookings/{new_bk}", headers=headers)
print('Risposta DELETE/bookings/<booking_id>', response.status_code, response.json())

# GET /bookings/<booking_id> per verificare che non esista più (status 404)
response = requests.get(f"{BASE_URL}/bookings/{new_bk}", headers=headers)
print('Risposta GET/bookings/<booking_id>', response.status_code, response.json())


