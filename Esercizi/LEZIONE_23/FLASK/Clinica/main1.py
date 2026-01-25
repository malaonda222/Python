from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any
from flask import Flask, jsonify, request, url_for


# ==========================
# Classi di dominio
# ==========================

class Booking(ABC):
    """
    Prenotazione astratta: non istanziabile direttamente.
    """

    def __init__(
        self,
        booking_id: str,
        patient_name: str,
        doctor: str,
        department: str,
        date: str,
        time: str,
        status: str,
    ):
        self.booking_id = booking_id
        self.patient_name = patient_name
        self.doctor = doctor
        self.department = department
        self.date = date
        self.time = time
        self.status = status

    @abstractmethod
    def booking_type(self) -> str:
        """Tipo prenotazione: visit / exam"""
        raise NotImplementedError

    @abstractmethod
    def base_duration(self) -> int:
        """Durata standard (minuti)."""
        raise NotImplementedError

    @abstractmethod
    def priority_level(self) -> int:
        """Priorità (1..10)."""
        raise NotImplementedError

    def info(self) -> dict[str, Any]:
        return {
            "booking_id": self.booking_id,
            "patient_name": self.patient_name,
            "doctor": self.doctor,
            "department": self.department,
            "date": self.date,
            "time": self.time,
            "status": self.status,
            "type": self.booking_type(),
        }

    def estimated_wait(self, factor: float = 1.0) -> int:
        """
        Attesa stimata (minuti):
        base_duration() * factor + priority_level() * 5
        """
        wait = self.base_duration() * float(factor) + self.priority_level() * 5
        return int(round(wait))


class MedicalVisit(Booking):
    def __init__(
        self,
        booking_id: str,
        patient_name: str,
        doctor: str,
        department: str,
        date: str,
        time: str,
        status: str,
        visit_reason: str,
        first_time: bool,
    ):
        super().__init__(booking_id, patient_name, doctor, department, date, time, status)
        self.visit_reason = visit_reason
        self.first_time = bool(first_time)

    def booking_type(self) -> str:
        return "visit"

    def base_duration(self) -> int:
        # Durata standard tipica di una visita (min)
        return 30 if self.first_time else 20

    def priority_level(self) -> int:
        # Semplice euristica: se motivo contiene parole "urgenti" alza priorità
        reason = (self.visit_reason or "").lower()
        keywords = ["urgente", "dolore", "acuto", "svenimento"]

        for k in keywords:
            if k in reason:
                return 7

        return 5

    def info(self) -> dict[str, Any]:
        base = super().info()
        base["visit_reason"] = self.visit_reason
        base["first_time"] = self.first_time
        return base


class DiagnosticExam(Booking):
    def __init__(
        self,
        booking_id: str,
        patient_name: str,
        doctor: str,
        department: str,
        date: str,
        time: str,
        status: str,
        exam_type: str,
        requires_fasting: bool,
    ):
        super().__init__(booking_id, patient_name, doctor, department, date, time, status)
        self.exam_type = exam_type
        self.requires_fasting = bool(requires_fasting)

    def booking_type(self) -> str:
        return "exam"

    def base_duration(self) -> int:
        # Durate indicative in base al tipo di esame
        et = (self.exam_type or "").strip().lower()
        if et in ["ecg", "e.c.g."]:
            return 15
        if et in ["rx", "x-ray", "radiografia"]:
            return 20
        if et in ["rmn", "mri", "tac", "ct"]:
            return 60
        return 30

    def priority_level(self) -> int:
        # Semplice euristica: RMN/TAC spesso più "critiche" o più impegnative
        et = (self.exam_type or "").strip().lower()
        if et in ["rmn", "mri", "tac", "ct"]:
            return 8
        return 7

    def info(self) -> dict[str, Any]:
        base = super().info()
        base["exam_type"] = self.exam_type
        base["requires_fasting"] = self.requires_fasting
        return base


