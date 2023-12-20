from typing import Optional, Tuple, Union
from customtkinter import *
from CTkListbox import *


class BiddingWindow(CTkFrame):
    def __init__(self, master: any, font: any,
                 text_label: str,
                 width: int = 400, height: int = 150, 
                 corner_radius: int | str | None = 0):
        
        super().__init__(master, width, height, corner_radius)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
                
        self.font_list_item = CTkFont(family='Monospac821 BT', size=12)
        self.font_general, self.font_buttons = font

        self.number_of_items = 0
        self.items_for_bidding = []
        
        self.window_label = CTkLabel(master=self, text=f"{text_label}", justify="left", font=self.font_general)
        self.window_label.grid(row=0, column=0, pady=(8, 0))
        
        self.listbox = CTkListbox(master=self, corner_radius=0, width=width, height=height, border_width=2, text_color=('black', 'white'), font=self.font_list_item)
        self.listbox._scrollbar.configure(height=0, width=16)
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
    