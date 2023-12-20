from typing import Optional, Tuple, Union
from customtkinter import *


class UsernameInputDialog(CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("CLIENT")
        self.after(250, lambda: self.iconbitmap('assets/img/bidblitz.ico'))
        self.resizable(width=False, height=False)
        
        self.set_font = CTkFont(family="Monospac821 BT", size=14, weight="normal")
        self.name_label = CTkLabel(master=self, text="Name:", font=self.set_font)
        self.name_label.grid(row=0, column=0, padx=(16, 8), pady=16)
        
        self.name_entry = CTkEntry(master=self, width=160)
        self.name_entry.grid(row=0, column=1, padx=(0, 8), pady=16)
        
        self.accept_button = CTkButton(master=self, width=64, text="Accept", font=self.set_font)
        self.accept_button.grid(row=0, column=2, padx=(0, 16), pady=16)
        
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
            
            self.selling_input_dialog = UsernameInputDialog(master=self)
        
        
    app = Tester()
    app.withdraw()
    app.mainloop()
    