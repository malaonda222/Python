from __future__ import annotations
from flask import Flask, jsonify, url_for, request
from abc import ABC, abstractmethod


'''Classi di dominio'''

class Animal(ABC):
    def __init__(self, animal_id: str, name: str, age_years: int, weight_kg: float) -> None:
        self.id: str = animal_id
        self.name: str = name 
        self.age_years: int = age_years
        self.weight_kg: float = weight_kg

    @abstractmethod
    def species(self):
        """Specie dell'animale (dog, cat, ..)"""
        pass 

    @abstractmethod
    def daily_food_grams(self) -> int:
        """Quantità di cibo giornaliera in grammi."""
        pass 

    def bmi_like(self) -> float:
        """Indice fittizio di forma fisica."""
        return self.weight_kg / (self.age_years + 1)
    
    def info(self) -> dict:
        """Informazioni di base + eventuali attributi specifici nelle sottoclassi."""
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species(),
            "age_years": self.age_years,
            "weight_kg": self.age_weight_kg,
            "bmi_like": self.bmi_like(),
            "daily_food_grams": self.daily_food_grams()
        }
    

class Dog(Animal):
    def __init__(self, animal_id: str, name: str, age_years: int, weight_kg: float, breed: str, is_trained: bool) -> None:
        super().__init__(animal_id, name, age_years, weight_kg)
        self.breed: str = breed
        self.is_trained: bool = is_trained
    
    def species(self) -> str:
        return "dog"
    
    def daily_food_grams(self) -> int:
        return round(200 + self.age_years * 50, 2)
    
    def info(self) -> dict:
        info_dict = super().info()
        info_dict["breed"] = self.breed
        info_dict["is_trained"] = self.is_trained
        return info_dict
    

class Cat(Animal):
    def __init__(self, animal_id: str, name: str, age_years: int, weight_kg: float, indoor_only: bool, favorite_toy: str) -> None:
        super().__init__(animal_id, name, age_years, weight_kg)
        self.indoor_only: bool = indoor_only
        self.favorite_toy: str = favorite_toy

    def species(self) -> str:
        return "cat"
    
    def daily_food_grams(self):
        return round(100+self.age_years*30, 2)
    
    def info(self) -> dict:
        info_dict = super().info()
        info_dict["indoor_only"] = self.indoor_only
        info_dict["favorite_toy"] = self.favorite_toy
        return info_dict
    

class Shelter:
    def __init__(self, animals: dict[str, Animal] | None = None, adoptions: dict[str, str] | None = None) -> None:
        self.animals: dict = animals if animals is not None else {}
        self.adoptions: dict = adoptions if adoptions is not None else {}

        # oppure senza mettere niente tra le parentesi dell'__init__:
        # self.animals: dict[str, Animal] = {}
        # self.adoptions: dict[str, str] = {}

    def add(self, animal: Animal) -> bool:
        """Aggiunge un animale. Ritorna False se l'id esiste già."""
        if animal.id in self.animals:
            raise ValueError("Errore. Id animale già esistente")
        self.animals[animal.id] = animal
        return True
    
    def get(self, animal_id: str) -> Animal | None:
        if animal_id not in self.animals:
            return None 
        else:
            return self.animals[animal_id] #oppure self.animals.get(animal_id)
    
    def list_all(self) -> list[Animal]:
        return list(self.animals.values())

    def is_adopted(self, animal_id: str) -> bool:
        return animal_id in self.adoptions 
    
    def set_adopted(self, animal_id: str, adopter_name: str) -> None:
        self.adoptions[animal_id] = adopter_name

    def get_adopter(self, animal_id: str) -> str | None:
        return self.adoptions.get(animal_id)


'''Inizializzazione dati'''

shelter = Shelter() 

fufi = Dog("123abc", "Fufi", 5, 20, "Labrador", True)
mira = Cat("456def", "Mira", 6, 3, False, "ball")

shelter.add(fufi)
shelter.add(mira)


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home(): #oppure index
    sample_dog_id = "123abc"
    return jsonify({
        "message": "Welcome to Animal Shelter API",
        "routes": {
            "list_animals": url_for('list_animals'),
            "sample_dog_details": url_for('get_animal', animal_id=sample_dog_id),
            "sample_dog_food": url_for('get_food', animal_id=sample_dog_id),
            "sample_dog_adoption": url_for('get_adoption', animal_id=sample_dog_id),
            "add_animal":url_for('add_animal')
        }
    })

@app.route('/animals', methods=['GET'])
def list_animals():
    """Restituisce la lista di tutti gli animali nel rifugio."""
    animals_info = [animal.info() for animal in shelter.list_all()]
    return jsonify(animals_info)

