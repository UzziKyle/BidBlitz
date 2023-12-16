class UserServer:
    USERS_LIST = []
    
    def __init__(self, name: str) -> None:
        self._id = len(self.USERS_LIST)
        self._name = name
        
        self.USERS_LIST.append(self)
        
    def __repr__(self) -> str:
        return self.get_name()
    
    def __str__(self) -> str:
        return self.get_name()
    
    def get_id(self) -> int:
        return self._id
        
    def get_name(self) -> str:
        return self._name
    
    def set_name(self, new_name: str) -> None:
        try:
            if type(new_name) == str and new_name != '':
                self._name = new_name
                
        except:
            print('invalid input')
            
    
