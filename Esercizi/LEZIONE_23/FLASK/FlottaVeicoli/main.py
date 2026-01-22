from __future__ import annotations
from flask import Flask, jsonify, url_for, request
from abc import ABC, abstractmethod 

class Vehicle(ABC):
    def __init__(self, plate_id: str, model: str, driver_name: str | None, registration_year: int, status: str) -> None:
        if status not in (
            "available",
            "rented",
            "maintenanace",
            "cleaning",
            "retired"
        ):
            raise ValueError("Invalid syntax")
    
        self.plate_id: str = plate_id
        self.model: str = model 
        self.driver_name: str = driver_name if driver_name else None 
        self.registration_year: int = registration_year
        self.status: str = status 

    @abstractmethod
    def vehicle_type(self):
        pass 

    @abstractmethod
    def base_cleaning_time(self):
        pass 

    @abstractmethod
    def wear_level(self):
        pass 

    def info(self) -> dict:
        return {
            "plate_id": self.plate_id,
            "model": self.model,
            "driver_name": self.driver_name,
            "vehicle_type": self.vehicle_type(),
            "registration_year": self.registration_year(),
            "status": self.status,
        }
    
    def estimated_prep_time(self, factor: float = 1.0) -> int:
        base = self.base_cleaning_time()
        wear_level = self.wear_level()
        estimated = base * factor + wear_level * 15
        return int(round(estimated))
    

class Car(Vehicle):
    def __init__(self, plate_id: str, model: str, driver_name: str| None, registration_year: int, status: str, doors: int, is_cabrio: bool) -> None:
        super().__init__(plate_id, model, driver_name, registration_year, status)
        self.doors: int = doors 
        self.is_cabrio: bool = is_cabrio
    
    def vehicle_type(self) -> str:
        return "car"
    
    def base_cleaning_time(self) -> int:
        return 30 
    
    def wear_level(self) -> int:
        return 2 
    
    def info(self) -> dict:
        info_base = super().info()
        info_base["doors"] = self.doors
        info_base["is_cabrio"] = self.is_cabrio
        return info_base
    

class Van(Vehicle):
    def __init__(self, plate_id: str, model: str, driver_name: str| None, registration_year: int, status: str, max_load_kg: int, require_special_license: bool) -> None:
        super().__init__(plate_id, model, driver_name, registration_year, status)
        self.max_load_kg: int = max_load_kg
        self.require_special_license: bool = require_special_license
    
    def vehicle_type(self) -> str:
        return "van"
    
    def base_cleaning_time(self) -> int:
        return 60
    
    def wear_level(self) -> int:
        return 4
    
    def info(self) -> dict:
        info_base = super().info()
        info_base["max_load_kg"] = self.max_load_kg
        info_base["require_special_license"] = self.require_special_license
        return info_base
    
class FleetManager:
    def __init__(self) -> None:
        self.vehicles: dict[str, Vehicle]
    
    def add_vehicle(self, vehicle: Vehicle) -> bool:
        if vehicle.plate_id not in self.vehicles:
            return False 
        self.vehicles[vehicle.plate_id] = vehicle 
        return True 
    
    def get(self, plate_id: str) -> Vehicle | None:
        if plate_id not in self.vehicles:
            return None 
        return self.vehicles[plate_id]
    
    def update(self, plate_id: str, new_vehicle: Vehicle) -> None:
        self.vehicles[plate_id] = new_vehicle
    
    def patch_status(self, plate_id: str, new_status: str) -> None:
        self.vehicles[plate_id]["status"] = new_status
    
    def delete(self, plate_id: str) -> bool:
        if plate_id in self.vehicles:
            del self.vehicles[plate_id]
            return True
        return False
    
    def list_all(self) -> list[Vehicle]:
        return list(self.vehicles.values())
    

fm = FleetManager()

car1 = Car("DR567KI", "Fiat Punto", "Sandro Rossi", 2021, "rented", 5)
van1 = Van("GI908LO", "Doblo", "Sergio Bianchi", 2023, "cleaning", 18000, False)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    vehicle_id: str = car1.plate_id
    return jsonify({
        "message": "Welcome to Rent Service API",
        "links": {
            "vehicles_list": url_for("list_vehicles"),
            "example_vehicle_sample": url_for("vehicle_sample", plate_id=vehicle_id),
            "example_estimate": url_for("estimate_sample", plate_id=vehicle_id, factor=2.0),
            "vehicle_adding": url_for("add_vehicle")
        }
    })

@app.route('/vehicles', methods=['GET'])
def list_vehicles():
    vehicles = [vehicle.info() for vehicle in fm.list_all()]
    return vehicles

@app.route('/vehicles/<string:plate_id>', methods=['GET'])
def vehicle_sample(plate_id):
    vehicle = fm.vehicles.get(plate_id)
    if not vehicle:
        return jsonify({"Error": "Vehicle not found"}), 404
    return jsonify(vehicle.info()), 200

@app.route('/vehicles/<string:plate_id>/prep-time/<float:factor>')
def estimate_sample(plate_id, factor):
    vehicle = fm.vehicles.get(plate_id)
    if vehicle is None:
        return jsonify({"Error": "Vehicle not found"}), 404
    try:
        factor_float = float(factor)
    except ValueError:
        return jsonify({"Error": "Factor must be float"}), 400
    
    estimate = vehicle.estimated_prep_time(factor_float)
    return jsonify({
        "id": plate_id,
        "device_type": "car",
        "factor": 2.0,
        "estimated": estimate
    }), 200 

@app.route('/vehicles', methods=['POST'])
def add_vehicle():
    data = request.get_json()
    if data is None:
        return jsonify({"Error": "invalid or missing JSON body"}), 400
    
    plate_id = data.get("plate_id")
    model = data.get("model") 
    driver_name = data.get("driver_name") 
    registration_year = data.get("registration_year")
    status = data.get("status")
    
    if not all([plate_id, model, driver_name, registration_year, status]):
        return jsonify({"Error": "Missing mandatory fields"}), 400
    
    if model == "car":
        doors = data.get("doors") 
        is_cabrio = data.get("is_cabrio")
        if doors is None or is_cabrio is None:
            return jsonify({"Error": "Doors or is_cabrio values not valid"}), 400
        vehicle = Car(plate_id=plate_id, model=model, driver_name=driver_name, registration_year=registration_year, status=status, doors=doors, is_cabrio=is_cabrio)
    
    elif model == "van":
        max_load_kg = data.get("max_load_kg")
        require_special_license = data.get("require_special_license")
        if max_load_kg is None or require_special_license is None:
            return jsonify({"Error": "Missing mandatory fields"})
        vehicle = Van(plate_id=plate_id, model=model, driver_name=driver_name, registration_year=registration_year, status=status, max_load_kg=max_load_kg, require_special_license=require_special_license)

    else:
        return jsonify({"Error": "Vehicle must be car or van"}), 400
    
    fm.add_vehicle(vehicle)
    return jsonify({
        "status": "ok",
        "info": vehicle.info()
    }), 201

