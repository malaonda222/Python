class Course:
    def __init__(self, name: str, id: str):
        self.name: str = name 
        self.id: str = id 
        self.mode: str = "Presenza"

    def change_mode(self):
        if self._mode == "Presenza":
            self._mode = "Telematico"
        else:
            self._mode = "Presenza"

    def get_mode(self) -> str:
        return self._mode
    
    def get_info(self) -> tuple[str, str, str]:
        return (self._name, self._id, self._mode)
    
    def get_id(self) -> str:
        return self._id