class ClinicHub:
    def __init__(self):
        self.bookings: dict[str, Booking] = {}

    def add(self, booking: Booking) -> bool:
        if booking.booking_id in self.bookings:
            return False
        self.bookings[booking.booking_id] = booking
        return True

    def get(self, booking_id: str) -> Booking | None:
        return self.bookings.get(booking_id)

    def update(self, booking_id: str, new_booking: Booking) -> None:
        self.bookings[booking_id] = new_booking

    def patch_status(self, booking_id: str, new_status: str) -> None:
        b = self.bookings.get(booking_id)
        if b is not None:
            b.status = new_status

    def delete(self, booking_id: str) -> bool:
        if booking_id not in self.bookings:
            return False
        del self.bookings[booking_id]
        return True

    def list_all(self) -> list[dict[str, Any]]:
        return [b.info() for b in self.bookings.values()]


# ==========================
# Setup dati iniziali
# ==========================

clinic_hub = ClinicHub()

clinic_hub.add(
    MedicalVisit(
        booking_id="BK-101",
        patient_name="Mario Rossi",
        doctor="Dr. Bianchi",
        department="Cardiologia",
        date="2026-02-10",
        time="14:30",
        status="scheduled",
        visit_reason="Controllo annuale",
        first_time=False,
    )
)

clinic_hub.add(
    DiagnosticExam(
        booking_id="BK-202",
        patient_name="Giulia Verdi",
        doctor="Dr. Neri",
        department="Radiologia",
        date="2026-02-11",
        time="09:15",
        status="scheduled",
        exam_type="RMN",
        requires_fasting=True,
    )
)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Clinic Booking Hub API",
        "links": {
            "booking_list": url_for("get_all_bookings"),
            "booking_sample": url_for("get_booking", booking_id="BK-101"),
            "estimate_sample": url_for("get_estimate_sample", booking_id="BK-101", factor=1.0),
            "create_booking": url_for("add_booking"),
            "put_booking": url_for("put_booking", booking_id="BK-101"),
            "patch_booking": url_for("patch_booking", booking_id="BK-101"),
            "delete_booking": url_for("delete_booking", booking_id="BK-101")
        }
    })

@app.route('/bookings', methods=['GET'])
def get_bookings():
    return jsonify(clinic_hub.list_all())

@app.route('/bookings/<string:booking_id>', methods=['GET'])
def get_booking(booking_id: str):
    booking = clinic_hub.get(booking_id)
    if booking is None:
        return jsonify({"error": "Booking not found"}), 404 
    return jsonify(booking.info()), 200

@app.route('/bookings/<string:booking_id>/wait/<float:factor>', methods=['GET'])
def get_estimate_booking(booking_id: str, factor: float):
    booking = clinic_hub.get(booking_id)
    if booking is None:
        return jsonify({"error": "Booking not found"}), 404
    
    try:
        factor_float = float(factor)
    except Exception as e:
        return jsonify({"error": f"{str(e)}"}), 400
    
    return jsonify({
        "booking_id": booking.booking_id,
        "booking_type": booking.type(),
        "factor": factor_float,
        "estimated_wait_minutes": booking.estimated_wait(factor_float)
    }), 200

@app.route('/bookings', methods=['POST'])
def add_booking():
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Data must be a JSON object"}), 400
    
    if "type" not in data:
        return jsonify({"error": "Missing required field 'type'"}), 400
    
    booking_type = data["type"]
    if not isinstance(booking_type, str):
        return jsonify({"error": "'Type' must be a string"}), 400
    
    if booking_type == "visit":
        required_fields = ['booking_id', 'patient_name', 'doctor', 'department', 'date', 'time', 'status', 'visit_reason', 'first_time']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        if not isinstance(data["visit_reason"], str):
            return jsonify({"error": "visit_reason must be a string"}), 400
        
        if not isinstance(data["first_time"], bool):
            return jsonify({"error": "first_time must be a boolean"}), 400
        
        new_booking = MedicalVisit(
            booking_type=booking_type,
            booking_id=data["booking_id"],
            patient_name=data["patient_name"],
            doctor=data["doctor"],
            department=data["department"],
            date=data["date"],
            time=data["time"], 
            status=data["status"], 
            visit_reason=data["visit_reason"],
            first_time=data["first_time"]   
        )

    elif booking_type == "exam":
        required_fields = ['booking_id', 'patient_name', 'doctor', 'department', 'date', 'time', 'status', 'exam_type', 'requires_fasting']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
            
        if not isinstance(data["exam_type"], str):
            return jsonify({"error": "exam_type must be a string"}), 400
        
        if not isinstance(data["requires_fasting"], bool):
            return jsonify({"error": "requires_fasting must be a boolean"}), 400
        
        new_booking = DiagnosticExam(
            booking_type=booking_type,
            booking_id=data["booking_id"],
            patient_name=data["patient_name"],
            doctor=data["doctor"],
            department=data["department"],
            date=data["date"],
            time=data["time"],
            status=data["status"],
            exam_type=data["exam_type"],
            requires_fasting=data["requires_fasting"]
        )

    else:
        return jsonify({"error": "'Type' must be visit or exam only"}), 400
    
    ok = clinic_hub.add(new_booking)
    if not ok:
        return jsonify({"error": "Booking id already exist"}), 400
    return jsonify(new_booking.info()), 201

