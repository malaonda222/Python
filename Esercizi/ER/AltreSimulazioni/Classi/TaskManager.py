class TaskManager:
    def __init__(self) -> None:
        self.tasks: dict[str, dict] = {}

    def add_task(self, task_id: str, descrizione: str, priorita: int) -> dict|str:
        if task_id in self.tasks: 
            return "Errore, task già registrato."
        else:
            self.tasks[task_id] = {"descrizione": descrizione, "completato": False, "priorita": priorita}
            return {task_id: self.tasks[task_id]}
        
    def mark_as_done(self, task_id: str) -> dict|str:
        if task_id not in self.tasks: 
            return "Errore, task già registrato."
        else:
            self.tasks[task_id]["completato"] = True 
            return {task_id: self.tasks[task_id]}
        
    def update_description(self, task_id: str, nuova_descrizione: str) -> dict|str:
        if task_id not in self.tasks:
            return "Errore, task non trovato."
        else:
            self.tasks[task_id]["descrizione"] = nuova_descrizione
            return {task_id: self.tasks[task_id]}
        
    def change_priority(self, task_id: str, nuova_priorita: int) -> dict|str:
        if task_id not in self.tasks:
            return "Errore, task non trovato"
        else:
            self.tasks[task_id]["priorita"] = nuova_priorita
            return {task_id: self.tasks[task_id]}
        
    def remove_task(self, task_id: str) -> dict|str:
        if task_id not in self.tasks:
            return "Errore, task non trovato."
        else:
            rimosso = self.tasks.pop(task_id)
            return {task_id: rimosso}
        
    def list_tasks(self) -> list[str]:
        return list(self.tasks.keys())
    
    def get_task(self, task_id: str) -> dict|str:
        if task_id not in self.tasks:
            return "Errore, task non trovato."
        else:
            return {task_id: self.tasks[task_id]}