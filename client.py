from typing import Optional, Tuple, Union
from gui_components.client_interface.utility import Utility
from gui_components.client_interface.window import Window
from customtkinter import *

        
class ClientInterface(CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        self.title('CLIENT')
        self.minsize(width=300, height=650)
        set_appearance_mode('System')
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(list(range(1, 4)), weight=1)
        
        self.utility = Utility(master=self)
        self.utility.grid(row=0, column=0, padx=8, pady=(8, 0), sticky="nsew")
        
        self.bidding_window = Window(master=self, text_label="Item for BIDDING:")
        self.bidding_window.grid(row=1, column=0, padx=8, pady=(8, 0), sticky="nsew")
        
        self.selling_window = Window(master=self, text_label="Item you are SELLING:")
        self.selling_window.grid(row=2, column=0, padx=8, pady=0, sticky="nsew")
        
        self.bidder_window = Window(master=self, text_label="Highest BIDDER:")
        self.bidder_window.grid(row=3, column=0, padx=8, pady=(0, 8), sticky="nsew")
                
        
if __name__ == '__main__':
    client_interface = ClientInterface()
    client_interface.mainloop()
    