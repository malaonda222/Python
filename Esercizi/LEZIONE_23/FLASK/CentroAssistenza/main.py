from __future__ import annotations
from flask import Flask, jsonify, url_for, request
from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, device_id: str, model: str, 
                 customer_name: str, purchase_year: int, status: str) -> None:
        if status not in (
            "received",
            "diagnosing",
            "repairing",
            "ready",
            "delivered"
        ):
            raise ValueError("Invalid status")
        
        self.device_id: str = device_id
        self.model: str = model
        self.customer_name: str = customer_name
        self.purchase_year: int = purchase_year
        self.status: str = status 

    @abstractmethod
    def device_type(self) -> str:
        pass 

    @abstractmethod
    def base_diagnosis_time(self) -> int:
        pass 

    @abstractmethod
    def repair_complexity(self) -> int:
        pass 

    def info(self) -> dict:
        return {
            "id": self.device_id,
            "device_type": self.device_type(),
            "model": self.model,
            "customer_name": self.customer_name,
            "purchase_year": self.purchase_year,
            "status": self.status,
        }
    
    def estimated_total_time(self, factor: float=1.0) -> int:
        base = self.base_diagnosis_time()
        complexity = self.repair_complexity()
        estimate = base * factor + complexity * 30
        return int(round(estimate))


class Smartphone(Device):
    def __init__(self, device_id: str, model: str, 
                 customer_name: str, purchase_year: int, status: str, has_protective_case: bool, storage_gb: int) -> None:
        super().__init__(device_id, model, customer_name, purchase_year, status)
        self.has_protective_case: bool = has_protective_case
        self.storage_gb: int = storage_gb

    def device_type(self) -> str:
        return "smartphone"

    def base_diagnosis_time(self) -> int:
        return 20 
    
    def repair_complexity(self) -> int:
        return 2
    
    def info(self) -> dict:
        base = super().info()
        base["has_protective_case"] = self.has_protective_case
        base["storage_gb"] = self.storage_gb
        return base 
    

class Laptop(Device):
    def __init__(self, device_id: str, model: str, 
                 customer_name: str, purchase_year: int, status: str, has_dedicated_gpu: bool, screen_size_inches: float) -> None:
        super().__init__(device_id, model, customer_name, purchase_year, status)
        self.has_dedicated_gpu: bool = has_dedicated_gpu
        self.screen_size_inches: float = screen_size_inches
    
    def device_type(self) -> str:
        return "laptop"
    
    def base_diagnosis_time(self) -> int:
        return 40

    def repair_complexity(self) -> int:
        return 3
    
    def info(self) -> dict:
        base = super().info()
        base["has_dedicated_gpu"] = self.has_dedicated_gpu
        base["screen_size_inches"] = self.screen_size_inches
        return base 


class ServiceCenter:
    def __init__(self) -> None:
        self.devices: dict[str, Device] = {}
    
    def add(self, device: Device) -> bool:
        if device.id in self.devices:
            return False 
        self.devices[device.id] = device
        return True 
    
    def get(self, device_id: Device):
        return self.devices.get(device_id)
    
    def list_all(self) -> list[Device]:
        return list(self.devices.values())
    
    def update(self, device_id: str, new_device: Device) -> None:
        self.devices[device_id] = new_device
    
    def patch_status(self, device_id: str, new_status: str) -> bool:
        device = self.get(device_id)
        if device is None:
            return False
        device.status = new_status
        return True 
        
    def delete(self, device_id: str) -> bool:
        if device_id in self.devices:
            del self.devices[device_id]
            return True
        return False

service_center = ServiceCenter()

d1 = Smartphone(device_id="dq", model="IPhone 13", customer_name="Gianni", purchase_year=2025, status="received", has_protective_case=True, storage_gb=128)

d2 = Laptop(device_id="d2", model="ThinkPad X1", customer_name="Bianca", purchase_year=2021, status="diagnosis", has_dedicated_gpu=False, screen_size_inches=14.0)

service_center.add(d1)
service_center.add(d2)



app = Flask(__name__)

