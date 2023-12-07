from typing import Optional, Tuple, Union
from customtkinter import *


class Utility(CTkFrame):
    def __init__(self, master: any, 
                 width: int = 200, height: int = 200, 
                 corner_radius: int | str | None = 0, 
                 border_width: int | str | None = None, 
                 bg_color: str | Tuple[str, str] = "transparent", 
                 fg_color: str | Tuple[str, str] | None = "transparent", 
                 border_color: str | Tuple[str, str] | None = None, 
                 background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, 
                 overwrite_preferred_drawing_method: str | None = None, **kwargs):
        
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
                
        self.grid_columnconfigure(list(range(2)), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.button_holder = CTkFrame(master=self, fg_color="transparent")
        self.button_holder.grid(row=0, column=0, padx=(8, 0), sticky="ew")
        
        self.bid_button = CTkButton(master=self.button_holder, width=64, text="Bid")
        self.bid_button.grid(row=0, column=0, padx=0, pady=8)
        
        self.sell_button = CTkButton(master=self.button_holder, width=64, text="Sell")
        self.sell_button.grid(row=0, column=1, padx=(8, 0), pady=8)
        
        self.timer = CTkLabel(master=self, text=f"Time Left: 00:00:00")
        self.timer.grid(row=0, column=1, padx=8, sticky="e")


if __name__ == '__main__':
    class Tester(CTk):
        def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
            super().__init__(fg_color, **kwargs)
                    
            self.grid_columnconfigure(0, weight=1)
            
            self.utility = Utility(master=self)
            self.utility.grid(row=0, column=0, padx=10, pady=10)
        
        
    app = Tester()
    
    app.mainloop()
    