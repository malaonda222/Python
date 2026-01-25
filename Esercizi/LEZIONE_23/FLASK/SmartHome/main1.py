from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from flask import Flask, jsonify, request, url_for


# -----------------------------
# Domain model
# -----------------------------

ALLOWED_STATUSES = {"online", "offline", "updating", "error"}


class SmartDevice(ABC):
    """
    Abstract base class for a generic IoT device.
    """

    def __init__(
        self,
        serial_number: str,
        brand: str,
        room: str,
        installation_year: int,
        status: str,
    ) -> None:
        self.serial_number = serial_number
        self.brand = brand
        self.room = room
        self.installation_year = installation_year
        self.status = status

    @abstractmethod
    def device_type(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def energy_consumption(self) -> float | int:
        raise NotImplementedError

    @abstractmethod
    def connection_quality(self) -> int:
        raise NotImplementedError

    def info(self) -> dict[str, float | int | str | bool]:
        return {
            "serial_number": self.serial_number,
            "brand": self.brand,
            "room": self.room,
            "installation_year": self.installation_year,
            "status": self.status,
            "device_type": self.device_type(),
        }

    def diagnostics_time(self, factor: float = 1.0) -> int:
        """
        Estimated seconds for a full diagnostics run.

        Formula:
          energy_consumption() * factor + connection_quality() * 10
        """
        seconds = float(self.energy_consumption()) * float(factor) + self.connection_quality() * 10
        return int(round(seconds))


class SmartBulb(SmartDevice):
    def __init__(
        self,
        serial_number: str,
        brand: str,
        room: str,
        installation_year: int,
        status: str,
        brightness_lumens: int,
        color_capability: bool,
    ) -> None:
        super().__init__(serial_number, brand, room, installation_year, status)
        self.brightness_lumens = brightness_lumens
        self.color_capability = color_capability

    def device_type(self) -> str:
        return "bulb"

    def energy_consumption(self) -> float | int:
        # typical low consumption
        return 9

    def connection_quality(self) -> int:
        # typical low/medium requirement
        return 3

    def info(self) -> dict[str, float | int | str | bool]:
        data = super().info()
        data.update(
            {
                "brightness_lumens": self.brightness_lumens,
                "color_capability": self.color_capability,
            }
        )
        return data


class SecurityCamera(SmartDevice):
    def __init__(
        self,
        serial_number: str,
        brand: str,
        room: str,
        installation_year: int,
        status: str,
        resolution: str,
        night_vision: bool,
    ) -> None:
        super().__init__(serial_number, brand, room, installation_year, status)
        self.resolution = resolution
        self.night_vision = night_vision

    def device_type(self) -> str:
        return "camera"

    def energy_consumption(self) -> float | int:
        # typical higher consumption for cameras
        return 50

    def connection_quality(self) -> int:
        # high requirement for video streaming
        return 9

    def info(self) -> dict[str, float | int | str | bool]:
        data = super().info()
        data.update({"resolution": self.resolution, "night_vision": self.night_vision})
        return data


class IoTHub:
    def __init__(self) -> None:
        self.devices: dict[str, SmartDevice] = {}

    def add(self, device: SmartDevice) -> bool:
        if device.serial_number in self.devices:
            return False
        self.devices[device.serial_number] = device
        return True

    def get(self, serial_number: str) -> SmartDevice | None:
        return self.devices.get(serial_number)

    def update(self, serial_number: str, new_device: SmartDevice) -> None:
        self.devices[serial_number] = new_device

    def patch_status(self, serial_number: str, new_status: str) -> None:
        d = self.devices.get(serial_number)
        if d is None:
            return
        d.status = new_status

    def delete(self, serial_number: str) -> bool:
        if serial_number not in self.devices:
            return False
        del self.devices[serial_number]
        return True

    def list_all(self) -> list[dict[str, float | int | str | bool]]:
        return [d.info() for d in self.devices.values()]
    

app = Flask(__name__)
iot_hub = IoTHub()

# Sample data (at least one bulb and one camera)
iot_hub.add(
    SmartBulb(
        serial_number="SN-101",
        brand="Nest",
        room="Living Room",
        installation_year=2021,
        status="online",
        brightness_lumens=800,
        color_capability=True,
    )
)
iot_hub.add(
    SecurityCamera(
        serial_number="SN-202",
        brand="Ring",
        room="Entrance",
        installation_year=2020,
        status="offline",
        resolution="1080p",
        night_vision=True,
    )
)


@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Smart Home Hub API",
        "links": {
            "get_all_devices": url_for("get_all_devices"),
            "get_device": url_for("get_device", serial_number="SN-101"),
            "get_estimated_diagnostic": url_for("get_estimated_diagnostic", serial_number="SN-101", factor=1.0),
            "create_device": url_for("add_device"),
            "put_device": url_for("put_device", serial_number="SN-101"),
            "patch_device": url_for("patch_device", serial_number="SN-101"),
            "delete_device": url_for("delete_device")
        }
    })

@app.route('/devices', methods=['GET'])
def get_all_devices():
    return jsonify(iot_hub.list_all())

@app.route('/devices/<string:serial_number>', methods=['GET'])
def get_device(serial_number: str):
    device = iot_hub.get(serial_number)
    if device is None:
        return jsonify({"error": "Device not found"}), 404
    return jsonify(device.info())

