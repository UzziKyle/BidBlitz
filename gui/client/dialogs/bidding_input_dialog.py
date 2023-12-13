from typing import Optional, Tuple, Union
from customtkinter import *


class BiddingInputDialog(CTkToplevel):
    def __init__(self, title: str | None = None, item: str | None = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title(title)

        self.item_label = CTkLabel(master=self, text=f"{item}:")
        self.item_label.grid(row=0, column=0, padx=(32, 8), pady=32)
        
        self.price_entry = CTkEntry(master=self, width=160, placeholder_text="Enter amount here...")
        self.price_entry.grid(row=0, column=1, padx=(0, 16), pady=32)
        
        self.submit_button = CTkButton(master=self, width=80, text="Accept", corner_radius=0)
        self.submit_button.grid(row=0, column=2, padx=(0, 32), pady=32)
        

if __name__ == '__main__':
    class Tester(CTk):
        def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
            super().__init__(fg_color, **kwargs)
                    
            self.grid_columnconfigure(0, weight=1)
            
            self.selling_input_dialog = BiddingInputDialog(master=self, title="BIDDING...")
        
        
    app = Tester()
    
    app.mainloop()
    