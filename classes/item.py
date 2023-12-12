class Item:
    def __init__(self, name: str, price: int | float, seller: object) -> None:
        self._name = name
        self._price = price if price >= 0 else 0
        self._seller = seller
        
    def __str__(self) -> str:
        self.get_name()
        
    def get_name(self) -> str:
        return self._name
    
    def set_name(self, new_name) -> None:
        try:
            if type(new_name) == str and new_name != '':
                self._name = new_name
                
        except:
            print('invalid input')
    
    def get_price(self):
        return self._price

    def set_price(self, new_price: int | float):
        try:
            if new_price < 0:
                raise
                
            self._price = new_price
            
        except:
            print('invalid input')
    