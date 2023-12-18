class UserClient:    
    def __init__(self, name: str) -> None:
        self._id: int | None = None
        self._name = name
    
    def __repr__(self) -> str:
        return self.get_name()

    def __str__(self) -> str:
        return self.get_name()
    
    def get_id(self) -> int:
        return self._id
    
    def set_id(self, id: int) -> None:
        try:
            if type(id) != int:
                raise
            self._id = id
            
        except:
            pass
        
    def get_name(self) -> str:
        return self._name
    
    def set_name(self, new_name: str) -> None:
        try:
            if type(new_name) == str and new_name != '':
                self._name = new_name
                
        except:
            print('invalid input')
            
    
