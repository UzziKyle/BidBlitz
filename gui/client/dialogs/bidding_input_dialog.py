from typing import Optional, Tuple, Union
from customtkinter import *


class BiddingInputDialog(CTkToplevel):
    def __init__(self, send_message, title: str | None = None, item: str | None = None, payload: dict = {}, topic: str = '', *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title('')
        self.resizable(width=False, height=False)
        self.payload = payload
        self.topic = topic
        self.send_message = send_message
        self.title_font = CTkFont(family="Monospac821 BT", size=20, weight="bold")
        self.title_label = CTkLabel(master=self, text=title, anchor="center", font=self.title_font)
        self.title_label.grid(row=0, column=0, columnspan=3, pady=(15,0), sticky='ew')
        

        self.item_font = CTkFont(family="Monospac821 BT", size=14, weight="normal")
        self.item_label = CTkLabel(master=self, text=f"Amount:", font=self.item_font)
        self.item_label.grid(row=1, column=0, padx=(14, 8), pady=12)
        
        self.bid_entry = CTkEntry(master=self, width=200, placeholder_text="Enter amount here...", font=self.item_font)
        self.bid_entry.grid(row=1, column=1, padx=(0, 16), pady=12)
        
        self.submit_button = CTkButton(master=self, width=80, text="Accept", command=lambda: self.submit_button_func(), corner_radius=4, font=self.item_font)
        self.submit_button.grid(row=1, column=2, padx=(0, 32), pady=16)
        
        self.set_active()
                
    def set_active(self):
        self.lift()
        self.focus_force()
        self.grab_set()
        self.grab_release()
        
    def get_input(self) -> int:
        try:
            bid_amount = int(self.bid_entry.get())
        
            if bid_amount <= 0:
                raise
            
            return bid_amount
        
        except:
            pass
        
    def submit_button_func(self):
        bid_amount = self.get_input()
        
        self.payload['bid_amount'] = bid_amount
        
        self.send_message(payload=self.payload, topic=self.topic)
        
        self.destroy()
        

if __name__ == '__main__':
    class Tester(CTk):
        def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
            super().__init__(fg_color, **kwargs)
                    
            self.grid_columnconfigure(0, weight=1)
            
            self.selling_input_dialog = BiddingInputDialog(master=self, title=None, send_message=None)
        
        
    app = Tester()
    
    app.mainloop()
    