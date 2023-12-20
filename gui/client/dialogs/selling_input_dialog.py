from typing import Optional, Tuple, Union
from customtkinter import *


class SellingInputDialog(CTkToplevel):
    def __init__(self, send_message, title: str | None = None, payload: dict = {}, topic: str = '', *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title('')
        self.payload = payload
        self.topic = topic
        self.send_message = send_message
        
        self.heading_font = CTkFont(family='roboto', size=24, weight='bold')
        
        self.title_label = CTkLabel(master=self, text="SELL", font=self.heading_font)
        self.title_label.grid(row=0, column=0, padx=16, pady=12)
        
        self.item_label = CTkLabel(master=self, text="Item:")
        self.item_label.grid(row=1, column=0, padx=(16, 8), pady=(12, 8))
        
        self.item_entry = CTkEntry(master=self, width=160, placeholder_text="Enter item here...")
        self.item_entry.grid(row=1, column=1, padx=(0, 16), pady=(16, 8))

        self.price_label = CTkLabel(master=self, text="Price:")
        self.price_label.grid(row=2, column=0, padx=(16, 8), pady=8)
        
        self.price_entry = CTkEntry(master=self, width=160, placeholder_text="Enter price here...")
        self.price_entry.grid(row=2, column=1, padx=(0, 16), pady=8)
        
        self.submit_button = CTkButton(master=self, width=80, text="Accept", command=lambda: self.submit_button_func())
        self.submit_button.grid(row=3, column=0, columnspan=2, pady=(8, 16))
        
        self.set_active()
                
    def set_active(self):
        self.lift()
        self.focus_force()
        self.grab_set()
        self.grab_release()
        
    def get_inputs(self) -> Tuple[str, int | float]:
        try:
            item = self.item_entry.get()
            price = int(self.price_entry.get())
            
            if price <= 0:
                raise
            
            return item, price
               
        except:
            pass
        
    def submit_button_func(self):
        item, price = self.get_inputs()
        
        self.payload['name'] = item
        self.payload['price'] = price
        
        self.send_message(payload=self.payload, topic=self.topic)
        
        self.destroy()
        
        
        
        
        

if __name__ == '__main__':
    class Tester(CTk):
        def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
            super().__init__(fg_color, **kwargs)
                    
            self.grid_columnconfigure(0, weight=1)
            
            self.selling_input_dialog = SellingInputDialog(master=self, title="SELLING...")
        
        
    app = Tester()
    
    app.mainloop()
    