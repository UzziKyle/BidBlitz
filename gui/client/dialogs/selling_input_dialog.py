from typing import Optional, Tuple, Union
from customtkinter import *


class SellingInputDialog(CTkToplevel):
    def __init__(self, send_message, title: str | None = None, payload: dict = {}, topic: str = '', *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title('')
        self.resizable(width=False, height=False)
        self.payload = payload
        self.topic = topic
        self.send_message = send_message
        
        self.title_font = CTkFont(family="Monospac821 BT", size=24, weight="bold")
        self.title_label = CTkLabel(master=self, text="Sell Item", font=self.title_font)
        self.title_label.grid(row=0, column=0, padx=12, pady=14, columnspan=2, sticky='w')
        
        self.item_font = CTkFont(family="Monospac821 BT", size=14, weight="normal")        
        self.item_label = CTkLabel(master=self, text="Item:", font=self.item_font)
        self.item_label.grid(row=1, column=0, padx=(16, 8), pady=(10, 10), sticky='w')
        
        self.item_entry = CTkEntry(master=self, width=180, placeholder_text="Enter item here...", font=self.item_font)
        self.item_entry.grid(row=1, column=1, padx=(0, 16), pady=(10, 10))
        self.item_entry.bind('<Return>', self.focus_on_price_entry)

        self.price_label = CTkLabel(master=self, text="Price:", font=self.item_font)
        self.price_label.grid(row=2, column=0, padx=(16, 8), pady=8, sticky='w')
        
        self.price_entry = CTkEntry(master=self, width=180, placeholder_text="Enter price here...", font=self.item_font)
        self.price_entry.grid(row=2, column=1, padx=(0, 16), pady=8)
        self.price_entry.bind('<Return>', self.submit_button_func)
        
        self.submit_button = CTkButton(master=self, width=80, text="Accept", command=lambda: self.submit_button_func(), corner_radius=4, font=self.item_font)
        self.submit_button.grid(row=3, column=0, columnspan=2, pady=(8, 16))
        
        self.set_active()
                
    def set_active(self):
        self.lift()
        self.focus_force()
        self.grab_set()
        self.grab_release()
        
    def focus_on_price_entry(self, event):
        self.price_entry.focus_set()
        
    def get_inputs(self) -> Tuple[str, int | float]:
        try:
            item = self.item_entry.get()
            price = int(self.price_entry.get())
            
            if price <= 0:
                raise
            
            return item, price
               
        except:
            pass
        
    def submit_button_func(self, event=None):
        try:
            item, price = self.get_inputs()
            
            self.payload['name'] = item
            self.payload['price'] = price
            
            self.send_message(payload=self.payload, topic=self.topic)
            
            self.destroy()
            
        except: 
            pass       
        

if __name__ == '__main__':
    class Tester(CTk):
        def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
            super().__init__(fg_color, **kwargs)
                    
            self.grid_columnconfigure(0, weight=1)
            
            self.selling_input_dialog = SellingInputDialog(master=self, title="SELLING...", send_message=None)
        
        
    app = Tester()
    app.mainloop()
    