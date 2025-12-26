from flask import Flask, url_for, jsonify, request

BASE_URL = "/animal"
if __name__ == "__main__":
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    r = request.get(f"{BASE_URL}", headers=headers)
    print(r.json)


    new_dog_id = "pdf789"
    new_dog = {
        "type": "dog",
        "id": new_dog_id,
        "name": "Fido",
        "age_years": 1,
        "weight_kg": 20,
        "breed": "Golden Retriever",
        "is_trained": True
    }

    r.request.post(
        f"{BASE_URL}/animals/add",
        headers=headers,
        json=new_dog #oppure data=json.dumps(new_dog)
    )

    print(r.json())