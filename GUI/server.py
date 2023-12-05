from typing import Optional, Tuple, Union
from components.server_interface.countdown_timer import CountdownTimer
from components.server_interface.window import Window
from customtkinter import *

        
class ServerInterface(CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        self.title('SERVER')
        self.geometry('300x400')
        # self.minsize(625, 300)
        set_appearance_mode('System')
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(list(range(1)), weight=1)
        
        self.window = Window(self)
        self.window.grid(row=0, column=0, padx=8, pady=8, sticky="nsew")
        
        self.countdown_timer = CountdownTimer(self)
        self.countdown_timer.grid(row=1, column=0, padx=8, pady=(0, 8), sticky="nsew")
        
        
if __name__ == '__main__':
    server_interface = ServerInterface()
    server_interface.mainloop()
    