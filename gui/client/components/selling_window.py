from typing import Optional, Tuple, Union
from customtkinter import *
from CTkListbox import *


class SellingWindow(CTkFrame):
    def __init__(self, master: any, 
                 text_label: str,
                 width: int = 400, height: int = 150, 
                 corner_radius: int | str | None = 0):
        
        super().__init__(master, width, height, corner_radius)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
                
        self.number_of_items = 0
        
        self.window_label = CTkLabel(master=self, text=f"{text_label}", justify="left")
        self.window_label.grid(row=0, column=0, pady=(8, 0))
        
        self.display = CTkScrollableFrame(master=self, corner_radius=0, width=width, height=height)
        self.display._scrollbar.configure(height=0)
        self.display.grid(row=1, column=0, padx=8, pady=8, sticky="nsew")
        
    def insert(self, message: str) -> None:        
        text = CTkLabel(master=self.display, text=message)
        text.grid(row=self.number_of_items, column=0, padx=4, sticky='w')
        
        self.number_of_items += 1

if __name__ == '__main__':
    class Tester(CTk):
        def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
            super().__init__(fg_color, **kwargs)
                    
            self.grid_columnconfigure(0, weight=1)
            self.grid_rowconfigure(0, weight=1)
            
            self.window = SellingWindow(master=self, text_label="Item for BIDDING:")
            self.window.grid(row=0, column=0, padx=8, pady=8)
        
        
    app = Tester()
    
    app.mainloop()
    