#il dizionario è un hashmap: permettono l'accesso agli elementi in modo molto rapido 


# 1. Scrivi dizionario
tasks = {
    "id": {
        "descrizione": " ",
        "completato": False
    }
}

# 2. Crea classe
class TaskManager:
    def __init__(self, tasks: dict[str, dict[str, str|bool]] = {}) -> None:
        self.tasks: dict[str, dict[str, str|bool]] = tasks 
    
    #oppure 
    def __init__(self) -> None:
        self.tasks: dict[str, dict[str, str|bool]] = {} 

    def create_task(self, task_id: str, descrizione: str) -> str|dict:
        if task_id in self.tasks:
            return "Errore. Il task esiste già"
            # oppure 
            raise KeyError("Il task_id è già presente")
        else:
            temp_dict: dict[str, str|bool] = {
                "descrizione": descrizione,
                "completato": False 
            }
            self.tasks[task_id] = temp_dict 
            return {task_id: temp_dict}

            # oppure 
            self.tasks[task_id] = {"descrizione": descrizione, "completato": False}
            return {task_id: self.tasks[task_id]}
        
    def complete_task(self, task_id: str) -> str|dict:
        if task_id not in self.tasks:
            return "Errore. Task inesistente"
        else:
            temp_dict: dict[str, str|bool] = {
                "completato": True 
            }
            self.task[task_id] = temp_dict 
            return {task_id: temp_dict}
            # oppure 
            self.tasks[task_id]["completato"] = True 
            return {task_id: self.tasks[task_id]}
        
    def update_description(self, task_id: str, nuova_descrizione: str) -> str|dict:
        if task_id not in self.tasks:
            return "Errore. Task non trovato"
        else:
            self.tasks[task_id]["descrizione"] = nuova_descrizione
            return {task_id: self.tasks[task_id]}
        
    def remove_task(self, task_id: str) -> dict|str:
        if task_id not in self.tasks:
            return "Errore. Task non trovato"
        else:
            rimosso = self.tasks.pop(task_id) 
            return {task_id: rimosso}
            # oppure key, value = self.tasks.popitem(task_id)
            # return (key, value)
    
    def list_tasks(self) -> list[str]:
        return list(self.tasks.keys())
        # oppure [str(key) for key in self.tasks.keys()]

    def get_tasks(self, task_id: str) -> dict|str:
        if task_id not in self.tasks:
            return "Errore. Task non trovato"
        else:
            return self.tasks[task_id]




h