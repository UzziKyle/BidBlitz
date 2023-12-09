from typing import Optional, Tuple, Union
from .server_components.countdown_setter import CountdownSetter
from .server_components.window import Window
from customtkinter import *

        
class ServerInterface(CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        self.title('SERVER')
        self.geometry('375x500')
        self.minsize(width=375, height=250)
        set_appearance_mode('System')
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        self.timer = CTkLabel(master=self, text=f"Time Left: 00:00:00")
        self.timer.grid(row=0, column=0, padx=8, pady=8, sticky="e")
        
        self.window = Window(self, corner_radius=8)
        self.window.grid(row=1, column=0, padx=8, sticky="nsew")
        
        # TODO center position this
        self.countdown_setter = CountdownSetter(self)
        self.countdown_setter.grid(row=2, column=0, padx=8, sticky="ew")
        
        
if __name__ == '__main__':
    server_interface = ServerInterface()
    server_interface.mainloop()
    