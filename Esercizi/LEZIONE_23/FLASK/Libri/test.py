import json 
import requests 

BASE_URL = "https://127.0.0.1:5000"

if __name__ == "__main__":
    headers = {
        "Content-type": "application/json",
        "Accept": "application/json"
    }

#1. Test per GET /books (Visualizzare tutti i libri)
response = requests.get(f"{BASE_URL}/books", headers=headers)
print('Risposta GET/books', response.status_code, response.json())

if response.status_code == 200:
    books = response.json()
    if not books: 
        print("La lista dei libri è vuota")
    else:
        print(f"La lista dei libri è lunga {len(books)})")
else:
    print(f"Errore nella richiesta: {response.status_code}")


#2. POST Test per POST /books (Aggiungere un nuovo libro)
new_book = "TGG"
post_body = {
    "category": "fiction",
    "title": "The Great Gatsby",
    "author": "John Doe",
    "year": 2023,
    "description": "A thrilling adventure story",
    "genre": "Adventure"
}
response = requests.post(
    f"{BASE_URL}/books",
    headers=headers,
    data = json.dumps(post_body)
)
print('Richiesta POST/books', response.status_code, response.json())


#3. Test per GET /books/<book_id> (Visualizzare un libro specifico)
response = requests.get(f"{BASE_URL}/books/{new_book}", headers=headers)
print('Risposta GET/books/<book_id>', response.status_code, response.json())

#4. PUT /books/<book_id> (Modifica un libro esistente)
put_body = {
    "category": "non-fiction",
    "title": "Severance",
    "author": "John Dan",
    "year": 2024,
    "description": "A thrilling drama story",
    "genre": "Drama"
}
response = requests.put(
    f"{BASE_URL}/books/{new_book}",
    headers=headers,
    data=json.dumps(put_body)
)
print('Risposta PUT/books/<book_id>', response.status_code, response.json())

#5. DELETE /books/<book_id> (Eliminare un libro)
response = requests.delete(f"{BASE_URL}/books/{new_book}", headers=headers)
print('Richiesta DELETE/books/<book_id>', response.status_code, response.json())

