from abc import ABC, abstractmethod
from flask import Flask, jsonify, request, url_for

# ==========================
# Classi di dominio
# ==========================

class Animal(ABC):
    def __init__(self, animal_id: str, name: str, age_years: int, weight_kg: float):
        self.id = animal_id
        self.name = name
        self.age_years = age_years
        self.weight_kg = weight_kg

    @abstractmethod
    def species(self) -> str:
        """Specie dell'animale (dog, cat, ...)"""
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
            "weight_kg": self.weight_kg,
            "bmi_like": self.bmi_like(),
        }


class Dog(Animal):
    def __init__(self, animal_id: str, name: str, age_years: int, weight_kg: float,
                 breed: str, is_trained: bool):
        super().__init__(animal_id, name, age_years, weight_kg)
        self.breed = breed
        self.is_trained = is_trained

    def species(self) -> str:
        return "dog"

    def daily_food_grams(self) -> int:
        # Formula semplice e "plausibile"
        return 200 + self.age_years * 50

    def info(self) -> dict:
        base = super().info()
        base["breed"] = self.breed
        base["is_trained"] = self.is_trained
        return base


class Cat(Animal):
    def __init__(self, animal_id: str, name: str, age_years: int, weight_kg: float,
                 indoor_only: bool, favorite_toy: str):
        super().__init__(animal_id, name, age_years, weight_kg)
        self.indoor_only = indoor_only
        self.favorite_toy = favorite_toy

    def species(self) -> str:
        return "cat"

    def daily_food_grams(self) -> int:
        # Anche qui una formula inventata ma coerente
        return 100 + self.age_years * 30

    def info(self) -> dict:
        base = super().info()
        base["indoor_only"] = self.indoor_only
        base["favorite_toy"] = self.favorite_toy
        return base


class Shelter:
    def __init__(self):
        self.animals: dict[str, Animal] = {}
        # adoptions: id -> nome adottante
        self.adoptions: dict[str, str] = {}

    def add(self, animal: Animal) -> bool:
        """Aggiunge un animale. Ritorna False se l'id esiste già."""
        if animal.id in self.animals:
            return False
        self.animals[animal.id] = animal
        return True

    def get(self, animal_id: str) -> Animal | None:
        return self.animals.get(animal_id)

    def list_all(self) -> list[Animal]:
        return list(self.animals.values())

    def is_adopted(self, animal_id: str) -> bool:
        return animal_id in self.adoptions

    def set_adopted(self, animal_id: str, adopter_name: str) -> None:
        self.adoptions[animal_id] = adopter_name

    def get_adopter(self, animal_id: str) -> str | None:
        return self.adoptions.get(animal_id)


# ==========================
# Inizializzazione dati
# ==========================

shelter = Shelter()

# Aggiungiamo un cane e un gatto di esempio
dog1 = Dog(animal_id="d1", name="Rex", age_years=2, weight_kg=18.5,
           breed="border collie", is_trained=True)
cat1 = Cat(animal_id="c1", name="Micia", age_years=3, weight_kg=4.2,
           indoor_only=True, favorite_toy="ball")

shelter.add(dog1)
shelter.add(cat1)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    new_sample = "dog123"
    return jsonify({
        "message": "Welcome to Animal Shelter API",
        "links": {
            "get_animals": url_for("get_animal_list"),
            "get_animal": url_for("get_animal", animal_id=new_sample),
            "get_estimated_food": url_for("get_estimated_food", animal_id=new_sample),
            "animal_adoption": url_for("animal_adoption", animal_id=new_sample),
            "create_animal": url_for("add_animal")
        }
    })

@app.route('/animals', methods=['GET'])
def get_animals():
    animals_info = [animal.info() for animal in shelter.list_all()]
    return jsonify(animals_info)

@app.route('/animals/<string:animal_id>', methods=['GET'])
def get_animal(animal_id):
    animal = shelter.get(animal_id)
    if animal is None:
        return jsonify({"error": "Animal not found"}), 404 
    return jsonify(animal.info())

@app.route('/animals/<string:animal_id>/food', methods=['GET'])
def get_estimated_food(animal_id: str):
    animal = shelter.get(animal_id)
    if animal is None:
        return jsonify({"error": "Animal not found"}), 404
    
    food = animal.daily_food_grams()
    return jsonify({
        "id":animal.id,
        "name": animal.name,
        "species": animal.species,
        "daily_food_grams":food
    }), 200

@app.route('/animals/<string:animal_id>/adoption', methods=['GET'])
def get_animal_adoption(animal_id: str):
    animal = shelter.get(animal_id)
    if animal is None:
        return jsonify({"error": "Animal not found"}), 404
    
    if shelter.is_adopted(animal):
        adopter = shelter.get_adopter(animal)
        return jsonify({
            "id":animal.id,
            "adopted":True,
            "adopter_name":adopter
        })
    else:
        return jsonify({
            "id":animal.id,
            "adopterd":False 
        })

@app.route('/animals', methods=['POST'])
def add_animal():
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Data must be a JSON object"}), 400
    
    species = data["species"]
    if species not in data:
        return jsonify({"error": "Missing 'species' field"}), 400
    
    try:
        if species == "dog":
            required_fields = ['id', 'name', 'species', 'age_years', 'weight_kg', 'bmi_like', 'breed', 'is_trained']
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": "Missing required fields"}), 400
            
            animal = Dog(
                species=data["species"],
                id=data["animal_id"],
                name=data["name"],
                age_years=data["age_years"], 
                weight_kg=data["weight_kg"],
                bmi_like=data["bmi_like"],
                breed=data["breed"],
                is_trained=data["is_trained"]
            )

        elif species == "cat":
            required_fields = ['id', 'name', 'species', 'age_years', 'weight_kg', 'bmi_like', 'indoor_only', 'favorite_toy']
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": "Missing required fields"}), 400
            
            animal = Cat(
                species=data["species"],
                id=data["animal_id"],
                name=data["name"],
                age_years=data["age_years"],
                weight_kg=data["weight_kg"],
                bmi_like=data["bmi_like"],
                indoor_only=data["indoor_only"],
                favorite_toy=data["favorite_toy"]
            )

        else:
            return jsonify({"error": "Input not valid"}), 400

        ok = shelter.add(animal)
        if not ok:
            return jsonify({"error": "Animal already exist"}), 400
        return jsonify({"status": "ok", "added": animal.info()})
    
    except KeyError:
        return jsonify({"error": "Invalid data. Missing required fields"}), 400
    
@app.route('/animals/<string:animal_id>/adopt', method=['POST'])
def animal_adoption(animal_id: str):
    animal = shelter.get(animal_id)
    if animal is None:
        return jsonify({"error": "Animal not found"}), 404
    
    if shelter.is_adopted(animal):
        return jsonify({"error": "Animal already adopted"}), 400
    
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "dData must be a JSON object"}), 400
    
    adopter_name = data["adopter_name"]
    if "adopter_name" not in data:
        return jsonify({"error": "Missing 'adopter_name' field"}), 400

    shelter.set_adopted(animal_id, adopter_name)

    return jsonify({
        "id":animal_id,
        "adopted": True,
        "adopter_name":adopter_name
    }), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
