from typing import Optional, Tuple, Union
from customtkinter import *


class WinnerDialog(CTkToplevel):
    def __init__(self, payload: dict = {}, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title('WINNERS')
        self.minsize(width=300, height=300)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.payload = payload
        self.items = payload['items']
        self.winners = payload['winners']

        self.scrollable_frame = CTkScrollableFrame(master=self, border_width=2, corner_radius=0)
        self.scrollable_frame.grid(row=0, column=0, padx=4, pady=4, sticky='nsew')
        
        for idx, winner in enumerate(self.winners):
            name = winner[0]
            bid = winner[1]
            
            CTkLabel(master=self.scrollable_frame, text=f"{self.items[idx]}: {name} - PHP{bid: ,.2f}").grid(row=idx, column=0, padx=4, sticky='w')
            
        self.set_active()
                
    def set_active(self):
        self.lift()
        self.focus_force()
        self.grab_set()
        self.grab_release()
        
        
        
if __name__ == '__main__':
    class Tester(CTk):
        def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
            super().__init__(fg_color, **kwargs)
                    
            self.grid_columnconfigure(0, weight=1)
            
            self.selling_input_dialog = WinnerDialog(master=self, title="SELLING...")
        
        
    app = Tester()
    
    app.mainloop()
    