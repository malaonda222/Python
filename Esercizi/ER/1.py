class TaskManager:
    def __init__(self, tasks: dict[str, dict] = None):
        self.tasks = tasks if tasks is not None else {}

    def create_task(self, task_id: str, descrizione: str) -> dict | str:
        if task_id in self.tasks:
            raise ValueError("Errore. Task esiste già")
        else:
            self.tasks[task_id] = {"descrizione": descrizione, "completato": False}  
            return {task_id: self.tasks[task_id]}
    
    def complete_tasks(self, task_id: str) -> dict|str:
        if task_id not in self.tasks:
            raise ValueError("Errore. Task non trovato.")
        else:
            self.tasks[task_id]["completato"] = True
            return {task_id: self.tasks[task_id]}
    
    def update_description(self, task_id: str, nuova_descrizione: str) -> dict | str:
        if task_id not in self.tasks:
            raise ValueError("Errore. Task non trovato")
        else:
            self.tasks[task_id]["descrizione"] = nuova_descrizione
            return {task_id: self.tasks[task_id]}
        
    def remove_task(self, task_id: str) -> dict|str:
        if task_id not in self.tasks:
            raise ValueError("Errore. Task non trovato.")
        else:
            rimosso = self.tasks.pop(task_id)
            return {task_id: rimosso}
        
    def list_tasks(self) -> list[str]:
        if not self.list_tasks:
            return []
        else:
            return list(self.tasks.keys())
        
    def get_tasks(self, task_id: str) -> dict|str:
        if task_id not in self.tasks:
            return "Task non trovato"
        else:
            return {task_id: self.tasks[task_id]}
    


tasks = {
    "task_01": {"Descrizione": "blablabla", "Completato": True},
    "task_02": {"Descrizione": "blablabla", "Completato": False},
}
tm = TaskManager(tasks)
create = tm.create_task("task_03", "blaa")
print(create)