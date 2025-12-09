from __future__ import annotations
from abc import ABC, abstractmethod
from flask import Flask, jsonify, url_for


class Ride(ABC):
    def __init__(self, id: str, name: str, min_height_cm: int) -> None:
        self.id: str = id 
        self.name: str = name 
        self.min_height_cm: int = min_height_cm

    @abstractmethod
    def category(self) -> str:
        pass 

    @abstractmethod
    def base_wait(self) -> int:
        pass 

    def info(self) -> dict:
        return {
            "id": self.id,
            "name": self.name, 
            "min-height_cm": self.min_height_cm,
            "category": self.category()
        } 

    def wait_time(self, crowd_factor: float = 1.0) -> int:
        base = self.base_wait()
        if base < 0:
            base = 0
        else:
            return round(base * crowd_factor)
    

class RollerCoaster(Ride):
    def __init__(self, id: str, name: str, min_height_cm: int, inversions: int) -> None:
        super().__init__(id, name, min_height_cm)
        self.inversions: int = inversions

    def category(self) -> str:
        return "roller_coaster"
    
    def base_wait(self) -> int:
        return 40
    
    def info(self) -> dict:
        info_dict = super().info()
        info_dict["inversions"] = self.inversions
        return info_dict
    

class Carousel(Ride):
    def __init__(self, id, name, min_height_cm, animals: list[str]) -> None:
        super().__init__(id, name, min_height_cm)
        self.animals =  animals

    def category(self) -> str:
        return "family"
    
    def base_wait(self) -> int:
        return 10
    
    def info(self) -> dict:
        info_dict = super().info()
        info_dict["animals"] = self.animals
        return info_dict
    

class Park:
    def __init__(self, rides: dict[str, Ride] | None = None) -> None:
        self.rides = rides if rides is not None else {}
    
    def add(self, ride: Ride) -> None:
        if ride is None:
            print("Errore: ride non valido")
            return
        else:
            self.rides[ride.id] = ride
    
    def get(self, ride_id: str) -> dict | None:
        if ride_id not in self.rides:
            print("Errore: ride ID non presente")
            return None 
        return self.rides[ride_id]

    def list_all(self) -> list[Ride] | None:
        if not self.rides:
            print(f"Nessun ride presente")
        else:
            return sorted(self.rides.values(),
                        key=lambda r: (r.category(), r.name))
        

# creazione delle attrazioni
roller_coaster101 = RollerCoaster(
    id='rc101',
    name='RollerCoaster101',
    min_height_cm=130,
    inversions=9
)

carousel89 = Carousel(
    id='c89',
    name='Carousel89',
    min_height_cm=60,
    animals=['horse', 'zebra', 'lion', 'elephant']
)

carousel22 = Carousel(
    id='56',
    name='Carousel22',
    min_height_cm=60,
    animals=['dog', 'cat', 'pig', 'bird']
)

park = Park()
park.add(roller_coaster101)
park.add(carousel89)
park.add(carousel22)

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Park API",
        "routes": {
            "all_rides": url_for('all_rides'),
            "ride_example": url_for('ride_details', ride_id="rc101"),
            "wait_example": url_for('wait_details', ride_id="rc101", crowd="3.0")
        }
    })

@app.route('/rides') 
def all_rides():
    rides_list = [
        {
            "id": r.id, 
            "name": r.name, 
            "category": r.category(),
            "min_height_cm": r.min_height_cm
        }
        for r in park.list_all()
    ]
    return jsonify(rides_list)

@app.route('/rides/<string:ride_id>')
def ride_details(ride_id: str):
    ride = park.get(ride_id)
    if ride is None:
        return jsonify({"Error" : "Ride not found"}), 404
    return jsonify(ride.info())

@app.route('/rides/<string:ride_id>/wait/<float:crowd>')
def wait_details(ride_id: str, crowd = 1.0):
    ride = park.get(ride_id)
    if ride is None:
        return jsonify({"Error" : "Ride ID not found"}), 404
    return jsonify({
        "id": ride_id,
        "wait_min" : ride.wait_time(crowd)
    })


if __name__ == "__main__":
    app.run(debug=True)