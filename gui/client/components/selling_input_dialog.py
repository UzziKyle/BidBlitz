from typing import Optional, Tuple, Union
from customtkinter import *


class SellingInputDialog(CTkToplevel):
    def __init__(self, title: str | None = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title(title)

        self.item_label = CTkLabel(master=self, text="Item:")
        self.item_label.grid(row=0, column=0, padx=(16, 8), pady=(24, 8))
        
        self.item_entry = CTkEntry(master=self, width=160, placeholder_text="Enter item here...")
        self.item_entry.grid(row=0, column=1, padx=(0, 16), pady=(16, 8))

        self.price_label = CTkLabel(master=self, text="Price:")
        self.price_label.grid(row=1, column=0, padx=(16, 8), pady=8)
        
        self.price_entry = CTkEntry(master=self, width=160, placeholder_text="Enter price here...")
        self.price_entry.grid(row=1, column=1, padx=(0, 16), pady=8)
        
        self.submit_button = CTkButton(master=self, width=80, text="Accept", corner_radius=0)
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=(8, 16))
        

if __name__ == '__main__':
    class Tester(CTk):
        def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
            super().__init__(fg_color, **kwargs)
                    
            self.grid_columnconfigure(0, weight=1)
            
            self.selling_input_dialog = SellingInputDialog(master=self, title="SELLING...")
        
        
    app = Tester()
    
    app.mainloop()
    