import requests 
import json 

BASE_URL = "https://127.0.0.1:5000"

if __name__ == "__main__":
    headers = {
    "Content-type": "application/json",
    "Accept": "application/json"
    }

#GET / e stampa/verifica il contenuto della risposta
response = requests.get(f"{BASE_URL}/", headers=headers)
print('Risposta GET/', response.status_code, response.json())

#GET /bookings e controlla che la lista non sia vuota
response = requests.get(f"{BASE_URL}/bookings", headers=headers)
print('Risposta GET/bookings', response.status_code, response.json())

if response.status_code == 200:
    bookings = response.json()
    if not bookings:
        print("La lista delle prenotazioni è vuota")
    else:
        print(f"Ci sono {len(bookings)} prenotazioni")
else:
    print(f"Errore nella richiesta: {response.status_code}")

#POST /bookings per aggiungere una nuova prenotazione
new_booking_id = "BK-598"
body_post = {
    "type": "exam",
    "booking_id": new_booking_id,
    "patient_name": "Mario Rossi",
    "doctor": "Mauro Mauri",
    "department": "Cardiologia",
    "date": "2026-02-19",
    "time": "13.15",
    "status": "scheduled",
    "exam_type": "ECG",
    "requires_fasting": True
}
response = requests.post(
    f"{BASE_URL}/bookings",
    headers=headers,
    data = json.dumps(body_post)
)
print('Risposta POST/bookings', response.status_code, response.json())

#GET /bookings/<booking_id> per verificare che sia stata creata
response = requests.get(f"{BASE_URL}/bookings/{new_booking_id}", headers=headers)
print('Risposta GET/bookings/<booking_id>', response.status_code, response.json())

#PATCH /bookings/<booking_id>/status per aggiornare lo stato
new_status = {"status": "checked_in"}
response = requests.patch(
    f"{BASE_URL}/bookings/{new_booking_id}",
    headers=headers,
    data = json.dumps(new_status)
)
print('Risposta PATCH/bookings/<booking_id>', response.status_code, response.json())

#PUT /bookings/<booking_id> per sostituire le info della prenotazione
put_body = {
    "type": "visit",
    "booking_id": "IGNORED_BY_SERVER",
    "patient_name": "Luigi Bianchi",
    "doctor": "Matteo Gini",
    "department": "Radiologia",
    "date": "2026-01-28",
    "time": "18.15",
    "status": "scheduled",
    "visit_reason": "Dolore muscolare",
    "first_time": True
}
response = requests.put(
    f"{BASE_URL}/bookings/{new_booking_id}",
    headers=headers,
    data = json.dumps(put_body)
)
print('Risposta PUT/bookings/<booking_id>', response.status_code, response.json())

#DELETE /bookings/<booking_id> per eliminarla
response = requests.delete(f"{BASE_URL}/bookings/{new_booking_id}", headers=headers)
print('Risposta DELETE/bookings/<booking_id>', response.status_code, response.json())

#GET /bookings/<booking_id> per verificare che non esista più (status 404)
response = requests.get(f"{BASE_URL}/bookings/{new_booking_id}", headers=headers)
print('Risposta GET/bookings/<booking_id', response.status_code, response.json())