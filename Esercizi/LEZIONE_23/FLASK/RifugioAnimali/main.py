from __future__ import annotations
from flask import Flask, jsonify, url_for, request
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float) -> None:
        self.id: str = id
        self.name: str = name 
        self.age_years: int = age_years
        self.weight_kg: float = weight_kg

    @abstractmethod
    def species(self):
        pass 

    @abstractmethod
    def daily_food_grams(self):
        pass 

    def info(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species(),
            "age_years": self.age_years,
            "weight_kg": self.age_weight_kg,
            "daily_food_grams": self.daily_food_grams()
        }
    
    def bmi_like(self):
        return self.weight_kg / (self.age_years + 1)
    

class Dog(Animal):
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float, breed: str, is_trained: bool) -> None:
        super().__init__(id, name, age_years, weight_kg)
        self.breed: str = breed
        self.is_trained: bool = is_trained
    
    def species(self):
        return "dog"
    
    def daily_food_grams(self):
        return round(200 + self.age_years * 50, 2)
    
    def info(self) -> dict:
        info_dict = super().info()
        info_dict["breed"] = self.breed
        info_dict["is_trained"] = self.is_trained
        return info_dict
    

class Cat(Animal):
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float, indoor_only: bool, favorite_toy: str) -> None:
        super().__init__(id, name, age_years, weight_kg)
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

    def add(self, animal: Animal):
        if animal.id in self.animals:
            raise ValueError("Errore. Id animale già esistente")
        self.animals[animal.id] = animal
    
    def get(self, animal_id: str) -> Animal | None:
        if animal_id not in self.animals:
            return None 
        else:
            return self.animals[animal_id]
    
    def list_all(self) -> list[Animal]:
        return [animal.info() for animal in self.animals.values()]

    def is_adopted(self, animal_id: str) -> bool:
        return animal_id in self.adoptions 
    
    def set_adopted(self, animal_id: str, adopter_name: str):
        self.adoptions[animal_id] = adopter_name


shelter = Shelter() 

fufi = Dog("123abc", "Fufi", 5, 20, "Labrador", True)
mira = Cat("456def", "Mira", 6, 3, False, "mouse")

shelter.add(fufi)
shelter.add(mira)


app = Flask(__name__)

@app.route('/')
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

@app.route('/animals')
def list_animals():
    animals_info = [animal.info() for animal in shelter.list_all()]
    return jsonify(animals_info)

@app.route('/animals/<string:animal_id>')
def get_animal(animal_id: str):
    animal = shelter.get(animal_id)
    if animal is None:
        return jsonify({"Error": "Animal not found"}), 404
    return jsonify(animal.info())

@app.route('/animals/<string:animal_id>/food')
def get_food(animal_id: str):
    animal = shelter.get(animal_id)
    if animal is None:
        return jsonify({"Error": "Animal not found"}), 404
    return jsonify(animal.daily_food_grams())

@app.route('/animals/<string:animal_id>/adoption')
def get_adoption(animal_id: str):
    animal = shelter.get(animal_id)
    return jsonify(animal.id, animal.is_adopted()) 

@app.route('/animals', methods=["POST"])
def add_animal():
    dati = request.get_json()
    if dati is None:
        return jsonify({"Error": "Invalid or missing JSON body"}), 400
    
    animal_type = dati.get("type")

    if animal_type not in ["dog", "cat"]:
        return jsonify({"Errore": "Animal type not valid"})
    
    common_fields = ["id", "name", "age_years", "weight_kg"]
    specific_field = ["breed", "is_trained"] if animal_type == "dog" else ["indoor_only", "favorite_toy"]
    fields = common_fields + specific_field

    missing_fields = [field for field in fields if field not in dati]
    if missing_fields:
        return jsonify({"Error": "Campi mancanti", "missing": missing_fields}), 400
    
    if shelter.get(dati['id']) is not None:
        return jsonify({"Error": "Animal id already exists"}), 400
    
    if animal_type == "dog":
        new_animal = Dog(
            id=dati["id"],
            name=dati["name"],
            age_years=dati["age_years"],
            weight_kg=dati["weight_kg"],
            breed=dati["breed"],
            is_trained=dati["is_trained"]
        )
    else:
        new_animal = Cat(
            id=dati["id"],
            name=dati["name"],
            age_years=dati["age_years"],
            weight_kg=dati["weigth_kg"],
            indoor_only=dati["indoor_only"],
            favorite_toy=dati["favorite_toy"]
        )
    
    shelter.add(new_animal)

    return jsonify({
        "status": "ok", 
        "added": {"id": "d3", "species": new_animal.species()}
    }), 201 

@app.route('/animals/<string:animal_id>', methods=['POST'])
def get_adoption(animal_id: str):
    dati = request.get_json()
    if not dati or "adopter_name" not in dati:
        return jsonify({"Error": "JSON must contain at least one adopter_name"}), 400

    animal = shelter.get(animal_id)
    if animal is None:
        return jsonify({"Error": "Animal not in the shelter"}), 404
    if shelter.is_adopted(animal_id):
        return jsonify({"Error": "Animal already exist"}), 400
        
    adopter_name = dati["adopter_name"]
    shelter.set_adopted(animal_id, adopter_name)
    
    return jsonify({
        "id": animal_id,
        "adopted": shelter.is_adopted(animal_id),
        "adopter_name": adopter_name
    }), 200


        
    


