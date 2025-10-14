class AppointmentScheduler:
    def __init__(self) -> None:
        self.appointments: dict[str, dict] = {}

    def schedule_appointment(self, app_id: str, data: str) -> dict|str:
        if app_id in self.appointments:
            return "Errore. Appuntamento esiste già."
        else:
            self.appointments[app_id] = {"data": data, "programmato": True}
            return {app_id: self.appointments[app_id]}
    
    def reschedule_appointment(self, app_id: str, nuova_data: str) -> dict|str:
        if app_id not in self.appointments:
            return "Errore. Appuntamento non trovato."
        else:
            self.appointments[app_id]["data"] = nuova_data
            return {app_id: self.appointments[app_id]}
        
    def cancel_appointment(self, app_id: str) -> dict|str:
        if app_id not in self.appointments:
            return "Errore. Appuntamento non trovato."
        else:
            self.appointments[app_id]["programmato"] = False
            return {app_id: self.appointments[app_id]}
    
    def remove_appointment(self, app_id: str) -> dict|str:
        if app_id not in self.appointments:
            return "Errore. Appuntamento non trovato."
        else:
            rimosso = self.appointments.pop(app_id)
            return {app_id: rimosso}
    
    def list_appointments(self) -> list[str]:
        return list(self.appointments.keys())
    
    def get_appointment(self, app_id: str) -> dict|str:
        if app_id not in self.appointments:
            return "Errore. Appuntamento non trovato"
        else:
            return {app_id: self.appointments[app_id]}
        

