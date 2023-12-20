from typing import Optional, Tuple, Union
from customtkinter import *


class Window(CTkScrollableFrame):
    def __init__(self, master: any, font: any,
                 width: int = 200, height: int = 200, 
                 corner_radius: int | str | None = 0, 
                 border_width: int | str | None = None, 
                 bg_color: str | Tuple[str, str] = "transparent", 
                 fg_color: str | Tuple[str, str] | None = None, 
                 border_color: str | Tuple[str, str] | None = None, 
                 background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, 
                 overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        self.font_general, self.font_buttons = font
        
        self.number_of_messages = 0
        
    def insert(self, message: str) -> None:
        new_message = CTkLabel(master=self, text=message, font=self.font_general)
        new_message.grid(row=self.number_of_messages, column=0, padx=8, pady=2, sticky='w')
        
        self.number_of_messages += 1


if __name__ == '__main__':
    class Tester(CTk):
        def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
            super().__init__(fg_color, **kwargs)
                    
            self.grid_columnconfigure(0, weight=1)
            
            self.window = Window(master=self)
            self.window.grid(row=0, column=0, padx=10, pady=10)
        
        
    app = Tester()
    
    app.mainloop()
    