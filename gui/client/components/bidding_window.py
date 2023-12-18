from typing import Optional, Tuple, Union
from customtkinter import *
from CTkListbox import *


class BiddingWindow(CTkFrame):
    def __init__(self, master: any, 
                 text_label: str,
                 width: int = 400, height: int = 150, 
                 corner_radius: int | str | None = 0, 
                 border_width: int | str | None = 2, 
                 bg_color: str | Tuple[str, str] = "transparent", 
                 fg_color: str | Tuple[str, str] | None = "transparent", 
                 border_color: str | Tuple[str, str] | None = "gainsboro", 
                 background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, 
                 overwrite_preferred_drawing_method: str | None = None, **kwargs):
        
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        
        self.number_of_items = 0
        self.items_for_bidding = []
        
        self.window_label = CTkLabel(master=self, text=f"{text_label}", justify="center")
        self.window_label.grid(row=0, column=0, pady=(8, 0))
        
        self.listbox = CTkListbox(master=self, text_color='black', corner_radius=0, width=width, height=height)
        self.listbox._scrollbar.configure(height=0)
        self.listbox.grid(row=1, column=0, padx=8, pady=8, sticky="nsew")
        
    def insert(self, message: str) -> None:
        self.listbox.insert(index=self.number_of_items, option=message)
        
        self.number_of_items += 1
        
    def get_item_index(self) -> int:
        return self.listbox.curselection()


if __name__ == '__main__':
    class Tester(CTk):
        def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
            super().__init__(fg_color, **kwargs)
                    
            self.grid_columnconfigure(0, weight=1)
            self.grid_rowconfigure(0, weight=1)
            
            self.window = BiddingWindow(master=self, text_label="Item for BIDDING:")
            self.window.grid(row=0, column=0, padx=8, pady=8)
        
        
    app = Tester()
    
    app.mainloop()
    