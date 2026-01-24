import json 
import requests 

BASE_URL = "https://127.0.0.1:5000"

if __name__ == "__main__":
    headers = {
        "Content-type": "aplication/json",
        "Accept": "application/json"
    }

# GET /
response = requests.get(f"{BASE_URL}/", headers=headers)
print('Risposta GET/', response.status_code, response.json())

# GET /animals
response = requests.get(f"{BASE_URL}/animals", headers=headers)
print('Risposta GET/animals', response.status_code, response.json())

if response.status_code == 200:
    animals = response.json()
    if not animals:
        print("la lista degli animali è vuota")
    else:
        print(f"La lista degli animali è lunga {len(animals)}")
else:
    print(f"Richiesta non andata a buon fine {response.status_code}")

# GET /animals/d1 (o l’ID che hai scelto per il cane di esempio)
response = requests.get(f"{BASE_URL}/animals/d1", headers=headers)
print('Risposta GET/animals/id1', response.status_code, response.json())

# GET /animals/d1/food
response = requests.get(f"{BASE_URL}/animals/d1/food", headers=headers)
print('Risposta GET/animals/d1/food', response.status_code, response.json())

# GET /animals/d1/adoption
response = requests.get(f"{BASE_URL}/animals/d1/adoption", headers=headers)
print(f"Risposta GET/animals/d1/adoption", response.status_code, response.json())

# POST /animals – aggiunta di un nuovo cane
new_dog = "d2"
body_post = {
    "species":"dog",
    "id":new_dog,
    "name":"Fido",
    "age_years":1,
    "weight_kg":18.5,
    "breed":"golden retriever",
    "is_trained":True
}
response = requests.post(
    f"{BASE_URL}/animals",
    headers=headers,
    data=json.dumps(body_post)
)
print('Risposta POST/animals', response.status_code, response.json())

# POST /animals – aggiunta di un nuovo gatto
new_cat = "c2"
body_post = {
    "species":"cat",
    "id":new_cat,
    "name":"Furia",
    "age_years":4,
    "weight_kg":5,
    "indoor_only":True,
    "favorite_toy":"Mouse"
}
response = requests.post(
    f"{BASE_URL}/animals",
    headers=headers,
    data=json.dumps(body_post)
)
print("Risposta POST/animals", response.status_code, response.json())

# POST /animals/<animal_id>/adopt
adopt_body = {
    "adopter_name": "Mario Rossi"
}
response = requests.post(
    f"{BASE_URL}/animals/{new_dog}/adopt",
    headers=headers,
    data=json.dumps(adopt_body)
)
print(f'Risposta GET/animals/{new_dog}/adopt', response.status_code, response.json())

