import json 
import requests 

BASE_URL = "https://127.0.0.1:5000"

headers = {
    "Content-type": "application/json",
    "Accept": "application/json"
}

#1. Test per GET all'elenco dei film
response = requests.get(f"{BASE_URL}/movies", headers=headers)
print('Risposta GET/movies', response.status_code, response.json())

if response.status_code == 200:
    movies = response.json()
    if not movies:
        print("la lista dei film è vuota")
    print(f"La lista dei film è lunga {len(movies)}")
print("Risposta delle richiesta invalida")

#2.Test per GET di un singolo film
response = requests.get(f'{BASE_URL}/movies/<string:movie_id>', headers=headers)
print('Risposta GET/movies/<movie_id>', response.status_code, response.json())

#3. Test per POST (creazione di un film)
new_movie = "fino23"
body_post = {
    "category": "drama",
    "id": "fino123",
    "director": "Bioni",
    "year": 2026,
    "description": "drama story",
    "theme": "family affair"
}
response = requests.post(
    f"{BASE_URL}/movies",
    headers=headers,
    data=json.dumps(body_post)
)
print('Risposta POST/movies', response.status_code, response.json())

#4. Test per PUT (aggiornamento di un film)
body_put = {
    "category": "action",
    "id": "fino123",
    "director": "Bioni",
    "year": 2024,
    "description": "action story",
    "theme": "team affair"
}
response = requests.put(
    f"{BASE_URL}/{new_movie}",
    headers=headers,
    data=json.dumps(body_put)
)
print('Risposta PUT/movies/<movie_id>', response.status_code, response.json())

#5. Test per PATCH Year
body_patch = {"year": 2025}
response = requests.patch(
    f"{BASE_URL}/movies/{new_movie}/year",
    headers=headers,
    data=json.dumps(body_patch)
)
print('Risposta PATCH/movies/<movie_id>/year', response.status_code, response.json())

# 6. Test per DELETE (eliminazione di un film)
response = requests.delete(f"{BASE_URL}/movies/{new_movie}", headers=headers)
print('Risposta DELETE/movies/<movie_id>', response.status_code, response.json())