from abc import ABC, abstractmethod
from flask import Flask, jsonify, request, url_for

# ==========================
# Classi di dominio
# ==========================

class Device(ABC):
    """
    Classe astratta che rappresenta un dispositivo generico
    preso in carico dal centro di assistenza.
    """

    def __init__(
        self,
        device_id: str,
        model: str,
        customer_name: str,
        purchase_year: int,
        status: str,
    ):
        self.id = device_id
        self.model = model
        self.customer_name = customer_name
        self.purchase_year = purchase_year
        self.status = status

    @abstractmethod
    def device_type(self) -> str:
        """Tipo di dispositivo (es. smartphone, laptop)."""
        pass

    @abstractmethod
    def base_diagnosis_time(self) -> int:
        """Tempo base di diagnosi in minuti."""
        pass

    @abstractmethod
    def repair_complexity(self) -> int:
        """Indice di complessità della riparazione."""
        pass

    def info(self) -> dict:
        """Restituisce un dizionario con le informazioni principali del device."""
        return {
            "id": self.id,
            "device_type": self.device_type(),
            "model": self.model,
            "customer_name": self.customer_name,
            "purchase_year": self.purchase_year,
            "status": self.status,
        }

    def estimated_total_time(self, factor: float = 1.0) -> int:
        """
        Tempo totale stimato in minuti, in base al tempo base di diagnosi,
        alla complessità di riparazione e a un fattore di carico.
        Formula totalmente inventata, ma coerente.
        """
        base = self.base_diagnosis_time()
        complexity = self.repair_complexity()
        estimate = base * factor + complexity * 30
        # Restituiamo un intero (arrotondando per eccesso)
        return int(round(estimate))


class Smartphone(Device):
    """
    Sottoclasse che rappresenta uno smartphone.
    """

    def __init__(
        self,
        device_id: str,
        model: str,
        customer_name: str,
        purchase_year: int,
        status: str,
        has_protective_case: bool,
        storage_gb: int,
    ):
        super().__init__(device_id, model, customer_name, purchase_year, status)
        self.has_protective_case = has_protective_case
        self.storage_gb = storage_gb

    def device_type(self) -> str:
        return "smartphone"

    def base_diagnosis_time(self) -> int:
        # Ad esempio, diagnosi più veloce
        return 20

    def repair_complexity(self) -> int:
        # Complessità media
        return 2

    def info(self) -> dict:
        base = super().info()
        base["has_protective_case"] = self.has_protective_case
        base["storage_gb"] = self.storage_gb
        return base


class Laptop(Device):
    """
    Sottoclasse che rappresenta un laptop.
    """

    def __init__(
        self,
        device_id: str,
        model: str,
        customer_name: str,
        purchase_year: int,
        status: str,
        has_dedicated_gpu: bool,
        screen_size_inches: float,
    ):
        super().__init__(device_id, model, customer_name, purchase_year, status)
        self.has_dedicated_gpu = has_dedicated_gpu
        self.screen_size_inches = screen_size_inches

    def device_type(self) -> str:
        return "laptop"

    def base_diagnosis_time(self) -> int:
        # Diagnosi più lunga rispetto allo smartphone
        return 40

    def repair_complexity(self) -> int:
        # Complessità un po' più alta
        return 3

    def info(self) -> dict:
        base = super().info()
        base["has_dedicated_gpu"] = self.has_dedicated_gpu
        base["screen_size_inches"] = self.screen_size_inches
        return base


class ServiceCenter:
    """
    Contenitore principale: gestisce i dispositivi presi in carico.
    """

    def __init__(self):
        self.devices = {}  # id -> Device

    def add(self, device: Device) -> bool:
        """Aggiunge un device. Ritorna False se l'id esiste già."""
        if device.id in self.devices:
            return False
        self.devices[device.id] = device
        return True

    def get(self, device_id: str):
        return self.devices.get(device_id)

    def list_all(self):
        return list(self.devices.values())

    def update(self, device_id: str, new_device: Device) -> None:
        """
        Sostituisce (o crea) il device con id device_id.
        Qui adottiamo comportamento tipo 'upsert':
        se non esiste, lo crea.
        """
        self.devices[device_id] = new_device

    def patch_status(self, device_id: str, new_status: str) -> bool:
        """Aggiorna solo lo status del device. Ritorna False se non esiste."""
        device = self.get(device_id)
        if device is None:
            return False
        device.status = new_status
        return True

    def delete(self, device_id: str) -> bool:
        """Elimina un device. Ritorna False se non esiste."""
        if device_id in self.devices:
            del self.devices[device_id]
            return True
        return False


# ==========================
# Setup iniziale
# ==========================

service_center = ServiceCenter()

# Dispositivi di esempio
d1 = Smartphone(
    device_id="d1",
    model="iPhone 13",
    customer_name="Alice",
    purchase_year=2021,
    status="received",
    has_protective_case=True,
    storage_gb=128,
)

d2 = Laptop(
    device_id="d2",
    model="ThinkPad X1",
    customer_name="Bob",
    purchase_year=2019,
    status="diagnosing",
    has_dedicated_gpu=False,
    screen_size_inches=14.0,
)

