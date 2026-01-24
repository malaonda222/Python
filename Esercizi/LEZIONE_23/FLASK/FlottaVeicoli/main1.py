from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from flask import Flask, jsonify, request, url_for


# -----------------------------
# Domain model
# -----------------------------

ALLOWED_STATUSES = {"available", "rented", "maintenance", "cleaning", "retired"}


class Vehicle(ABC):
    """
    Abstract base class for a generic vehicle managed by the system.
    """

    def __init__(
        self,
        plate_id: str,
        model: str,
        driver_name: str | None,
        registration_year: int,
        status: str,
    ) -> None:
        # driver_name can be a string or None
        self.plate_id = plate_id
        self.model = model
        self.driver_name = driver_name
        self.registration_year = registration_year
        self.status = status

    @abstractmethod
    def vehicle_type(self) -> str:
        """Return the type of vehicle, e.g. 'car' or 'van'."""
        raise NotImplementedError

    @abstractmethod
    def base_cleaning_time(self) -> int:
        """Return ordinary cleaning time in minutes."""
        raise NotImplementedError

    @abstractmethod
    def wear_level(self) -> int:
        """Return average wear level for this type (1..5)."""
        raise NotImplementedError

    def info(self) -> dict[str, int | str | bool | None]:
        return {
            "plate_id": self.plate_id,
            "model": self.model,
            "driver_name": self.driver_name,
            "vehicle_type": self.vehicle_type(),
            "registration_year": self.registration_year,
            "status": self.status,
        }

    def estimated_prep_time(self, factor: float = 1.0) -> int:
        """
        Estimated preparation time before a new rent (cleaning + checks).

        Formula:
          base_cleaning_time() * factor + wear_level() * 15
        """
        minutes = self.base_cleaning_time() * float(factor) + self.wear_level() * 15
        return int(round(minutes))


class Car(Vehicle):
    def __init__(
        self,
        plate_id: str,
        model: str,
        driver_name: str | None,
        registration_year: int,
        status: str,
        doors: int,
        is_cabrio: bool,
    ) -> None:
        super().__init__(plate_id, model, driver_name, registration_year, status)
        self.doors = doors
        self.is_cabrio = is_cabrio

    def vehicle_type(self) -> str:
        return "car"

    def base_cleaning_time(self) -> int:
        return 30

    def wear_level(self) -> int:
        # Typical low wear for standard cars
        return 2

    def info(self) -> dict[str, int | str | bool | None]:
        data = super().info()
        data.update({"doors": self.doors, "is_cabrio": self.is_cabrio})
        return data


class Van(Vehicle):
    def __init__(
        self,
        plate_id: str,
        model: str,
        driver_name: str | None,
        registration_year: int,
        status: str,
        max_load_kg: int,
        require_special_license: bool,
    ) -> None:
        super().__init__(plate_id, model, driver_name, registration_year, status)
        self.max_load_kg = max_load_kg
        self.require_special_license = require_special_license

    def vehicle_type(self) -> str:
        return "van"

    def base_cleaning_time(self) -> int:
        return 60

    def wear_level(self) -> int:
        # Typical high wear for work vans
        return 5

    def info(self) -> dict[str, int | str | bool | None]:
        data = super().info()
        data.update(
            {
                "max_load_kg": self.max_load_kg,
                "require_special_license": self.require_special_license,
            }
        )
        return data


class FleetManager:
    def __init__(self) -> None:
        self.vehicles: dict[str, Vehicle] = {}

    def add(self, vehicle: Vehicle) -> bool:
        if vehicle.plate_id in self.vehicles:
            return False
        self.vehicles[vehicle.plate_id] = vehicle
        return True

    def get(self, plate_id: str) -> Vehicle | None:
        return self.vehicles.get(plate_id)

    def update(self, plate_id: str, new_vehicle: Vehicle) -> None:
        self.vehicles[plate_id] = new_vehicle

    def patch_status(self, plate_id: str, new_status: str) -> None:
        v = self.vehicles.get(plate_id)
        if v is None:
            return
        v.status = new_status

    def delete(self, plate_id: str) -> bool:
        if plate_id not in self.vehicles:
            return False
        del self.vehicles[plate_id]
        return True

    def list_all(self) -> list[dict[str, int | str | bool | None]]:
        return [v.info() for v in self.vehicles.values()]
    

# -----------------------------
# Flask app
# -----------------------------

app = Flask(__name__)
fleet_manager = FleetManager()

# Sample data (at least one Car and one Van)
fleet_manager.add(
    Car(
        plate_id="HA014AS",
        model="Fiat Panda",
        driver_name=None,
        registration_year=2019,
        status="available",
        doors=5,
        is_cabrio=False,
    )
)
fleet_manager.add(
    Van(
        plate_id="CC216FG",
        model="Peugeot Partner",
        driver_name="Luca Neri",
        registration_year=2018,
        status="rented",
        max_load_kg=750,
        require_special_license=False,
    )
)


@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to Rent Service API",
        "links": {
            "all_vehicles": url_for("get_all_vehicles"),
            "get_vehicle": url_for("get_vehicle", plate_id="HA014AS"),
            "estimate_sample": url_for("get_estimate_sample", plate_id="HA014AS", factor=2.0),
            "create_vehicle": url_for("add_vehicle"),
            "put_vehicle": url_for("put_vehicle", plate_id="HA014AS"),
            "patch_vehicle": url_for("patch_vehicle", plate_id="HA014AS"),
            "delete_vehicle": url_for("delete_vehicle")
        }
    }) 

