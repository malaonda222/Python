

class Faculty:
    def __init__(self, name: str, id: str):
        self._name = name 
        self._id = id 

    def get_name(self) -> str:
        return self._name 
    
    def get_id(self) -> str:
        return self._id 
    
    