service_center.add(d1)
service_center.add(d2)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    new_device = "123cd"
    return jsonify({
        "message": "Welcome to Service Center API",
        "links": {
            "get_devices": url_for("get_devices"),
            "device_example": url_for("get_device", device_id=new_device),
            "get_estimated": url_for("get_estimated", device_id=new_device, factor=1.0),
            "post_device": url_for("add_device"),
            "put_device": url_for("pur_device", device_id=new_device),
            "patch_device": url_for("patch_device", device_id=new_device),
            "delete_device": url_for("delete_device")
        }
    })

@app.route('/devices', methods=['GET'])
def get_devices():
    return jsonify(service_center.list_all())

@app.route('/devices/<string:device_id>', methods=['GET'])
def get_device(device_id):
    device = service_center.get(device_id)
    if device is None:
        return jsonify({"error": "Device not found"}), 404
    return jsonify(device.info())

@app.route('/devices/<string:device_id>/estimate/<float:factor>', methods=['GET'])
def get_estimated(device_id: str, factor: float):
    device = service_center.get(device_id)
    if device is None:
        return jsonify({"error": "Device not found"}), 404
    
    try:
        factor_float = float(factor)
    except Exception:
        return jsonify({"error": "Factor must be float"}), 400
    
    return jsonify({
        "id":device.id,
        "device_type":device.device_type(),
        "factor":factor_float,
        "estimated_total_minutes": device.estimated_total_time(factor_float)
    }), 200

@app.route('/devices', methods=['POST'])
def add_device():
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "data must be a JSON object"}), 400
    
    if "device_type" not in data:
        return jsonify({"error": "Missing field"}), 400
    
    device_type = data["device_type"]
    
    try: 
        if device_type == "smartphone":
            required_fields = ['device_id', 'device_type', 'model', 'customer_name', 'purchase_year', 'status', 'has_protective_case', 'storage_gb']
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": "Missing required fields"}), 400
                
            device = Smartphone(
                device_id=data["device_id"],
                device_type=data["device_type"],
                model=data["model"],
                customer_name=data["customer_name"],
                purchase_year=data["purchase_year"],
                status=data["status"],
                has_protective_case=data["has_protective_case"],
                storage_gb=data["storage_gb"]
            )

        elif device_type == "laptop":
            required_fields = ['device_id', 'device_type', 'model', 'customer_name', 'purchase_year', 'status', 'has_dedicated_gpu', 'screen_size_inches']
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": "Missing required fields"}), 400
                
            device = Laptop(
                device_id=data["id"],
                device_type=data["device_type"],
                model=data["model"],
                customer_name=data["customer_name"],
                purchase_year=data["purchase_year"],
                status=data["status"],
                has_dedicated_gpu=data["has_dedicated_gpu"],
                screen_size_inches=data["screen_size_inches"]
            )

        else:
            return jsonify({"error": "Device Type not valid"}), 400
        
        added_device = service_center.add(device)
        if not added_device:
            return jsonify({"error": "Device already exist"}), 400
        return jsonify({device.info()})
        
    except KeyError:
        return jsonify({"error": "Invalid data. Missing required fields"}), 400
    
@app.route('/devices/<string:device_id>', methods=['PUT'])
def put_device(device_id: str):
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Data must be a JSON object"}), 400

    device = service_center.get(device_id)
    if device is None:
        return jsonify({"error": "Device not found"}), 404

    if "device_type" not in data:
        return jsonify({"error": "Missing required field"}), 400
    device_type = data["device_type"] 

    try:
        if device_type == "smartphone":
            required_fields = ['device_type', 'model', 'customer_name', 'purchase_year', 'status', 'has_protective_case', "storage_gb"]
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": "Missing required fields"}), 400

            device = Smartphone(
                device_id=device_id,
                device_type=data["device_type"],
                model=data["model"],
                customer_name=data["customer_name"], 
                purchase_year=data["purchase_year"],
                status=data["status"],
                has_protective_case=data["has_protective_case"],
                storage_gb=data["storage_gb"]
            )     

        elif device_type == "laptop":
            required_fields = ['device_id', 'device_type', 'model', 'customer_name', 'purchase_year', 'status', 'has_dedicated_gpu', 'screen_size_inches']
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": "Missing required fields"}), 400
                
            device = Laptop(
                device_id=device_id,
                device_type=data["device_type"],
                model=data["model"], 
                customer_name=data["customer_name"],
                purchase_year=data["purchase_year"],
                status=data["status"],
                has_dedicated_gpu=data["has_dedicated_gpu"],
                screen_size_inches=data["screen_size_inches"]
            )

        else:
            return jsonify({"error": "Device Type not valid"}), 400 
    
        service_center.update(device_id, device)
        return jsonify({device.info()})
    
    except KeyError:
        return jsonify({"error": "Invalid data. Missing required fields"}), 400
    
@app.route('/devices/<string:device_id>/status', methods=['PATCH'])
def patch_device(device_id: str):
    device = service_center.get(device_id)
    if device is None:
        return jsonify({"error": "Device not found"}), 404
    
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Data must be a JSON object"}), 400
    
    new_status = data["status"]
    if not new_status or not isinstance(new_status, str):
        return jsonify({"error": "Status not valid"}), 400
    
    service_center.patch_status(device_id, new_status)
    return jsonify(device.info())

@app.route('/devices/<string:device_id>', methods=['DELETE'])
def delete_device(device_id: str):
    deleted = service_center.delete(device_id)
    if not deleted:
        return jsonify({"error": "Device not found"}), 404
    return jsonify({"deleted": True, "device_id": device_id}), 201


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

    