@app.route('/bookings/<string:booking_id>', methods=['PUT'])
def put_booking(booking_id: str):
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Data must be a JSON object"}), 400
    
    booking = clinic_hub.get(booking_id)
    if booking is None:
        return jsonify({"error": "Booking not found"}), 404
    
    if "type" not in data:
        return jsonify({"error": "'Type' field is missing"}), 400
    
    booking_type = data["type"]
    if not isinstance(booking_type, str):
        return jsonify({"error": "'Type' must be a string"}), 400
    
    if booking_type == "visit":
        required_fields = ['patient_name', 'doctor', 'department', 'date', 'time', 'status', 'visit_reason', 'first_time']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        if not isinstance(data["visit_reason"], str):
            return jsonify({"error": "visit_reason must be a string"}), 400
        
        if not isinstance(data["first_time"], bool):
            return jsonify({"error": "first_time must be a boolean"}), 400
        
        new_booking = MedicalVisit(
            booking_id=booking_id,
            booking_type=booking_type,
            patient_name=data["patient_name"],
            doctor=data["doctor"],
            department=data["department"],
            date=data["date"],
            time=data["time"], 
            status=data["status"], 
            visit_reason=data["visit_reason"],
            first_time=data["first_time"]   
        )

    elif booking_type == "exam":
        required_fields = ['patient_name', 'doctor', 'department', 'date', 'time', 'status', 'exam_type', 'requires_fasting']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        if not isinstance(data["exam_type"], str):
            return jsonify({"error": "exam_type must be a string"}), 400
        
        if not isinstance(data["requires_fasting"], bool):
            return jsonify({"error": "requires_fasting must be a boolean"}), 400
        
        new_booking = DiagnosticExam(
            booking_id=booking_id,
            booking_type=booking_type,
            patient_name=data["patient_name"],
            doctor=data["doctor"], 
            department=data["department"],
            date=data["date"],
            time=data["time"],
            status=data["status"],
            exam_type=data["exam_type"],
            requires_fasting=data["requires_fasting"]
        )

    else:
        return jsonify({"error": "Booking type not valid"}), 400
    
    clinic_hub.update(booking_id, new_booking)
    return jsonify(new_booking.info()), 200

@app.route('/bookings/<string:booking_id>/status', methods=['PATCH'])
def patch_booking(booking_id: str):
    booking = clinic_hub.get(booking_id)
    if booking is None:
        return jsonify({"error": "Booking not found"}), 404
    
    data = request.get_json()
    if "status" not in data:
        return jsonify({"error": "Missing required field"}), 400
    
    new_status = data["status"]
    if not isinstance(new_status, str) or not new_status:
        return jsonify({"error": "Status not valid"}), 400
    
    clinic_hub.patch_status(booking_id, new_status)
    return jsonify(clinic_hub.get(booking_id).info()), 200

@app.route('/bookings/<string:booking_id>', methods=['DELETE'])
def delete_booking(booking_id: str):
    deleted = clinic_hub.get(booking_id)
    if not deleted:
        return jsonify({"error": "Booking not found"}), 404
    return jsonify({"deleted": True, "booking_id": booking_id}), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

