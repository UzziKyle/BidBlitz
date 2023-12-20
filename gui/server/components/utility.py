from typing import Optional, Tuple, Union
from .countdown_setter import CountdownSetter
from customtkinter import *
from threading import Thread, Event
from time import sleep


class Utility(CTkFrame):
    def __init__(self, master: any, 
                 font, func,
                 width: int = 250, height: int = 250, 
                 corner_radius: int | str | None = 0, 
                 border_width: int | str | None = 0, 
                 bg_color: str | Tuple[str, str] = "transparent", 
                 fg_color: str | Tuple[str, str] | None = "transparent", 
                 border_color: str | Tuple[str, str] | None = None, 
                 background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, 
                 overwrite_preferred_drawing_method: str | None = None, **kwargs):
        
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
                        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.func = func
        
        # TODO center position this
        self.countdown_setter = CountdownSetter(self, font=font)
        self.countdown_setter.grid(row=2, column=0, padx=8)
        
        self.countdown_setter.start_button.configure(command=lambda: self.func())


if __name__ == '__main__':
    class Tester(CTk):
        def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
            super().__init__(fg_color, **kwargs)
                    
            self.grid_columnconfigure(0, weight=1)
            
            self.utility = Utility(master=self)
            self.utility.grid(row=0, column=0, padx=10, pady=10)
        
        
    app = Tester()
    
    app.mainloop()
    