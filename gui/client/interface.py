from typing import Optional, Tuple, Union
from .components.utility import Utility
from .components.bidding_window import BiddingWindow
from .components.selling_window import SellingWindow
from .components.bidder_window import BidderWindow
from customtkinter import *

        
class ClientInterface(CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        self.minsize(width=300, height=650)
        set_appearance_mode('System')
        set_default_color_theme('assets/themes/coffee.json')        
                
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(list(range(1, 4)), weight=1)
        
        self.utility = Utility(master=self)
        self.utility.grid(row=0, column=0, padx=8, pady=(8, 0), sticky="nsew")
        
        self.bidding_window = BiddingWindow(master=self, text_label="BID:")
        self.bidding_window.grid(row=1, column=0, padx=8, pady=(8, 0), sticky="nsew")
        
        self.selling_window = SellingWindow(master=self, text_label="SELLING:")
        self.selling_window.grid(row=2, column=0, padx=8, pady=0, sticky="nsew")
        
        self.bidder_window = BidderWindow(master=self, text_label="BIDDERS:")
        self.bidder_window.grid(row=3, column=0, padx=8, pady=(0, 8), sticky="nsew")                
        
if __name__ == '__main__':
    client_interface = ClientInterface()
    client_interface.mainloop()
    