@app.route('/devices/<string:serial_number>/diagnostic/<float:factor', methods=['GET'])
def get_estimated_diagnostic(serial_number: str, factor: float):
    device = iot_hub.get(serial_number)
    if device is None:
        return jsonify({"error": "Device not found"}), 404
    
    try:
        factor_float = float(factor)
    except Exception as e:
        return jsonify({"error": f"{str(e)}"}), 400
    
    return jsonify({
        "id": device.serial_number,
        "device_type": device.device_type(),
        "factor": factor_float,
        "diagnostic_seconds": device.diagnostics_time(factor_float)
    }), 200

@app.route('/devices', methods=['POST'])
def add_device():
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Data must be a JSON object"}), 400
    
    if "type" not in data:
        return jsonify({"error": "Missing required field 'type'"}), 400
    
    device_type = data["type"]

    if device_type == "bulb":
        required_fields = ['serial_number', 'brand', 'room', 'installation_year', 'status', 'brightness_lumens', 'color_capability']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field {field}"}), 400
        
        if not isinstance(data['brightness_lumens'], int) or data['brightness_lumens'] <= 0:
            return jsonify({"error": "brightness_lumens must be a positive number"}), 400

        if not isinstance(data['color_capability'], bool):
            return jsonify({"error": "color_capability must be a boolean"}), 400
        device = SmartBulb(
            serial_number=data["serial_number"], 
            brand=data["brand"],
            room=data["room"],
            installation_year=data["installation_year"],
            status=data["status"],
            brightness_lumens=data["brightness_lumens"],
            color_capability=data["color_capability"]
        )

    elif device_type == "camera":
        required_fields = ['serial_number', 'room', 'installation_year', 'status', 'resolution', 'night_vision']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": "Missing required fields"}), 400
            
        if not isinstance(data["resolution"], str) or 'x' not in data['resolution']:
            return jsonify({"error": "resolution must be a string"}), 400
        
        if not isinstance(data["night_vision"], bool):
            return jsonify({"error": "night_vision must be a boolean"}), 400
        device = SecurityCamera(
            serial_number=data["serial_number"],
            room=data["room"],
            installation_year=data["installation_year"],
            status=data["status"],
            resolution=data["resolution"],
            night_vision=data["night_vision"]
        )

    else:
        return jsonify({"error": "Invalid device type"}), 400
    
    ok = iot_hub.add(device)
    if not ok:
        return jsonify({"error": "Device already exist"}), 400
    return jsonify(device.info())    

@app.route('/devices/<string:serial_number', methods=['PUT'])
def put_device(serial_number: str):
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Data must be a JSON object"}), 400
    
    device = iot_hub.get(serial_number)
    if device is None:
        return jsonify({"error": "Device not found"}), 404
    
    if "type" not in data:
        return jsonify({"error": "Missing required field 'type'"}), 400
    
    device_type = data["type"]

    if device_type == "bulb":
        required_fields = ['serial_number', 'brand', 'room', 'installation_year', 'status', 'brightness_lumens', 'color_capability']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field {field}"}), 400
            
        if not isinstance(data["brightness_lumens"], int) or data["brightness_lumens"] <= 0:
            return jsonify({"error": "brightness_lumens must be integer and greater than 0"}), 400
        
        if not isinstance(data["color_capability"], bool):
            return jsonify({"error": "color_capability must be boolean"}), 400
        
        device = SmartBulb(
            serial_number=serial_number,
            brand=data["brand"],
            room=data["room"],
            installation_year=data["installation_year"],
            status=data["status"],
            brightness_lumens=data["brightness_lumens"],
            color_capability=data["color_capability"]
        )

    elif device_type == "camera":
        required_fields = ['serial_number', 'brand', 'room', 'installation_year', 'status', 'resolution', 'night_vision']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required fields {field}"}), 400
        
        if not isinstance(data["resolution"], str) or 'x' not in data["resolution"]:
            return jsonify({"error": "resolution must be a string and has to have 'x'"}), 400
        
        if not isinstance(data["night_vision"], bool):
            return jsonify({"error": "night_vision must be a boolean"}), 400
        
        device = SecurityCamera(
            serial_number=serial_number,
            brand=data["brand"],
            room=data["room"],
            installation_year=data["installation_year"],
            status=data["status"],
            resolution=data["resolution"],
            color_capability=data["color_capability"]
        )
    
    else:
        return jsonify({"error": "Invalid device type"}), 400
    
    iot_hub.update(serial_number, device)
    return jsonify(device.info())

@app.route('/devices/<string:serial_number>/status', methods=['PATCH'])
def patch_device(serial_number: str):
    device = iot_hub.get(serial_number)
    if device is None:
        return jsonify({"error": "Device not found"}), 404
    
    data = request.get_json()
    if "status" not in data:
        return jsonify({"error": "Missing 'status' field"}), 400
    
    new_status = data["status"]
    if not isinstance(data["status"], str) or new_status not in ALLOWED_STATUSES:
        return jsonify({"error": f"Status must be a string and one of the {ALLOWED_STATUSES}"}), 400
    
    iot_hub.patch_status(serial_number, new_status)
    return jsonify(iot_hub.get(serial_number).info()), 200

@app.route('/devices/<string:serial_number>', methods=['DELETE'])
def delete_device(serial_number: str):
    deleted = iot_hub.delete(serial_number)
    if not deleted:
        return jsonify({"error": "Device not found"}), 404
    return jsonify({"deleted": True, "serial_number": serial_number}), 200 

if __name__ == "__main__":
    app.run(host="127.0.0.1:5000", port=5000, debug=True)
    