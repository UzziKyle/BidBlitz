class User:
    def __init__(self, name: str) -> None:
        self._name = name
        
        # TODO Figure this out?
        self._selling = {}
        self._bids = {}
        
    def __str__(self) -> str:
        return self.get_name()
        
    def get_name(self) -> str:
        return self._name
    
    def set_name(self, new_name: str) -> None:
        try:
            if type(new_name) == str and new_name != '':
                self._name = new_name
                
        except:
            print('invalid input')