@app.route('/vehicles', methods=['GET'])
def get_all_vehicles():
    return jsonify(fleet_manager.list_all())

@app.route('/vehicles/<string:plate_id>', methods=['GET'])
def get_vehicle(plate_id):
    vehicle = fleet_manager.get(plate_id)
    if vehicle is None:
        return jsonify({"error": "Vehicle not found"}), 404
    return jsonify(vehicle.info())

@app.route('/vehicles/<string:plate_id>/prep-time/<float:factor>', methods=['GET'])
def get_estimate_sample(plate_id: str, factor: float):
    vehicle = fleet_manager.get(plate_id)
    if vehicle is None:
        return jsonify({"error": "Vehicle not found"}), 404 
    
    try:
        factor_float = float(factor)
    except Exception:
        return jsonify({"error": "Factor must be float"}), 400

    prep_time = vehicle.estimated_prep_time(factor_float)
    return jsonify({
        "id":vehicle.plate_id,
        "device_type":vehicle.vehicle.type(),
        "factor":factor_float,
        "estimated_total_minutes":prep_time
    }), 200

@app.route('/vehicles', methods=['POST'])
def add_vehicle():
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Data must be a JSON object"}), 400
    
    if "type" not in data:
        return jsonify({"error": "Missing required field"}), 400
    
    vehicle_type = data["type"]
    try:
        if vehicle_type == "car":
            required_fields = ['plate_id', 'model', 'driver_name', 'vehicle_type', 'registration_year', 'status', 'doors', 'is_cabrio']
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": "Missing required fields"}), 400

            vehicle = Car(
                plate_id=data["plate_id"],
                model=data["model"],
                driver_name=data["driver_name"],
                registration_year=data["registration_year"],
                status=data["status"],
                doors=data["doors"],
                is_cabrio=data["is_cabrio"]
            )

        elif vehicle_type == "van":
            required_fields = ['plate_id', 'model', 'driver_name', 'vehicle_type', 'registration_year', 'status', 'doors', 'is_cabrio']
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": "Missing required fields"}), 400
            
            vehicle = Van(
                plate_id=data["plate_id"],
                model=data["model"],
                driver_name=data["driver_name"],
                registration_year=data["registration_year"],
                status=data["status"],
                max_load_kg=data["max_load_kg"],
                require_special_license=data["require_special_license"]
            )

        else:
            return jsonify({"error": "Type not valid; it must be 'car' or 'van'"}), 400

        ok = fleet_manager.add(vehicle)
        if not ok:
            return jsonify({"error": "Vehicle already exist"}), 400
        return jsonify(vehicle.info())

    except KeyError as e:
        return jsonify({"error": f"Missing field or invalid input: {str(e)}"}), 400

 @add.route('/vehicles/<string:plate_id>', methods=['PUT'])
 def put_vehicle(plate_id):
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Data must be a JSON object"}), 400
    
    vehicle = fleet_manager.get(plate_id)
    if vehicle is None:
        return jsonify({"error": "Vehicle not found"}), 404
    
    if "type" not in data:
        return jsonify({"error": "Missing required field"}), 400
    
    vehicle_type = data["type"]

    try:
        if vehicle_type == "car":
            required_fields = ['plate_id', 'model', 'driver_name', 'vehicle_type', 'registration_year', 'status', 'doors', 'is_cabrio']
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": "Missing required fields"}), 400
            
            vehicle = Car(
                plate_id=plate_id,
                model=data["model"],
                driver_name=data["driver_name"],
                registration_year=data["registration_year"],
                status=data["status"],
                doors=data["doors"],
                is_cabrio=data["is_cabrio"]  
            )

        elif vehicle_type == "van":
            required_fields = ['plate_id', 'model', 'driver_name', 'vehicle_type', 'registration_year', 'status', 'doors', 'is_cabrio']
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": "Missing required fields"}), 400
            
            vehicle = Van(
                plate_id=plate_id,
                model=data["model"],
                driver_name=data["driver_name"],
                registration_year=data["registration_year"],
                status=data["status"],
                doors=data["doors"],
                is_cabrio=data["is_cabrio"]
            )

        else:
            return jsonify({"error": "Invalid input; 'Type' must be car or van"}), 400
        
        fleet_manager.update(plate_id, vehicle)
        return jsonify(vehicle.info())

    except KeyError as e:
        return jsonify({"error": "Missing required fields or invalid input"}), 400

@app.route("/vehicles/<string:plate_id>/status")
def patch_vehicle(plate_id: str):
    vehicle = fleet_manager(plate_id)
    if vehicle is None:
        return jsonify({"error": "Vehicle not found"}), 404

    data = request.get_json()
    if "status" not in data:
        return jsonify({"error": "Missing 'status' field"}), 400

    new_status = data["status"]
    if not isinstance(new_status, str) or new_status not in ALLOWED_STATUSES:
        return jsonify({"error": f"status must be one of {sorted(ALLOWED_STATUSES)}"})
    fleet_manager.patch_status(plate_id, new_status) 
    return jsonify(fleet_manager.get(plate_id).info())

@app.route('/vehicles', methods=['DELETE'])
def delete_vehicle():
    deleted = fleet_manager.get(plate_id)
    if not deleted:
        return jsonify({"error": "Vehicle not found"}), 404
    return jsonify("deleted": True, "id": plate_id), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)



