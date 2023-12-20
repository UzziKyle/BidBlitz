from typing import Optional, Tuple, Union
from .components.utility import Utility
from .components.bidding_window import BiddingWindow
from .components.selling_window import SellingWindow
from .components.bidder_window import BidderWindow
from customtkinter import *
from PIL import Image

        
class ClientInterface(CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry('430x520')
        self.maxsize(width=700, height=700)
        self.minsize(width=375, height=500)
        self.iconbitmap('assets/img/bidblitz.ico')
        
        self.font_general = CTkFont(family='Monospac821 BT', size=14)
        self.font_buttons = CTkFont(family='Monospac821 BT', size=14, weight='bold')
        
        self.font = (self.font_general, self.font_buttons)
        
        set_appearance_mode('System')
        set_default_color_theme('assets/themes/coffee.json')     
                
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((1, 2), weight=1)
        
        self.utility = Utility(master=self, font=(self.font_general, self.font_buttons))
        self.utility.grid(row=0, column=0, columnspan=2, padx=8, pady=8, sticky="nsew")
        
        self.bidding_window = BiddingWindow(master=self, text_label="BID:", font=self.font)
        self.bidding_window.grid(row=1, column=0, padx=(8, 0), pady=0, sticky="nsew")
        
        self.selling_window = SellingWindow(master=self, text_label="SELLING:", font=self.font)
        self.selling_window.grid(row=1, column=1, padx=(0, 8), pady=0, sticky="nsew")
        
        self.bidder_window = BidderWindow(master=self, text_label="BIDDERS:", font=self.font)
        self.bidder_window.grid(row=2, column=0, columnspan=2, padx=8, pady=(0, 8), sticky="nsew")                
        
if __name__ == '__main__':
    client_interface = ClientInterface()
    client_interface.mainloop()
    