@app.route('/animals/<string:animal_id>', methods=['GET'])
def get_animal(animal_id: str):
    """Restituisce i dettagli di un singolo animale."""
    animal = shelter.get(animal_id)
    if not animal:
        return jsonify({"Error": "Animal not found"}), 404
    return jsonify(animal.info())

@app.route('/animals/<string:animal_id>/food', methods=['GET'])
def get_food(animal_id: str):
    """Restituisce il cibo giornaliero consigliato per l'animale."""
    animal = shelter.get(animal_id)
    if not animal:
        return jsonify({"Error": "Animal not found"}), 404
    return jsonify({
        "id": animal.id,
        "name": animal.name,
        "species": animal.species,
        "daily_food_grams": animal.daily_food_grams()
    })

@app.route('/animals/<string:animal_id>/adoption', methods=['GET'])
def get_adoption(animal_id: str):
    """Restituisce lo stato di adozione dell'animale."""
    animal = shelter.get(animal_id)
    if not animal:
        return jsonify({"Error": "Animal not found"}), 404
    
    if shelter.is_adopted(animal_id):
        adopter = shelter.get_adopter(animal_id)
        return jsonify({
            "id": animal.id, 
            "adopter": True,
            "adopter_name": adopter
        })
    else:
        return jsonify({
            "id": animal.id,
            "adopter": False
            
        })
    
@app.route('/animals/add', methods=["POST"])
def add_animal():
    """
    Aggiunge un nuovo animale.
    Body JSON richiesto:
    - type: "dog" o "cat"
    - campi comuni: id, name, age_years, weight_kg
    - per dog: breed, is_trained
    - per cat: indoor_only, favorite_toy
    """

    dati = request.get_json()
    if dati is None:
        return jsonify({"Error": "Invalid or missing JSON body"}), 400
    
    animal_type = dati.get("type")
    animal_id = dati.get("id")
    name = dati.get("name")
    age_years = dati.get("age_years")
    weight_kg = dati.get("weight_kg")

    if not all([animal_type, animal_id, name]) or age_years is None or weight_kg is None:
        return jsonify({"Error": "Missing required fields"}), 400
    
    if shelter.get(animal_id) is not None:
        return jsonify({"Error": "Animal with this id already exist"})

    if animal_type not in ["dog", "cat"]:
        return jsonify({"Errore": "Animal type not valid"})
    
    try:
        age_years = int(age_years)
        weight_kg = float(weight_kg)
    except ValueError:
        return jsonify({"Error": "age_years must be int, weight_kg must be float"}), 400
    
    if animal_type == "dog":
        breed = dati.get("breed")
        is_trained = dati.get("is_trained")
        if breed is None or is_trained is None:
            return jsonify({"Error": "Missing fields for dog: breed, is_trained"}), 400
        animal = Dog(animal_id=animal_id, name=name, age_years=age_years, breed=breed, is_trained=bool(is_trained))       
    elif animal_type == "cat":
        indoor_only = dati.get("indoor_only"),
        favorite_toy = dati.get("favorite_toy")
        if indoor_only is None or favorite_toy is None:
            return jsonify({"Error": "Missing field for the cat: indoor_only, favorite_toy"}), 400
        animal = Cat(animal_id=animal_id, name=name,age_years=age_years, indoor_only=bool(indoor_only), favorite_toy=favorite_toy)
    else:
        return jsonify({"Error": "Unknown animal type, expected 'dog' or 'cat'"}), 400
    
    shelter.add(animal)
    return jsonify({
        "status": "ok", 
        "added": animal.info()
    }), 201 

@app.route('/animals/<string:animal_id>/adopt', methods=['POST'])
def adopt_animal(animal_id: str):
    """
    Registra l'adozione di un animale.
    Body JSON:
    {
        "adopter_name": "Mario Rossi"
    }
    """
    animal = shelter.get(animal_id)
    if not animal:
        return jsonify({"Error": "Animal not found"}), 404
    
    if shelter.is_adopted(animal_id):
        return jsonify({"Error": "Animal already adopted"}), 400
    
    dati = request.get_json()
    if not dati or "adopter_name" not in dati:
        return jsonify({"Error": "JSON must contain at least one adopter_name"}), 400

    adopter_name = dati["adopter_name"] #oppure shelter.get("adopter_name")
    if not adopter_name:
        return jsonify({"Error": "Missing adopter name"}), 400
    
    shelter.set_adopted(animal_id, adopter_name)
    
    return jsonify({
        "id": animal_id,
        "adopted": True,
        "adopter_name": adopter_name
    }), 200


if __name__ == "__main__":
    # Avvia il server in debug sulla porta 5000
    app.run(debug=True, host="127.0.0.1", port=5000)


        
    