def create_device_from_data(data: dict, device_id: str = None) -> Device:
    """
    Crea un oggetto Device (Smartphone o Laptop) a partire da un dizionario JSON.
    Se device_id è fornito, viene usato al posto di data["id"] (per PUT).
    """
    device_type = data.get("type")
    if device_type not in ("smartphone", "laptop"):
        raise ValueError("Unknown or missing 'type' field (expected 'smartphone' or 'laptop').")

    # Campi comuni
    if device_id is None:
        device_id = data.get("id")
    model = data.get("model")
    customer_name = data.get("customer_name")
    purchase_year = data.get("purchase_year")
    status = data.get("status")

    if not all([device_id, model, customer_name, purchase_year, status]):
        raise ValueError("Missing required common fields.")

    try:
        purchase_year = int(purchase_year)
    except ValueError:
        raise ValueError("purchase_year must be an integer.")

    if device_type == "smartphone":
        has_protective_case = data.get("has_protective_case")
        storage_gb = data.get("storage_gb")
        if has_protective_case is None or storage_gb is None:
            raise ValueError("Missing smartphone fields: has_protective_case, storage_gb.")
        try:
            storage_gb = int(storage_gb)
        except ValueError:
            raise ValueError("storage_gb must be an integer.")
        return Smartphone(
            device_id=device_id,
            model=model,
            customer_name=customer_name,
            purchase_year=purchase_year,
            status=status,
            has_protective_case=bool(has_protective_case),
            storage_gb=storage_gb,
        )

    else:  # laptop
        has_dedicated_gpu = data.get("has_dedicated_gpu")
        screen_size_inches = data.get("screen_size_inches")
        if has_dedicated_gpu is None or screen_size_inches is None:
            raise ValueError("Missing laptop fields: has_dedicated_gpu, screen_size_inches.")
        try:
            screen_size_inches = float(screen_size_inches)
        except ValueError:
            raise ValueError("screen_size_inches must be a float.")
        return Laptop(
            device_id=device_id,
            model=model,
            customer_name=customer_name,
            purchase_year=purchase_year,
            status=status,
            has_dedicated_gpu=bool(has_dedicated_gpu),
            screen_size_inches=screen_size_inches,
        )


@app.route('/', methods=['GET'])
def index():
    sample_id = "d1"
    return jsonify({
        "message": "Welcome to Service Center API",
        "links": {
            "list_devices": url_for("list_devices"),
            "sample_device": url_for("get_device", device_id=sample_id),
            "sample_estimate": url_for("get_estimate", device_id=sample_id, factor =1.5),
            "create_device": url_for("create_device"),
            "update_device_put": url_for("update_device", device_id=sample_id),
            "patch_status": url_for("patch_device_status", device_id=sample_id),
            "delete_device": url_for("delete_device", device_id=sample_id)
        }
    })

@app.route('/devices', methos=['GET'])
def list_devices():
    device_info = [device.info() for device in service_center.list_all()]
    return device_info

@app.route('/devices/<string:device_id>', methods=['GET'])
def get_device(device_id):
    device = service_center.get(device_id)
    if device is None:
        return jsonify({"Error": "Device not found"}), 404
    return jsonify(device.info())

@app.route('/devices/<string:device_id>/estimate/<float:factor>')
def get_estimate(device_id, factor):
    device = service_center.get(device_id)
    if device is None:
        return jsonify({"Error": "Device not found"}), 404
    try: 
        factor_float = float(factor)
    except ValueError:
        return jsonify({"Error": "Factor must be float"}), 400
    
    estimate = device.estimated_total_time(factor_float)
    return jsonify({
        "id": device.id,
        "device_type": device.device_type(),
        "factor": factor_float,
        "estimated_total_minutes": estimate,
    })

@app.route('/devices', methods=['POST'])
def create_device():
    data = request.get_json()
    if data is None:
        return jsonify({"Error": "Missing or invalid JSON body"}), 400
    try:
        device = create_device_from_data(data)
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    
    if service_center.get(device.id) is not None:
        return jsonify({"Error": "Device with this is already exist"}), 400
    
    service_center.add(device)
    return jsonify(device.info()), 201

@app.route('/devices/<string:device_id>', methods=['PUT'])
def update_device(device_id):
    data = request.get_json()
    if data is None:
        return jsonify({"Error": "Missing or invalid JSON body"}), 400
    try:
        device = create_device_from_data(data)
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
    
    service_center.update(device_id, device)
    return jsonify(device.info()), 200

@app.route('/devices/<string:device_id>/status', method=['PATCH'])
def patch_device_status(device_id):
    device = service_center.get(device_id)
    if device is None:
        return jsonify({"Error": "Device not found"}), 404
    
    data = request.get_json()
    if data is None:
        return jsonify({"Error": "Missing or invalid JSON body"}), 400
    
    new_status = data.get("status")
    if not new_status:
        return jsonify({"Error": "Missing or invalid JSON body"}), 400
    
    service_center.patch_status(device_id, new_status)
    return jsonify(device.info()), 200

@app.route('/devices/<string:device_id>', methods=['DELETE'])
def delete_device(device_id):
    deleted = service_center.delete(device_id)
    if not deleted:
        return jsonify({"Error": "Device not found"}), 404
    return jsonify({"deleted": True, "id": device_id}), 200 
    #oppure return "", 204 



if __name__ == "__main__":
    #Avvia il server in debug sulla porta 5000
    app.run(debug=True, host="127.0.0.1", port=5000)
    