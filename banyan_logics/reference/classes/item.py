from typing import Optional, Tuple, Union


class Item:
    ITEMS_LIST = []
    
    def __init__(self, name: str, price: int | float, seller: object) -> None:
        self._name = name
        self._price = price if price >= 0 else 0
        self._seller_name = seller.get_name()
        self._seller_id = seller.get_id()
        self._bidders = {}
        self._current_highest_bidder: Tuple[str, float | int] | None = None
        
        self.ITEMS_LIST.append(self)
    
    def __repr__(self) -> str:
        return f"{self.get_seller_name()} {self.get_seller_id()} {self.get_name()} @ $ {self.get_price():0.2f}"

    def __str__(self) -> str:
        return self.get_name()
        
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
            
    def get_seller_name(self) -> int:
        return self._seller_name
    
    def get_seller_id(self) -> int:
        return self._seller_id
            
    def get_bidders(self):
        return self._bidders
    
    def add_bidder(self, bidder: object, bid_amount: float | int) -> None:
        try:
            if bidder.get_id() == self.get_seller_id():
                raise
            
            self._bidders[bidder.get_name()] = bid_amount
            
            if self._current_highest_bidder == None:
                self._current_highest_bidder = (bidder.get_name(), bid_amount)
                
            if self._bidders[bidder.get_name()] > self._current_highest_bidder[1]:
                self._current_highest_bidder = (bidder.get_name(), bid_amount)
            
        except:
            pass
        
    def get_highest_bidder(self) -> Tuple[str, float | int]:
        return self._current_highest_bidder
    
    